#!/usr/bin/env python3
"""One-time correction (2026-10-08): files loose in incoming/DI and incoming/HI were read before the labelled
folders, so where the same file (byte for byte) also sits in a labelled folder such as 'Female DIs', the record
got no filing label and the labelled copy was noted only as an identical copy.  Give such records the label of the
folder that holds the identical copy.  Only records whose label is empty are changed; each change is logged.

    python pipeline/fill_filing_labels.py            # apply
    python pipeline/fill_filing_labels.py --dry-run  # list what would change
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402
import ingest as G        # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    reg = I.load_json(I.DATA / "source_files.json", []) or []
    labels = {}                                     # record ID -> labels of folders holding identical copies
    for e in reg:
        if e.get("identical_copy_of") and e.get("path"):
            ev, lab = G.folder_info(str(I.ROOT / e["path"]))
            if lab:
                labels.setdefault(e["identical_copy_of"], []).append((lab, ev, e["path"]))
    changed = 0
    with I.DbLock():
        db = I.load_db()
        for r in db["records"]:
            if r["performer_category_as_filed"] not in ("", I.NS) or r["id"] not in labels:
                continue
            found = sorted({lab for lab, ev, _ in labels[r["id"]] if ev == r["event"]})
            if len(found) != 1:                     # none, or copies filed under different labels: leave it for a person
                if found:
                    print("%s: identical copies filed under several labels %s; left empty" % (r["id"], found))
                continue
            path = next(p for lab, ev, p in labels[r["id"]] if lab == found[0])
            print("%s %s: filing label -> %r (from %s)" % (r["id"], r["source_file"], found[0], path))
            if not a.dry_run:
                r["performer_category_as_filed"] = found[0]
                I.set_prov(r, "performer_category_as_filed", "human", evidence="Folder name of an identical copy: " + path)
                r["ingest_notes"].append("Filing label taken from the folder of an identical copy (%s), %s." % (path, I.today()))
                r["date_updated"] = I.today()
                I.derive(r)
            changed += 1
        if changed and not a.dry_run:
            I.save_db(db)
    print("%d record(s) %s" % (changed, "would change (dry run)" if a.dry_run else "given a filing label"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
