#!/usr/bin/env python3
"""Column-aware reading.  (1) The 46 files already in the library must parse exactly as stored.
(2) A two-column file must read left column then right, checked against what pdftotext -layout shows.
Run:  python tests/test_columns.py      (needs pdfplumber and pdftotext)"""
import glob
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
sys.path.insert(0, str(ROOT / "tests"))
import layouts as L                     # noqa: E402
import ingest as G                      # noqa: E402
from _sandbox import check, finish      # noqa: E402

with open(ROOT / "data" / "cuttings.json", encoding="utf-8") as f:
    by_file = {r["source_file"]: r for r in json.load(f)["records"]}

# (1) regression on the original files
diffs, two_col = [], []
for p in sorted(glob.glob(str(ROOT / "sources" / "*.pdf"))):
    old = by_file.get(os.path.basename(p))
    if old is None:
        continue                                            # the identical copy
    parsed = L.parse_pdf(p)
    if parsed.get("two_column_pages"):
        two_col.append((os.path.basename(p), parsed["two_column_pages"]))
    if parsed["layout"] != old["source_layout"]:
        diffs.append("%s: layout %s, stored %s" % (old["id"], parsed["layout"], old["source_layout"]))
        continue
    new = G.build_record(old["id"], p, parsed, old["source_file_sha1"], old["event"], old["performer_category_as_filed"])
    for k in ("title", "author", "work_title", "publisher", "isbn", "introduction_text", "text_raw", "source_block_raw", "intro_boundary"):
        if new[k] != old[k]:
            diffs.append("%s %s: %s differs" % (old["id"], old["source_file"], k))
check("the 45 library records parse exactly as stored (title, author, work, publisher, ISBN, introduction, raw text, source block, boundary)",
      not diffs, diffs[:6])
print("info: original files with pages read as two columns (expected: none, or only a two-column source block):", two_col or "none")

# (2) a two-column file
f = ROOT / "incoming" / "Prose" / "Prose- Female" / "Burned Alive - PR.pdf"
if not f.exists():
    check("two-column test file present", False, str(f))
else:
    lay = subprocess.run(["pdftotext", "-layout", "-l", "1", str(f), "-"], capture_output=True, text=True).stdout
    check("pdftotext -layout shows the test file in two columns (right-column text set beside the left column)",
          any(l.find("According to the Washington Post") > 30 for l in lay.splitlines()))
    parsed = L.parse_pdf(str(f))
    check("Burned Alive parses as di_cutting", parsed["layout"] == "di_cutting", parsed["layout"] + " " + " ".join(parsed.get("notes", [])))
    if parsed["layout"] == "di_cutting":
        check("page 1 is read as two columns", 1 in parsed["two_column_pages"], parsed["two_column_pages"])
        check("reading order agrees with pdftotext", (parsed["reading_order_agreement"] or 0) >= 0.95, parsed["reading_order_agreement"])
        rec = G.build_record("IC-T", str(f), parsed, "x", "Prose", "")
        intro, perf = rec["introduction_text"], rec["performance_text"]
        check("title and author come from the left column", rec["title"] == "Burned Alive" and rec["author"] == "Souad", (rec["title"], rec["author"]))
        check("introduction starts in the left column and continues into the right",
              intro.startswith("Honor killings.") and "According to the Washington Post" in intro, intro[:120])
        check("introduction ends with the title-by-author line", re.sub(r"\s+", " ", intro).rstrip().endswith("Burned Alive by Souad."), intro[-80:])
        check("the teaser comes first in the performance text", perf.startswith("(Pg 1) I am a girl."), perf[:80])
        i, j = perf.find("make fun of her."), perf.find("(Pg 2-3) It is a curse in my village")
        check("left-column teaser is followed by the right-column text, not interleaved", 0 < i < j, (i, j))
        check("no right-column words leaked into the teaser", "Washington Post" not in perf[:j])
# (3) prose in two columns is joined into paragraphs; verse in two columns keeps its line breaks
for rel, want in (("incoming/Prose/Prose Any Gender/Birds for Christmas - PR.pdf", "prose"),
                  ("incoming/Poetry/Any Gender Poetry/Lion and Blue - PO.pdf", "verse")):
    f = ROOT / rel
    if not f.exists():
        check("test file present: " + rel, False)
        continue
    parsed = L.parse_pdf(str(f))
    rec = G.build_record("IC-T", str(f), parsed, "x", "Prose", "") if parsed["layout"] == "di_cutting" else None
    check("%s is laid out as %s" % (f.name, want), rec is not None and rec["text_layout"] == want, rec and rec["text_layout"])

# (3b) the last page of a two-column file has only a short right column (the source block): still split
f = ROOT / "incoming" / "Prose" / "Prose Any Gender" / "Chomp - PR.pdf"
if f.exists():
    parsed = L.parse_pdf(str(f))
    check("Chomp: the short last page is read as two columns too", parsed["layout"] == "di_cutting" and 6 in parsed.get("two_column_pages", []),
          (parsed["layout"], parsed.get("two_column_pages")))
    if parsed["layout"] == "di_cutting":
        rec = G.build_record("IC-T", str(f), parsed, "x", "Prose", "")
        check("Chomp: source fields come out clean", (rec["author"], rec["publisher"]) == ("Carl Hiaasen", "Yearling"), (rec["author"], rec["publisher"]))
        check("Chomp: no source heading inside the story", "SOURCE INFORMATION" not in rec["performance_text"])

# (4) a file whose section headings come in an unexpected order is refused, not crashed on
f = ROOT / "incoming" / "Prose" / "Prose- Male" / "Jeffreys Moatmeal Accident - PR.pdf"
if f.exists():
    parsed = L.parse_pdf(str(f))
    check("headings out of order: refused with a note, no crash", parsed["layout"].endswith("sections not in the expected order"), parsed["layout"])
sys.exit(finish())
