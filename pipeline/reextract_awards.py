#!/usr/bin/env python3
"""One-time correction (2026-10-02): the first extraction kept only award lines that start with a year, so undated
lines such as 'MN State Qualifier' or 'NIETOC' were missed.  Re-read the award lines of existing records from their
PDFs with the current parser.  A record is changed only if every old award line is still present (lines are only
added, never lost), and each change is logged in the record's ingest_notes.

    python pipeline/reextract_awards.py            # apply
    python pipeline/reextract_awards.py --dry-run  # list what would change
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402
import layouts as L       # noqa: E402
import ingest as G        # noqa: E402

NOTE = "Award lines re-read on %s: undated award lines (for example state qualifiers) were missed by the first extraction."


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    reg = I.load_json(I.DATA / "source_files.json", []) or []
    # only the records from before this change: their register entries have no "path" (files in sources/)
    path_of = {e["record"]: I.ROOT / "sources" / e["file"] for e in reg if e.get("record") and not e.get("path")}
    changed = 0
    with I.DbLock():
        db = I.load_db()
        for r in db["records"]:
            p = path_of.get(r["id"])
            if r["source_layout"] != "di_cutting" or p is None or not p.exists() or any(n.startswith("Award lines re-read") for n in r["ingest_notes"]):
                continue
            parsed = L.parse_pdf(str(p))
            if parsed["layout"] != "di_cutting":
                continue
            new = G.build_record(r["id"], str(p), parsed, r["source_file_sha1"], r["event"], r["performer_category_as_filed"])["award_history_raw"]
            old_lines = [x for x in r["award_history_raw"].split("\n") if x]
            new_lines = new.split("\n") if new else []
            if new == r["award_history_raw"] or not all(x in new_lines for x in old_lines):
                continue
            print("%s %s: + %s" % (r["id"], r["source_file"], [x for x in new_lines if x not in old_lines]))
            if not a.dry_run:
                r["award_history_raw"] = new
                r["ingest_notes"].append(NOTE % I.today())
                r["date_updated"] = I.today()
                I.derive(r)
            changed += 1
        if not a.dry_run and changed:
            I.save_db(db)
    print("%d record(s) %s" % (changed, "would change (dry run)" if a.dry_run else "corrected"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
