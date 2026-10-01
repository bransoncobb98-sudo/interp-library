#!/usr/bin/env python3
"""Scan ingested records for problems that counts cannot show.

  python pipeline/qc_scan.py            # print findings
  python pipeline/qc_scan.py --json     # machine-readable

Checks: leaked page headers/footers and section headings, mid-word artifacts,
truncated endings, records starting mid-sentence, bracket/parenthesis balance,
author-name variants inside one file, suspicious lengths, introductions that
do not look like introductions.
"""
import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I  # noqa: E402

LEAK_PATTERNS = [
    (r"(?m)^\s*(Page\s+)?\d+\s+of\s+\d+\s*$", "page footer"),
    (r"(?m)^\s*SOURCE INFORMATION\s*$", "source-block heading"),
    (r"(?m)^\s*AWARD(S| HISTORY)\s*$", "award heading"),
    (r"(?m)^\s*INTRODUCTION\s*$", "introduction heading"),
    (r"(?i)\bISBN\s*:", "ISBN line"),
    (r"(?i)\bPublisher\s*:", "publisher line"),
    (r"(?i)cutting\s+compliments\s+of", "cutter credit"),
    (r"(?i)\bNational Qualifier\b", "award text"),
    (r"\f", "form feed"),
]
TERMINAL = tuple('.!?"”’)]…—-:;\'*')


def words_of(t):
    return re.findall(r"[\w'’-]+", t)


def scan_record(r):
    f = []
    perf, intro = r["performance_text"], r["introduction_text"]
    for pat, what in LEAK_PATTERNS:
        for field, txt in (("performance_text", perf), ("introduction_text", intro)):
            m = re.search(pat, txt)
            if m:
                f.append(("leak", "%s in %s: %r" % (what, field, txt[max(0, m.start() - 25):m.end() + 25])))
    # mid-word artifacts
    for field, txt in (("performance_text", perf), ("introduction_text", intro)):
        if re.search("[\ufffd\ue000-\uf8ff]", txt):
            f.append(("artifact", "replacement or private-use character in " + field))
        for m in re.finditer(r"(?<![\w'’.-])([b-hj-zB-HJ-Z])(?![\w'’.-])\s", txt):          # stray single letters (not I, a, A)
            ctx = txt[max(0, m.start() - 20):m.end() + 20].replace("\n", " ")
            if not re.search(r"[A-Z]\s*:|\b[Pp]g\b|\b[A-Z]\.\s|#|\b(Mr|Ms|Dr)\b", ctx):
                f.append(("artifact", "stray single letter %r in %s: ...%s..." % (m.group(1), field, ctx)))
                break
        if re.search(r"\w-\s+[a-z]", txt) and field == "performance_text":
            m = re.search(r"\w-\s+[a-z]\w*", txt)
            f.append(("artifact", "possible unjoined hyphenation: %r" % m.group(0)))
        if "  " in txt:
            f.append(("artifact", "double space in " + field))
    # truncated endings
    tail = perf.rstrip()[-1:] if perf.strip() else ""
    if tail and tail not in TERMINAL:
        f.append(("truncated", "performance text ends without closing punctuation: ...%s" % perf.rstrip()[-60:].replace("\n", " ")))
    itail = intro.rstrip()[-1:] if intro.strip() else ""
    ends_with_credit = bool(re.search(r"\bby\s+[A-Z][\w.'’ -]+$", intro.strip().replace("\n", " "), re.I))
    if itail and itail not in TERMINAL and not ends_with_credit and not re.search(r"staff$", intro.strip()):
        f.append(("truncated", "introduction ends without closing punctuation: ...%s" % intro.rstrip()[-60:].replace("\n", " ")))
    # starts mid-sentence
    first = perf.lstrip()[:1]
    if first and (first.islower() or first in ",;)]") and r["text_layout"] != "verse":
        f.append(("mid-sentence start", "performance text starts: %s..." % perf.lstrip()[:60].replace("\n", " ")))
    if intro.strip() and not intro.lstrip()[:1].isupper() and not intro.lstrip()[:1] in "\"“'‘•(…[0123456789*":
        f.append(("mid-sentence start", "introduction starts: %s..." % intro.lstrip()[:60].replace("\n", " ")))
    # balance
    for field, txt in (("performance_text", perf), ("introduction_text", intro)):
        if txt.count("(") != txt.count(")"):
            f.append(("balance", "%s has %d '(' and %d ')'" % (field, txt.count("("), txt.count(")"))))
        if txt.count("[") != txt.count("]"):
            f.append(("balance", "%s has %d '[' and %d ']'" % (field, txt.count("["), txt.count("]"))))
    # author-name variants inside one file
    m = re.search(r"\bby\s+([A-Z][\w.'’-]+(?:\s+[A-Z][\w.'’-]+){0,3})[.\s]*$", intro.strip())
    if m and r["author"] != I.NS:
        strip = lambda w: re.sub(r"[^\w]", "", w).lower()        # noqa: E731
        a_sur, i_sur = strip(r["author"].split(",")[0].split()[-1]), strip(m.group(1).split()[-1])
        if a_sur != i_sur:
            f.append(("name variant", "byline author %r but introduction ends 'by %s'" % (r["author"], m.group(1))))
    # capital J where a capital I is expected (a font-encoding error seen in one source)
    jt = sorted(set(re.findall(r"\b[A-Z]*(?:[BCDFGHKLMNPQRSTVWXZ]J[A-Z]+|J[BCDFGHKLMNPQRSTVWXZ][A-Z]*)\b", perf)))
    jt = [w for w in jt if len(w) >= 4]
    if jt:
        f.append(("font encoding", "capital J where I is expected, possibly a text-layer error: %s" % ", ".join(jt)))
    # sizes
    if r["word_count"] < 400:
        f.append(("length", "only %d spoken words" % r["word_count"]))
    if r["word_count"] > 2600:
        f.append(("length", "%d spoken words (long)" % r["word_count"]))
    if r["intro_word_count"] > 260:
        f.append(("length", "introduction is %d words" % r["intro_word_count"]))
    if r["source_layout"] == "di_cutting" and r["intro_word_count"] == 0:
        f.append(("length", "no introduction text found"))
    return f


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    db = I.load_db()
    ack = I.load_json(I.DATA / "qc_acknowledged.json", []) or []
    # An acknowledgement says a finding is present in the source PDF itself.  It must give a reason.
    # "resolved" marks one whose cause was since corrected (for example by text_repairs.json).
    live = [x for x in ack if not x.get("resolved")]
    bad_ack = [x for x in ack if not (x.get("reason") or "").strip()]
    used = set()
    out = {}
    for r in db["records"]:
        fl = []
        for k, m in scan_record(r):
            hit = [i for i, x in enumerate(live) if x["source_file"] == r["source_file"] and x["kind"] == k and x["contains"] in m]
            used.update(hit)
            if not hit:
                fl.append((k, m))
        if fl:
            out[r["id"]] = {"file": r["source_file"], "findings": fl}
    stale = [x for i, x in enumerate(live) if i not in used]
    if a.json:
        print(json.dumps({"findings": out, "stale_acknowledgements": stale, "acknowledgements_without_reason": bad_ack}, indent=1))
        return 0
    kinds = {}
    for rid, d in out.items():
        for k, _ in d["findings"]:
            kinds[k] = kinds.get(k, 0) + 1
    print("records scanned: %d | records with findings: %d" % (len(db["records"]), len(out)))
    print("finding kinds:", kinds or "none")
    for rid, d in sorted(out.items()):
        print("\n%s  %s" % (rid, d["file"]))
        for k, msg in d["findings"]:
            print("   [%s] %s" % (k, msg))
    if stale:
        print("\nAcknowledgements that no longer match any finding (check, then mark 'resolved' or remove the cause):")
        for x in stale:
            print("   %s [%s] %r" % (x["source_file"], x["kind"], x["contains"]))
    if bad_ack:
        print("\nAcknowledgements without a reason (every one needs a reason):")
        for x in bad_ack:
            print("   %s [%s] %r" % (x["source_file"], x["kind"], x["contains"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
