#!/usr/bin/env python3
"""Introduction boundary at a 'Title by Author' phrase, and the 'Cutting compliments of' credit.
(1) A byline inside a sentence does not end the introduction; the sentence stays whole.
(2) A byline that closes its line, or a sentence followed by a stage direction or speaker, still ends it.
(3) A 'Cutting compliments of' line is back matter, never performance text, and the credit stops at the school.
(4) The library holds no record with that line in its performance text and no credit with a note run on to it.
Run:  python tests/test_intro_credit.py      (needs pdfplumber and pdftotext)"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
sys.path.insert(0, str(ROOT / "tests"))
import layouts as L                     # noqa: E402
from _sandbox import check, finish      # noqa: E402

DI, PR, PO = "incoming/DI/Female DIs/", "incoming/Prose/Prose- Female/", "incoming/Poetry/Any Gender Poetry/"


def parse(rel):
    p = ROOT / rel
    if not p.exists():
        check("test file present: " + rel, False)
        return None
    return L.parse_pdf(str(p))


def text(lines):
    return " ".join(l.text for l in lines)


# (1) the sentence holding the byline stays whole
for rel, ending in [(DI + "Bellyfruit - DI.pdf", "This is her story."),
                    (DI + "Fifteen Minutes from Talking With - DI.pdf", "literal and figurative stage of life."),
                    ("sources/Get Up Stand Up - DI.pdf", "and cast.")]:
    d = parse(rel)
    if d:
        check("%s: the introduction ends '... %s'" % (rel.split("/")[-1], ending), text(d["intro_lines"]).rstrip().endswith(ending),
              text(d["intro_lines"])[-120:])
        check("... and every word is kept", L.conservation(d)[0], L.conservation(d)[1])

# (2) the cut still happens where the byline or its sentence ends and a speaker or direction follows
for rel, first in [("incoming/DI/Male DIs/Rest Area - DI.pdf", "GRACE"), (DI + "Susan Smith Tapes - DI.pdf", "[Smith sets up")]:
    d = parse(rel)
    if d:
        check("%s: '%s' is performance text, not introduction" % (rel.split("/")[-1], first),
              first in text(d["performance_lines"]) and first not in text(d["intro_lines"]), text(d["intro_lines"])[-120:])

# (3) the credit line is back matter, and the credit is the cutter and school only
for rel, cutter in [(PO + "Pulse - A Collection of LGBTQ Poetry - PO.pdf", "Rhys Jones of Mound Westonka High School, MN"),
                    (PR + "Impossible Knife of Memory - PR.pdf", "Coach Heather Whitney of Norfolk Public Schools, NE"),
                    (PR + "All the Bright Places - PR.pdf", "Shelly Uttke, Coach at Port Washington High School, WI"),
                    (PR + "Finding Alice - PR.pdf", "Heather Whitney, Norfolk Public Schools, NE"),
                    (PR + "Dreamland - PR.pdf", "Heather Whitney, Norfolk Public Schools, NE")]:
    d = parse(rel)
    if d:
        check("%s: no 'Cutting compliments of' line in the performance text" % rel.split("/")[-1],
              not any(L.CUTTER_LINE_RE.match(l.text.strip()) for l in d["performance_lines"]))
        check("... the cutter credit is %r" % cutter, d["back"]["cutter_credit"] == cutter, d["back"]["cutter_credit"])

# (4) the library itself (after pipeline/fix_intro_and_credit.py)
with open(ROOT / "data" / "cuttings.json", encoding="utf-8") as f:
    recs = json.load(f)["records"]
leak = [r["id"] for r in recs if any(L.CUTTER_LINE_RE.match(x.strip()) for x in r["performance_text"].split("\n"))]
check("no record has a 'Cutting compliments of' line in its performance text", not leak, leak[:10])
runon = [(r["id"], r["cutter"]) for r in recs if r["cutter"] != "Not specified" and
         any(w in r["cutter"].lower() for w in ("selection cut", "from pages", "minor edits", "modifications", "award history"))]
check("no cutter credit has a note run on to it", not runon, runon[:5])
sys.exit(finish())
