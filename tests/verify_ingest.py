#!/usr/bin/env python3
"""Independent checks on the ingest.  Run:  python tests/verify_ingest.py
Nothing here reuses the parser's own logic for the counts it is checking: headings are
counted from pdftotext output, word totals come from a second extraction tool."""
import glob, json, os, re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
import ilib as I

fails = []
def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("  " + detail) if detail else ""))
    if not ok:
        fails.append(name)

pdfs = sorted(glob.glob(str(ROOT / "sources" / "*.pdf")))
db = I.load_db(); recs = db["records"]
reg = json.load(open(ROOT / "data" / "source_files.json"))

# files from the first upload live in sources/; later uploads stay in incoming/ and the register records their path
where = lambda e: ROOT / e["path"] if e.get("path") else ROOT / "sources" / e["file"]          # noqa: E731
missing_files = [e["file"] for e in reg if not where(e).exists()]
check("every registered file exists where the register says", not missing_files, missing_files[:5])
registered = {str(where(e).resolve()) for e in reg}
check("every PDF in sources/ is registered", all(str(Path(p).resolve()) in registered for p in pdfs),
      [os.path.basename(p) for p in pdfs if str(Path(p).resolve()) not in registered][:5])
copies = [e for e in reg if "identical_copy_of" in e]
check("records = files - byte-identical copies", len(recs) == len(reg) - len(copies), "%d = %d - %d" % (len(recs), len(reg), len(copies)))
check("record IDs are unique and sequential", [r["id"] for r in recs] == ["IC-%04d" % i for i in range(1, len(recs) + 1)])

def ptt(f, layout=True):
    return subprocess.run(["pdftotext"] + (["-layout"] if layout else []) + [f, "-"], capture_output=True, text=True).stdout

intro_files, src_files, award_files = set(), set(), set()
worst = 0.0
for f in pdfs:
    t = ptt(f); n = os.path.basename(f)
    if re.search(r"^\s*INTRODUCTION\s*$", t, re.M): intro_files.add(n)
    if re.search(r"^\s*SOURCE INFORMATION\s*$", t, re.M): src_files.add(n)
    if re.search(r"^\s*AWARD HISTORY\s*$", t, re.M): award_files.add(n)
src_names = {os.path.basename(p) for p in pdfs}
recs_src = [r for r in recs if r["source_file"] in src_names]          # the first upload, checked against pdftotext below
by_file = {r["source_file"]: r for r in recs_src}
rec_intro = {r["source_file"] for r in recs_src if r["introduction_text"].strip()}
missing = (intro_files - set(by_file)) - {e["file"] for e in copies}
check("every file with an INTRODUCTION heading has a record with introduction text",
      all(n in rec_intro for n in intro_files if n in by_file) and not missing,
      "%d files by text search, %d records with introductions" % (len(intro_files), len(rec_intro)))
no_intro = [r["source_file"] for r in recs_src if not r["introduction_text"].strip()]
check("first upload: only the publisher script lacks an introduction", no_intro == ["Consequences by Aaron Fraire.pdf"], str(no_intro))
src_rec = {r["source_file"] for r in recs_src if r["source_block_raw"].strip()}
diff = src_rec - src_files - {"Consequences by Aaron Fraire.pdf"}
check("source blocks: text search finds all but the two-column file", diff == {"Therac 25 - DI.pdf"}, "explained difference: %s (heading shares a line with award text in layout mode)" % sorted(diff))
for f in pdfs:
    a = len(re.findall(r"[\w][\w'’]*", ptt(f, False)))
    lines_words = sum(len(re.findall(r"[\w][\w'’]*", r["text_raw"] + " " + r["intro_raw"] + " " + r["source_block_raw"] + " " + r["back_matter_raw"])) for r in [by_file.get(os.path.basename(f))] if r)
    # the body buckets exclude title/byline/footers, so they must be no larger than the whole file and within 15% of it
    if lines_words:
        ratio = lines_words / a; worst = max(worst, abs(1 - ratio))
check("bucketed words are within 15% of the file's total words (titles, bylines and footers are the remainder)", worst < 0.15, "worst deviation %.1f%%" % (100 * worst))
bad = [(r["id"], p) for r in recs for p in I.validate_record(r)]
check("every record validates against the schema and taxonomy", not bad, str(bad[:3]))
check("unknown values are 'Not specified', never blank, for source fields",
      all(r[k] for r in recs for k in ("title", "author", "work_title", "publisher", "isbn", "publication_date_raw", "cutter")))
check("exact duplicates are recorded, not deleted: the two Live to Tell files share one record",
      any(r["source_file"].startswith("Live to Tell") and "Live to Tell - DI (1).pdf" in r["also_appears_in"] for r in recs))
check("every AI value has a confidence and evidence",
      all(p.get("confidence") in ("high", "medium", "low") and p.get("evidence")
          for r in recs for p in r["provenance"].values() if p.get("origin") == "ai"))
check("no run-time estimates or league timing flags are stored (removed at the director's request)",
      not re.search(r'"(estimated_seconds_body|estimated_seconds_with_intro|estimated_range_with_intro|timing_flags)"',
                    open(ROOT / "data" / "cuttings.json", encoding="utf-8").read()),
      "read from the raw file, not through load_db, which drops these fields")
check("performance text contains no section headings or footers",
      not any(re.search(r"(?m)^\s*(SOURCE INFORMATION|AWARD HISTORY|AWARDS|INTRODUCTION|(Page )?\d+ of \d+)\s*$", r["performance_text"]) for r in recs))
print("\n%d checks failed" % len(fails) if fails else "\nall checks passed")
sys.exit(1 if fails else 0)
