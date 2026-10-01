#!/usr/bin/env python3
"""Director-approved corrections to extracted text (data/text_repairs.json).

    python pipeline/repairs.py            # list which repairs are applied and which are waiting
    (build.py and ingest.py apply them automatically)

Rules
  * Only repairs listed in data/text_repairs.json are ever made.
  * Each 'from' string must occur exactly once in the named field, otherwise the repair is
    refused and the build stops.  Nothing is replaced by pattern.
  * The text as extracted stays in text_raw / intro_raw.  Each applied repair is logged in the
    record's ingest_notes, which is also how a repair is recognised as already applied.
  * Only performance_text and introduction_text can be repaired.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I  # noqa: E402

PATH = I.DATA / "text_repairs.json"
RAW_OF = {"performance_text": "text_raw", "introduction_text": "intro_raw"}


class RepairError(Exception):
    pass


def load():
    return (I.load_json(PATH, {}) or {}).get("repairs", [])


def note_for(rp):
    return "Text repair: '%s' -> '%s' in %s (%s Approved: %s). The text before repair is kept in %s." % (
        rp["from"], rp["to"], rp["field"], rp["reason"], rp["approved"], RAW_OF[rp["field"]])


def apply_to_record(rec, repairs=None):
    """Apply every listed repair for this record's file.  Returns the notes of repairs applied now."""
    done = []
    for rp in (load() if repairs is None else repairs):
        if rp["source_file"] != rec["source_file"]:
            continue
        if rp["field"] not in RAW_OF:
            raise RepairError("%s: field %s cannot be repaired" % (rec["id"], rp["field"]))
        note = note_for(rp)
        text = rec[rp["field"]]
        n = text.count(rp["from"])
        if note in rec["ingest_notes"] and n == 0:
            continue                                            # already applied
        if n != 1:
            raise RepairError("%s (%s): '%s' occurs %d times in %s; a repair needs exactly one. Nothing changed."
                              % (rec["id"], rec["source_file"], rp["from"], n, rp["field"]))
        rec[rp["field"]] = text.replace(rp["from"], rp["to"])
        if note not in rec["ingest_notes"]:
            rec["ingest_notes"].append(note)
        rec["date_updated"] = I.today()
        done.append(note)
    return done


def apply_all(db):
    """Validate every repair against the whole database first, then apply.  All or nothing."""
    repairs = load()
    by_file = {}
    for r in db["records"]:
        by_file.setdefault(r["source_file"], []).append(r)
    for rp in repairs:
        if rp["source_file"] not in by_file:
            raise RepairError("repair for '%s' names a file with no record" % rp["source_file"])
    trial = [dict(r, ingest_notes=list(r["ingest_notes"])) for r in db["records"]]
    for r in trial:
        apply_to_record(r, repairs)                             # raises before anything real changes
    applied = []
    for r in db["records"]:
        applied += apply_to_record(r, repairs)
    return applied


def main():
    db = I.load_db()
    repairs = load()
    by_file = {r["source_file"]: r for r in db["records"]}
    for rp in repairs:
        r = by_file.get(rp["source_file"])
        state = "NO RECORD" if not r else ("applied" if note_for(rp) in r["ingest_notes"] else "waiting (runs on next build)")
        print("%-8s %s: '%s' -> '%s'  [%s]" % (r["id"] if r else "-", rp["source_file"], rp["from"], rp["to"], state))
    for rp in (I.load_json(PATH, {}) or {}).get("proposed_not_applied", []):
        print("PROPOSED, NOT APPLIED  %s: '%s' -> '%s'" % (rp["source_file"], rp["from"], rp["to"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
