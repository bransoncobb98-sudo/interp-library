#!/usr/bin/env python3
"""Site build: hidden records never reach the page, only public fields do, text repairs are logged and
idempotent, timing fields are gone, the rights guard and repair guard stop a bad build.
Run:  python tests/test_build_site.py      (standard library only; works on a copy of the project)"""
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _sandbox import check, finish, make, run, raw, records, edit_records, cleanup  # noqa: E402

ALLOWED = {"id", "record_type", "title", "event", "performer_category_as_filed", "author", "work_title", "publisher", "isbn",
           "publication_date_raw", "source_url", "literary_form", "source_block_raw", "source_notes", "cutter", "award_history_raw",
           "copyright_notice", "rights_status", "attribution_note", "source_file", "source_pages", "introduction_text",
           "performance_text", "text_layout", "intro_boundary", "teaser_present", "speaker_labels", "character_count", "word_count",
           "intro_word_count", "source_citation", "web_only_source", "tone", "content_warnings", "difficulty", "performance_demands",
           "audience_level", "themes", "subject_matter", "metadata_confidence", "review_status", "duplicate_status", "human_verified",
           "date_verified", "date_added", "also_appears_in", "ingest_notes", "provenance",
           "selections", "character_bucket", "same_book", "similar_versions"}          # the last three are added for the page
NEVER = ("takedown_log", "rights_note", "text_raw", "intro_raw", "source_file_sha1", "timing_flags", "estimated_seconds")


def snippet(text):
    """A 50-character run of plain words from the middle of a text (survives JSON escaping unchanged)."""
    flat = re.sub(r"\s+", " ", text)
    mid = len(flat) // 2
    for start in list(range(mid, len(flat) - 50)) + list(range(0, mid)):
        s = flat[start:start + 50]
        if re.fullmatch(r"[A-Za-z ,.]+", s) and s.count(" ") >= 5:
            return s
    return None


def payload(html):
    m = re.search(r"const LIB = (\{.*?\});\n\(function\(\)", html, re.S)
    return json.loads(m.group(1)) if m else None


d = make(first_upload_only=True)            # the 45 first-upload records: these files and IDs are fixed in the checks
try:
    orig = records(d)
    HID_TAKEDOWN, HID_ARCHIVED = "IC-0010", "IC-0011"

    def hide(rs):
        rs[HID_TAKEDOWN]["rights_status"] = "Removal requested"
        rs[HID_TAKEDOWN]["provenance"]["rights_status"] = {"origin": "human", "evidence": "Removal request"}
        rs[HID_TAKEDOWN]["takedown_log"] = [{"date": "2026-09-30", "reason": "SECRET-REASON-XYZ", "email": "hidden@example.org"}]
        rs[HID_ARCHIVED]["record_status"] = "Archived"
    edit_records(d, hide)
    p = run(d, "pipeline/build.py")
    check("build succeeds", p.returncode == 0, p.stdout[-400:] + p.stderr[-400:])
    html = (d / "site" / "index.html").read_text(encoding="utf-8")
    lib = payload(html)
    check("the page carries its data as one JSON object", lib is not None)
    recs = records(d)

    # ---- hidden records
    for rid, why in ((HID_TAKEDOWN, "removal requested"), (HID_ARCHIVED, "archived")):
        s = snippet(recs[rid]["performance_text"])
        check("%s record: its ID is nowhere in the page" % why, rid not in html)
        check("%s record: a passage of its text is nowhere in the page" % why, s is not None and s not in html, s)
        check("%s record: its title is not listed" % why, all(r["title"] != recs[rid]["title"] for r in lib["records"]))
    check("takedown reason and email are nowhere in the page", "SECRET-REASON-XYZ" not in html and "hidden@example.org" not in html)
    expect = sorted(i for i, r in recs.items() if r["record_status"] == "Active" and r["rights_status"] not in ("Removal requested", "Removed")
                    and not (r["duplicate_status"] == "Exact Duplicate" and r["duplicate_of"]))
    check("the page lists exactly the visible records (counted from the database file)",
          sorted(r["id"] for r in lib["records"]) == expect, "%d on page, %d expected" % (len(lib["records"]), len(expect)))

    # ---- fields
    keys = set().union(*(r.keys() for r in lib["records"]))
    check("page records carry only allowed fields", keys <= ALLOWED, sorted(keys - ALLOWED))
    check("private and removed field names appear nowhere in the page", not [n for n in NEVER if '"%s"' % n in html],
          [n for n in NEVER if '"%s"' % n in html])
    check("text is stored unaltered: every page text equals the database text",
          all(r["performance_text"] == recs[r["id"]]["performance_text"] and r["introduction_text"] == recs[r["id"]]["introduction_text"] for r in lib["records"]))
    check("no raw '<' in the embedded data (so text cannot close the script tag)",
          "<" not in re.search(r"const LIB = (\{.*?\});\n\(function\(\)", html, re.S).group(1))

    # ---- repairs
    z = next(r for r in recs.values() if r["source_file"] == "Zooman and the Sign - DI.pdf")
    bad = ("MJSSED", "FAMJLY", "FRJENDS", "KJLLED", "JDENTJFY", "if l eva", "KlLLERS")
    check("Zooman: the approved errors are corrected in the stored text", not any(b in z["performance_text"] for b in bad),
          [b for b in bad if b in z["performance_text"]])
    check("Zooman: corrected words are present", all(w in z["performance_text"] for w in ("MISSED", "FAMILY", "FRIENDS", "KILLED", "IDENTIFY", "if I eva", "KILLERS")))
    check("Zooman: the raw extraction still has the original characters", all(b in z["text_raw"] for b in bad), [b for b in bad if b not in z["text_raw"]])
    check("Zooman: seven repairs are logged in ingest_notes", sum(n.startswith("Text repair:") for n in z["ingest_notes"]) == 7)
    check("Zooman: the proposed LESTER TOHNSON change is NOT applied", "LESTER TOHNSON" in z["performance_text"])
    check("Zooman: word count unchanged by the repairs", z["word_count"] == orig[z["id"]].get("word_count"), (z["word_count"], orig[z["id"]].get("word_count")))
    snap = raw(d)
    p = run(d, "pipeline/build.py")
    check("a second build changes nothing in the database (repairs are idempotent)", raw(d) == snap and p.returncode == 0)

    # ---- timing removed
    check("no run-time fields in the database file", not re.search(rb'"(timing_flags|estimated_seconds_body|estimated_seconds_with_intro|estimated_range_with_intro)"', raw(d)))

    # ---- exports
    con = sqlite3.connect(str(d / "exports" / "Interp_Database.sqlite"))
    n = con.execute("select count(*) from cuttings").fetchone()[0]
    check("SQLite export holds every record, hidden ones included", n == len(recs), n)
    try:
        hit = [x[0] for x in con.execute("select id from cuttings_fts where cuttings_fts match 'Zooman'")]
        check("SQLite full-text search finds Zooman", z["id"] in hit, hit)
    except sqlite3.OperationalError:
        check("SQLite full-text table exists (FTS5)", False, "this Python's sqlite has no FTS5")
    con.close()
    check("CSV and JSON exports exist", (d / "exports" / "Interp_Database.csv").exists() and (d / "exports" / "Interp_Database.json").exists())

    # ---- guards
    snap = raw(d)

    def perm(rs):
        rs["IC-0012"]["rights_status"] = "Permission on file"
    edit_records(d, perm)
    bad_db = raw(d)
    p = run(d, "pipeline/build.py")
    check("'Permission on file' without a reviewer and a rights note stops the build", p.returncode == 1 and "may only be set by a reviewer" in p.stdout, p.stdout[-300:])
    check("... and nothing is saved", raw(d) == bad_db)
    (d / "data" / "cuttings.json").write_bytes(snap)
    rp = json.loads((d / "data" / "text_repairs.json").read_text(encoding="utf-8"))
    rp["repairs"].append({"source_file": "Fontaine - DI.pdf", "field": "performance_text", "from": "NO SUCH TEXT 123", "to": "x", "reason": "test", "approved": "test"})
    (d / "data" / "text_repairs.json").write_text(json.dumps(rp), encoding="utf-8")
    p = run(d, "pipeline/build.py")
    check("a repair whose text is not found stops the build", p.returncode == 1 and "occurs 0 times" in p.stdout, p.stdout[-300:])
    check("... and nothing is saved", raw(d) == snap)
finally:
    cleanup(d)
sys.exit(finish())
