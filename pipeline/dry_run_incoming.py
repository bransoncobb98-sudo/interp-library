#!/usr/bin/env python3
"""Dry run over incoming/: parse every PDF with the existing layout parsers and report.  Writes NOTHING
to the database; only reports/dry_run/.

    python pipeline/dry_run_incoming.py                  # all of incoming/, 2 worker processes
    python pipeline/dry_run_incoming.py --folder "incoming/HI" --jobs 4

Results are cached per file (by checksum) in reports/dry_run/cache/, so an interrupted run continues
where it stopped.  Outputs:
    reports/dry_run/summary.md     counts per folder, layouts, introduction boundaries, QC findings, failures
    reports/dry_run/files.tsv      one row per file
    reports/dry_run/samples/       full extracted text of a fixed sample of parsed files, for reading
"""
import argparse
import collections
import hashlib
import json
import multiprocessing
import os
import random
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402

OUT = I.ROOT / "reports" / "dry_run"
CACHE = OUT / "cache"
MAP = I.load_json(I.DATA / "incoming_map.json", {}).get("folders", {})
VERSION = "1"                                        # bump to invalidate cached results after a parser change


def folder_info(rel_dir):
    best = max((k for k in MAP if rel_dir == k or rel_dir.startswith(k + "/")), key=len, default=None)
    return MAP.get(best) or {"event": "Not specified", "filing_label": ""}


def code_version():
    h = hashlib.sha1(VERSION.encode())
    for name in ("layouts.py", "ingest.py", "ilib.py", "qc_scan.py"):
        h.update((I.ROOT / "pipeline" / name).read_bytes())
    return h.hexdigest()[:12]


def work(job):
    """Parse one file.  Runs in a worker process; returns a plain dict."""
    path, sha, info, ver = job
    cached = CACHE / (sha + ".json")
    if cached.exists():
        r = json.loads(cached.read_text(encoding="utf-8"))
        if r.get("code_version") == ver and r.get("event") == info["event"] and r.get("filing_label") == info["filing_label"]:
            r["path"] = path
            return r
    import layouts as L
    import ingest as G
    import qc_scan as Q
    out = {"path": path, "sha1": sha, "code_version": ver, "event": info["event"], "filing_label": info["filing_label"]}
    try:
        parsed = L.parse_pdf(path)
        out.update(layout=parsed["layout"], pages=parsed.get("pages"), two_column_pages=len(parsed.get("two_column_pages") or []),
                   order=parsed.get("reading_order_agreement"), notes=parsed.get("notes", []))
        if parsed["layout"] not in [n for n, _, _ in L.PARSERS]:
            out["status"] = "refused: " + parsed["layout"]
        else:
            ok, detail = L.conservation(parsed)
            out["conservation"] = detail
            if not ok:
                out["status"] = "conservation failed"
            else:
                rec = G.build_record("IC-DRY", path, parsed, sha, info["event"], info["filing_label"])
                keep = ("title", "author", "work_title", "publisher", "isbn", "publication_date_raw", "copyright_notice", "cutter",
                        "intro_boundary", "intro_boundary_method", "teaser_present", "word_count", "intro_word_count",
                        "character_count", "speaker_labels", "text_layout", "source_citation", "text_hash", "ingest_notes",
                        "introduction_text", "performance_text", "source_block_raw", "text_raw")
                out["record"] = {k: rec[k] for k in keep}
                out["qc"] = Q.scan_record(rec)
                out["status"] = "parsed"
    except Exception:
        out["status"] = "error"
        out["error"] = traceback.format_exc()[-1500:]
    CACHE.mkdir(parents=True, exist_ok=True)
    cached.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--folder", default="incoming")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--include-library", action="store_true",
                    help="also parse files already in the library (to check the parsers and the two-column threshold on them)")
    a = ap.parse_args()
    root = I.ROOT / a.folder
    files = sorted(str(p.relative_to(I.ROOT)) for p in root.rglob("*")
                   if p.is_file() and p.suffix.lower() == ".pdf" and not p.name.startswith("._"))   # ._ files are macOS metadata, not PDFs
    reg = I.load_json(I.DATA / "source_files.json", []) or []
    lib_sha = {e["sha1"]: e.get("record") or e.get("identical_copy_of") for e in reg}
    db = I.load_db()                                   # read only
    lib_hash = {r["text_hash"]: r["id"] for r in db["records"] if r["text_hash"]}
    ver = code_version()
    jobs, first_of, rows = [], {}, []
    for f in files:
        sha = I.sha1_file(I.ROOT / f)
        info = folder_info(os.path.dirname(f).replace(os.sep, "/"))
        if sha in lib_sha and not a.include_library:
            rows.append({"path": f, "sha1": sha, "status": "in library (same bytes) as " + str(lib_sha[sha]), **info})
        elif sha in first_of:
            rows.append({"path": f, "sha1": sha, "status": "byte-identical copy of " + first_of[sha], **info})
        else:
            first_of[sha] = f
            jobs.append((str(I.ROOT / f), sha, info, ver))
    print("%d files: %d to parse, %d already in the library or copies" % (len(files), len(jobs), len(rows)), flush=True)
    with multiprocessing.Pool(max(1, a.jobs)) as pool:
        for i, r in enumerate(pool.imap(work, jobs, chunksize=4), 1):
            r["path"] = str(Path(r["path"]).relative_to(I.ROOT))
            rows.append(r)
            if i % 50 == 0 or i == len(jobs):
                print("  parsed %d / %d" % (i, len(jobs)), flush=True)
    # exact text duplicates: against the library, then within the upload
    seen_hash = {}
    for r in sorted(rows, key=lambda r: r["path"]):
        if r["status"] != "parsed":
            continue
        h = r["record"]["text_hash"]
        if h in lib_hash:
            r["status"] = "parsed; same text as library record " + lib_hash[h]
        elif h in seen_hash:
            r["status"] = "parsed; same text as " + seen_hash[h]
        else:
            seen_hash[h] = r["path"]
    report(rows, ver, {r["source_file_sha1"]: r for r in db["records"]})


def kind(status):
    if status.startswith("refused:"):
        return status
    return status.split(" as ")[0].split(" of ")[0].split(":")[0] if not status.startswith("parsed;") else "parsed, duplicate text"


def report(rows, ver, lib_by_sha):
    OUT.mkdir(parents=True, exist_ok=True)
    rows.sort(key=lambda r: r["path"])
    cols = ["path", "event", "filing_label", "status", "layout", "pages", "two_column_pages", "order", "intro_boundary", "words",
            "intro_words", "teaser", "speakers", "title", "author", "work_title", "publisher", "qc", "notes"]
    with open(OUT / "files.tsv", "w", encoding="utf-8") as f:
        f.write("\t".join(cols) + "\n")
        for r in rows:
            rec = r.get("record") or {}
            vals = [r["path"], r["event"], r["filing_label"], r["status"], r.get("layout", ""), r.get("pages", ""),
                    r.get("two_column_pages", ""), r.get("order", ""), rec.get("intro_boundary", ""), rec.get("word_count", ""),
                    rec.get("intro_word_count", ""), rec.get("teaser_present", ""), rec.get("character_count", ""),
                    rec.get("title", ""), rec.get("author", ""), rec.get("work_title", ""), rec.get("publisher", ""),
                    "; ".join(sorted({k for k, _ in r.get("qc", [])})), " | ".join(r.get("notes", []) + rec.get("ingest_notes", []))]
            f.write("\t".join(str(v).replace("\t", " ").replace("\n", " ") for v in vals) + "\n")
    by_folder = collections.defaultdict(collections.Counter)
    for r in rows:
        by_folder[os.path.dirname(r["path"])][kind(r["status"])] += 1
    kinds = sorted({k for c in by_folder.values() for k in c})
    md = ["# Dry run over incoming/", "", "Nothing was written to the database. Parser code version %s." % ver, "",
          "## Files by folder", "", "| Folder | Files | " + " | ".join(kinds) + " |", "|---|---|" + "---|" * len(kinds)]
    for d in sorted(by_folder):
        md.append("| %s | %d | %s |" % (d, sum(by_folder[d].values()), " | ".join(str(by_folder[d].get(k, 0)) for k in kinds)))
    tot = collections.Counter(kind(r["status"]) for r in rows)
    md.append("| **Total** | %d | %s |" % (len(rows), " | ".join(str(tot.get(k, 0)) for k in kinds)))
    parsed = [r for r in rows if r["status"].startswith("parsed")]
    md += ["", "## Parsed files (%d)" % len(parsed), "", "| Measure | Count |", "|---|---|"]
    for label, fn in (("layout", lambda r: r["layout"]), ("introduction boundary", lambda r: r["record"]["intro_boundary"]),
                      ("teaser", lambda r: r["record"]["teaser_present"]), ("text layout", lambda r: r["record"]["text_layout"]),
                      ("source citation", lambda r: r["record"]["source_citation"])):
        for v, n in collections.Counter(fn(r) for r in parsed).most_common():
            md.append("| %s: %s | %d |" % (label, v, n))
    md += ["", "## Reading order check", "",
           "Share of 5-word runs in the extracted introduction and performance text that also appear in pdftotext's own",
           "reading-order output. Files below %.2f are refused. Column mistakes keep every word but scramble the order." % 0.85, "",
           "| Agreement | Parsed, one column | Parsed, some pages read as two columns | Refused |", "|---|---|---|---|"]
    for lo in (0, 0.5, 0.7, 0.8, 0.85, 0.9, 0.95, 0.98):
        hi = {0: 0.5, 0.5: 0.7, 0.7: 0.8, 0.8: 0.85, 0.85: 0.9, 0.9: 0.95, 0.95: 0.98, 0.98: 1.01}[lo]
        inr = lambda r: r.get("order") is not None and lo <= r["order"] < hi                        # noqa: E731
        md.append("| %.2f to %.2f | %d | %d | %d |" % (lo, min(hi, 1), sum(1 for r in parsed if inr(r) and not r.get("two_column_pages")),
                  sum(1 for r in parsed if inr(r) and r.get("two_column_pages")),
                  sum(1 for r in rows if r["status"].startswith("refused: reading order") and inr(r))))
    md.append("| not measured | %d | %d | |" % (sum(1 for r in parsed if r.get("order") is None and not r.get("two_column_pages")),
                                              sum(1 for r in parsed if r.get("order") is None and r.get("two_column_pages"))))
    # regression: files already in the library must parse exactly as before
    md += ["", "## Files already in the library, parsed again", ""]
    diffs, same = [], 0
    for r in rows:
        old = lib_by_sha.get(r["sha1"])
        if not old:
            continue
        if not r["status"].startswith("parsed"):
            diffs.append("- `%s` (%s): now %s" % (r["path"], old["id"], r["status"]))
            continue
        rec = r["record"]
        changed = [k for k in ("title", "author", "work_title", "publisher", "introduction_text", "source_block_raw", "text_raw")
                   if rec[k] != old[k]]
        if changed:
            diffs.append("- `%s` (%s): differs in %s" % (r["path"], old["id"], ", ".join(changed)))
        else:
            same += 1
    md += ["%d identical to the stored record (title, author, work, publisher, introduction, source block, raw text)." % same, ""] + diffs
    qc = collections.Counter(k for r in parsed for k, _ in r.get("qc", []))
    md += ["", "## QC findings in parsed files", "", "| Kind | Findings |", "|---|---|"] + ["| %s | %d |" % kv for kv in qc.most_common()]
    md += ["", "### First QC findings of each kind", ""]
    for k in qc:
        ex = [(r["path"], m) for r in parsed for kk, m in r.get("qc", []) if kk == k][:6]
        md += ["**%s**" % k, ""] + ["- `%s`: %s" % (p, m[:220]) for p, m in ex] + [""]
    bad = sorted((r for r in rows if r["status"] in ("conservation failed", "error") or r["status"].startswith("refused")),
                 key=lambda r: (r["status"] != "error", r["status"], r["path"]))      # errors first
    md += ["## Not parsed (%d)" % len(bad), "", "| File | Status | Detail |", "|---|---|---|"]
    for r in bad[:400]:
        det = r.get("error", "").strip().splitlines()[-1:] or [json.dumps(r.get("conservation", "")) if r["status"] == "conservation failed" else " ".join(r.get("notes", []))]
        md.append("| %s | %s | %s |" % (r["path"], r["status"], det[0][:200].replace("|", "/")))
    (OUT / "summary.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    # a fixed sample of parsed files, full text, for reading
    sd = OUT / "samples"
    sd.mkdir(exist_ok=True)
    for old in sd.glob("*.txt"):
        old.unlink()
    rnd = random.Random(20261001)
    by_ev = collections.defaultdict(list)
    for r in parsed:
        by_ev[r["event"]].append(r)
    for ev, rs in by_ev.items():
        for r in rnd.sample(rs, min(6, len(rs))):
            rec = r["record"]
            name = "%s - %s.txt" % (ev, Path(r["path"]).stem)
            (sd / name).write_text("FILE: %s\nTITLE: %s\nAUTHOR: %s\nINTRO BOUNDARY: %s (%s)\n\n=== INTRODUCTION ===\n%s\n\n=== PERFORMANCE TEXT ===\n%s\n\n=== SOURCE BLOCK ===\n%s\n" % (
                r["path"], rec["title"], rec["author"], rec["intro_boundary"], rec["intro_boundary_method"],
                rec["introduction_text"], rec["performance_text"], rec["source_block_raw"]), encoding="utf-8")
    print("wrote %s, %s and %d samples" % ((OUT / "summary.md").relative_to(I.ROOT), (OUT / "files.tsv").relative_to(I.ROOT), len(list(sd.glob("*.txt")))))


if __name__ == "__main__":
    main()
