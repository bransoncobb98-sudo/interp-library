#!/usr/bin/env python3
"""Programs: several selections, each followed by its own SOURCE INFORMATION block, stored as one record with
the selections in order.  Works on a copy of the project; reads results from the database and page files.
Run:  python tests/test_programs.py      (needs pdfplumber and pdftotext)"""
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _sandbox import ROOT, check, finish, make, run, records, cleanup  # noqa: E402

PROG = ROOT / "incoming" / "Poetry" / "Any Gender Poetry" / "Borders Accents and Weapons - PO.pdf"
ONE = ROOT / "incoming" / "DI" / "Female DIs" / "Southern Utah - Another Tragedy - DI.pdf"
missing = [str(p) for p in (PROG, ONE) if not p.exists()]
if missing:
    check("test files present", False, missing)
    sys.exit(finish())

d = make()
try:
    p = run(d, "pipeline/build.py")
    check("sandbox copy builds", p.returncode == 0, p.stdout[-300:] + p.stderr[-300:])
    shutil.copy2(PROG, d / "sources" / PROG.name)
    shutil.copy2(ONE, d / "sources" / ONE.name)
    p = run(d, "pipeline/ingest.py", "sources/" + PROG.name, "--event", "Poetry", "--filing-label", "Any Gender Poetry")
    check("the program file ingests", p.returncode == 0 and "new records: 1" in p.stdout, p.stdout[-400:] + p.stderr[-600:])
    p = run(d, "pipeline/ingest.py", "sources/" + ONE.name, "--event", "Dramatic Interpretation", "--filing-label", "Female DIs")
    check("the one-piece, two-source file ingests", p.returncode == 0 and "new records: 1" in p.stdout, p.stdout[-400:] + p.stderr[-600:])
    recs = records(d)
    prog = next((r for r in recs.values() if r["source_file"] == PROG.name), None)
    one = next((r for r in recs.values() if r["source_file"] == ONE.name), None)
    if prog:
        sels = prog["selections"]
        check("program: one record of type Program", prog["record_type"] == "Program", prog["record_type"])
        check("program: three selections, in order", [s["order"] for s in sels] == [1, 2, 3], [s["order"] for s in sels])
        check("program: every selection has its own source block", all(s["source_block_raw"].strip() for s in sels))
        check("program: each source names Denice Frohman", all("Denice Frohman" in s["source_block_raw"] for s in sels))
        check("program: selections 2 and 3 begin with the performer's transition", all(s["text"].startswith("TRANSITION") for s in sels[1:]),
              [s["text"][:30] for s in sels])
        check("program: no source-block text inside any selection's text",
              not any(re.search(r"(?m)^(Author|ISBN|Publisher|Date \(Month/Year\)):", s["text"]) for s in sels))
        check("program: award lines stay with their selection, not in the text",
              "KS State Qualifier" in sels[1]["award_history_raw"] and "MN State Qualifier" in sels[2]["award_history_raw"]
              and not any("State Qualifier" in s["text"] for s in sels), [s["award_history_raw"] for s in sels])
        check("program: the performance text is the selections joined in order", prog["performance_text"] == "\n\n".join(s["text"] for s in sels))
        check("program: word counts add up", prog["word_count"] == sum(s["word_count"] for s in sels), (prog["word_count"], [s["word_count"] for s in sels]))
        check("program: introduction stored separately", prog["introduction_text"].strip() and prog["introduction_text"] not in prog["performance_text"])
    if one:
        check("one piece with two source blocks is a Cutting, not a Program", one["record_type"] == "Cutting", one["record_type"])
        check("... and keeps both source blocks as printed", one["source_block_raw"].count("Author:") >= 1 and one["selections"]
              and one["selections"][0]["source_blocks"] == 2, one["selections"][0].get("source_blocks") if one["selections"] else None)
    p = run(d, "pipeline/build.py")
    check("the database builds with a program in it", p.returncode == 0, p.stdout[-300:] + p.stderr[-300:])
    html = (d / "site" / "index.html").read_text(encoding="utf-8")
    m = re.search(r"const LIB = (\{.*?\});\n\(function\(\)", html, re.S)
    lib = json.loads(m.group(1)) if m else {"records": []}
    page = next((r for r in lib["records"] if prog and r["id"] == prog["id"]), None)
    check("the page carries the program with its selections and their sources",
          page is not None and len(page["selections"]) == 3 and all(s["source_block_raw"] for s in page["selections"]))
finally:
    cleanup(d)
sys.exit(finish())
