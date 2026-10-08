#!/usr/bin/env python3
"""One-time correction (2026-10-08) for three parser faults found after the ingest of incoming/:
  1. An introduction ending with lines after a 'Title by Author' phrase that sat INSIDE a sentence ('Missing Natalie
     by Nicole Blackman brings to life ...') was cut at that phrase, and the rest of the sentence was moved into the
     performance text.  The cut is now made only when the byline closes its line (or, inside a sentence, at the end
     of that sentence when the italic lines after it open with a stage direction or speaker).
  2. A 'Cutting compliments of ...' line (and the notes after it) at the end of the text stayed in the performance
     text.  It is now back matter, and the cutter credit is read from it.
  3. The cutter credit ran on to the end of the back matter ('... Norfolk Public Schools, NE Selection cut from
     pages: 14, 50 ...').  It now stops at the end of the credit; the notes stay in back_matter_raw.
Records whose introduction was cut at a byline, or whose performance text holds a 'Cutting compliments of' line, are
read again from their PDFs.  A record is changed only if
  * the file reads into the same layout and record type as before,
  * no text field was set by a person and no text repair has been applied (those are left for a hand check), and
  * the words of introduction + performance text + back matter are exactly the same before and after (words only move
    between fields; none are added or lost).
Records with a cutter credit are read again too; for those only the credit changes, and only when the new credit is
the start of the old one (a credit that would change in any other way is held for a hand check).
Each change is logged in the record's ingest_notes.  Duplicate links are then recomputed (the text hash changes).

    python pipeline/fix_intro_and_credit.py            # apply
    python pipeline/fix_intro_and_credit.py --dry-run  # list what would change
"""
import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402
import layouts as L       # noqa: E402
import ingest as G        # noqa: E402

TEXT_FIELDS = ("introduction_text", "performance_text", "intro_raw", "text_raw", "back_matter_raw",
               "intro_boundary", "intro_boundary_method", "selections")
RETYPE_FIELDS = ("record_type", "work_title", "publisher", "isbn", "publication_date_raw", "source_url", "source_work_key",
                 "source_citation", "web_only_source", "award_history_raw")
NOTE_TAIL_RE = re.compile(r"(?i)\s*(\*\s*)?(with|selection|from|minor|edited|formatting)\b|\W*$")   # what may be cut off a credit
NOTE = ("Text boundaries re-read on %s: %s.  Words only moved between the introduction, performance text and back "
        "matter; none were added or lost.")


def squash(s):
    return re.sub(r"\s+", " ", s).strip().lower()


def bag(r):
    return collections.Counter(I.WORD_RE.findall(" ".join((r["introduction_text"], r["performance_text"], r["back_matter_raw"])).lower()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    reg = I.load_json(I.DATA / "source_files.json", []) or []
    path_of = {e["record"]: I.ROOT / (e["path"] if e.get("path") else "sources/" + e["file"])
               for e in reg if e.get("record") and not e.get("identical_copy_of")}
    changed, held = 0, []
    with I.DbLock():
        db = I.load_db()
        for r in db["records"]:
            cut = r["intro_boundary_method"].startswith("font+byline (trailing")
            credit = any(L.CUTTER_LINE_RE.match(x.strip()) for x in r["performance_text"].split("\n"))
            if not (cut or credit or r["cutter"] != I.NS):
                continue
            fields = TEXT_FIELDS if (cut or credit) else ()      # a record picked for its credit only: only the credit changes
            p = path_of.get(r["id"])
            why = None
            if p is None or not p.exists():
                why = "PDF not found"
            elif fields and (any(I.prov_origin(r, k) == "human" for k in fields) or any(n.startswith("Text repair:") for n in r["ingest_notes"])):
                why = "text set or repaired by a person"
            if why is None:
                parsed = L.parse_pdf(str(p))
                if parsed.get("layout") != r["source_layout"]:
                    why = "the file no longer reads the same way (%s)" % parsed.get("layout")
                elif not L.conservation(parsed)[0]:
                    why = "word-conservation check failed: %s" % L.conservation(parsed)[1]
            if why is None:
                new = G.build_record(r["id"], str(p), parsed, r["source_file_sha1"], r["event"], r["performer_category_as_filed"])
                # a program whose only 'second selection' was the credit line is one piece: a Cutting
                retype = (credit and r["record_type"] == "Program" and new["record_type"] == "Cutting" and len(new["selections"]) == 1
                          and len(r["selections"]) == 2 and not r["selections"][1]["source_block_raw"]
                          and not any(I.prov_origin(r, k) == "human" for k in RETYPE_FIELDS))
                if new["record_type"] != r["record_type"] and not retype:
                    why = "record type would change (%s -> %s)" % (r["record_type"], new["record_type"])
                elif fields and bag(new) != bag(r):
                    why = "the words would not be the same before and after"
                elif new["cutter"] != r["cutter"] and r["cutter"] != I.NS and not (
                        new["cutter"] != I.NS and squash(r["cutter"]).startswith(squash(new["cutter"]))
                        and NOTE_TAIL_RE.match(r["cutter"][len(new["cutter"]):])):
                    why = "cutter credit would change from %r to %r" % (r["cutter"], new["cutter"])
                elif I.prov_origin(r, "cutter") == "human" and new["cutter"] != r["cutter"]:
                    why = "cutter credit set by a person"
            if why is not None:
                held.append((r["id"], r["source_file"], why))
                continue
            if all(new[k] == r[k] for k in fields) and new["cutter"] == r["cutter"]:
                continue
            what = []
            if new["introduction_text"] != r["introduction_text"]:
                what.append("introduction %d -> %d words" % (r["intro_word_count"], new["intro_word_count"]))
            if credit:
                what.append("the 'Cutting compliments of' line and what follows it moved to back matter")
            if new["cutter"] != r["cutter"]:
                what.append("cutter credit %r -> %r (notes after the credit stay in back matter)" % (r["cutter"], new["cutter"]))
            if new["record_type"] != r["record_type"]:
                what.append("record type Program -> Cutting (the credit line had been read as a second selection with no "
                            "source; the file holds one piece)")
                fields = fields + RETYPE_FIELDS
            print("%s %s: %s" % (r["id"], r["source_file"], "; ".join(what) or "boundary method only"))
            if not a.dry_run:
                for k in fields:
                    r[k] = new[k]
                    if k in new["provenance"]:
                        r["provenance"][k] = new["provenance"][k]
                if new["cutter"] != r["cutter"]:
                    r["cutter"] = new["cutter"]
                    r["provenance"]["cutter"] = new["provenance"]["cutter"]
                r["ingest_notes"].append((NOTE if fields else "Cutter credit re-read on %s: %s.") % (I.today(), "; ".join(what) or "boundary method recorded"))
                r["date_updated"] = I.today()
                I.derive(r)
            changed += 1
        if changed and not a.dry_run:
            G.mark_duplicates(db["records"], reg)
            for r in db["records"]:
                I.derive(r)
            I.save_db(db)
    for rid, f, why in held:
        print("HELD for a hand check: %s %s: %s" % (rid, f, why))
    print("%d record(s) %s; %d held for a hand check" % (changed, "would change (dry run)" if a.dry_run else "corrected", len(held)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
