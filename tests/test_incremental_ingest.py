#!/usr/bin/env python3
"""Incremental ingest: duplicates are checked against EXISTING records, re-running changes nothing.
Run:  python tests/test_incremental_ingest.py      (needs pdfplumber; works on a copy of the project)"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _sandbox import check, finish, make, run, raw, records, register, edit_records, cleanup  # noqa: E402

LIVE, FONT = "Live to Tell - DI.pdf", "Fontaine - DI.pdf"
d = make([LIVE, FONT])
try:
    p = run(d, "pipeline/build.py")                        # bring the copy up to the current schema first
    check("sandbox copy builds", p.returncode == 0, p.stdout[-300:] + p.stderr[-300:])
    before, reg0 = raw(d), register(d)
    recs0 = records(d)
    live_id = next(i for i, r in recs0.items() if r["source_file"] == LIVE)
    font_id = next(i for i, r in recs0.items() if r["source_file"] == FONT)

    # 1. the same file again: nothing changes
    p = run(d, "pipeline/ingest.py", "sources/" + LIVE)
    check("re-running a file already in the library exits cleanly", p.returncode == 0, p.stdout.strip()[-200:] + p.stderr[-300:])
    check("... reports it as already in the library", "already in the library: 1" in p.stdout)
    check("... leaves cuttings.json byte-for-byte unchanged", raw(d) == before)
    check("... leaves source_files.json unchanged", register(d) == reg0)

    # 2. a byte-identical copy under a new name: recorded on the existing record, not parsed again
    shutil.copy2(d / "sources" / LIVE, d / "sources" / "Live to Tell copy 2.pdf")
    p = run(d, "pipeline/ingest.py", "sources/Live to Tell copy 2.pdf")
    recs1 = records(d)
    check("identical copy under a new name creates no record", len(recs1) == len(recs0), "%d -> %d" % (len(recs0), len(recs1)))
    check("... the existing record lists it in also_appears_in (and keeps the earlier copy)",
          {"Live to Tell - DI (1).pdf", "Live to Tell copy 2.pdf"} <= set(recs1[live_id]["also_appears_in"]), recs1[live_id]["also_appears_in"])
    reg1 = register(d)
    check("... the register gains one entry pointing at the existing record",
          len(reg1) == len(reg0) + 1 and reg1[-1].get("identical_copy_of") == live_id, reg1[-1])
    changed = [i for i in recs0 if i != live_id and recs0[i] != recs1[i]]
    check("... no other record changed", not changed, changed[:5])

    # 3. different bytes, same text: an exact duplicate of an EXISTING record
    (d / "sources" / "Fontaine resaved.pdf").write_bytes((d / "sources" / FONT).read_bytes() + b"\n%resaved\n")
    p = run(d, "pipeline/ingest.py", "sources/Fontaine resaved.pdf")
    recs2 = records(d)
    new = [i for i in recs2 if i not in recs1]
    check("a re-saved copy with the same text is parsed into one new record", len(new) == 1, p.stdout.strip()[-300:] + p.stderr[-500:])
    if new:
        n = recs2[new[0]]
        check("... it is marked Exact Duplicate of the existing record",
              n["duplicate_status"] == "Exact Duplicate" and n["duplicate_of"] == [font_id], (n["duplicate_status"], n["duplicate_of"]))
        check("... the existing record lists the new file in also_appears_in", "Fontaine resaved.pdf" in recs2[font_id]["also_appears_in"])
        check("... the new record's ID follows the last ID", new[0] == "IC-%04d" % (max(int(i[3:]) for i in recs1) + 1), new[0])

    # 4. re-running everything changes nothing
    snap = raw(d)
    pdfs = sorted(str(x.relative_to(d)) for x in (d / "sources").glob("*.pdf"))
    p = run(d, "pipeline/ingest.py", *pdfs)
    check("re-running every file in sources/ changes nothing", raw(d) == snap and p.returncode == 0, p.stdout.strip()[-200:])

    # 5. a different file under an existing name is refused, nothing written
    (d / "sources" / "renamed.pdf").write_bytes((d / "sources" / FONT).read_bytes() + b"\n%other\n")
    shutil.move(str(d / "sources" / "renamed.pdf"), str(d / "sources" / LIVE))
    p = run(d, "pipeline/ingest.py", "sources/" + LIVE)
    check("a changed file under an existing name is refused", p.returncode == 1 and "REFUSED" in p.stdout, p.stdout.strip()[-200:])
    check("... and nothing is written", raw(d) == snap)

    # 6. a reviewer's duplicate decision survives a later ingest
    if new:
        def mark(rs):
            rs[new[0]]["duplicate_status"] = "Unique"
            rs[new[0]]["provenance"]["duplicate_status"] = {"origin": "human", "evidence": "test"}
        edit_records(d, mark)
        shutil.copy2(d / "sources" / FONT, d / "sources" / "Fontaine third.pdf")
        run(d, "pipeline/ingest.py", "sources/Fontaine third.pdf")
        check("a reviewer-set duplicate status is not overwritten by a later ingest", records(d)[new[0]]["duplicate_status"] == "Unique")
finally:
    cleanup(d)
sys.exit(finish())
