#!/usr/bin/env python3
"""Ingest cutting PDFs into data/cuttings.json.

  python pipeline/ingest.py sources/*.pdf --event "Dramatic Interpretation" --filing-label "Any Gender"
  python pipeline/ingest.py sources/*.pdf --dry-run      # parse and verify only; write nothing
  python pipeline/ingest.py FILE.pdf --layout di_cutting   # force a layout parser

Re-running is safe: a file already in the library (same name, same bytes) is skipped; a byte-identical
copy under another name is recorded on the existing record; duplicates are checked against EVERY record.

Every file is parsed by the layout parser that matches it (pipeline/layouts.py).
A parse is refused (nothing written) if the word-conservation check fails:
every line of the PDF must land in exactly one bucket.
"""
import argparse
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402
import layouts as L       # noqa: E402
import repairs as RP      # noqa: E402

LEAKED_HEADING_RE = re.compile(r"(?m)^\s*(SOURCE INFORMATION|AWARD HISTORY|AWARDS|INTRODUCTION|(Page )?\d+ of \d+)\s*$")
EXCLUDED = (I.load_json(I.DATA / "excluded_files.json", {}) or {}).get("rules", [])
AWARDISH = re.compile(r"(?i)\b(qualifier|finalist|semifinalist|quarterfinalist|champion|winner|place|nietoc|ncfl|toc|tournament)\b")
AWARD_LINE = re.compile(r"^(19|20)\d\d\s+(National|State|District|Regional|NIETOC|NCFL|TOC)\b", re.I)


def norm_name(s):
    return re.sub(r"[^a-z0-9]+", " ", (s or "").lower()).strip()


def file_order(path):
    n = os.path.basename(path)
    return (1 if re.search(r"\(\d+\)\.pdf$", n) else 0, n.lower())


def build_record(rid, path, parsed, sha, event, filing_label):
    r = I.new_record()
    src = parsed["source_fields"]
    name = os.path.basename(path)
    r["id"] = rid
    r["record_type"] = "Cutting"
    r["source_file"], r["source_file_sha1"] = name, sha
    r["source_pages"], r["source_layout"] = parsed["pages"], parsed["layout"]
    r["date_added"] = r["date_updated"] = I.today()
    notes = list(parsed["notes"])
    L_clean = lambda s: L.clean_chars(s, notes)           # noqa: E731

    def put(field, value, evidence, origin="source"):
        if value and value != I.NS:
            r[field] = L_clean(value)
            I.set_prov(r, field, origin, evidence=evidence)

    put("title", parsed["title"], "Title lines at the top of page 1")
    put("author", parsed["byline_author"], "Byline: By " + parsed["byline_author"]) if parsed["byline_author"] else None
    work = src.get("Book") or src.get("Magazine") or src.get("Journal") or src.get("Title")
    standalone = parsed["layout"] == "publisher_script" or (parsed["layout"] == "mcp" and parsed.get("variant") != "classic")
    if not work and standalone:
        work = parsed["title"]                           # a script published on its own is its own work
    put("work_title", work, {"di_cutting": "Source block", "publisher_script": "Copyright page heading",
                             "mcp": "Published script (title page)"}.get(parsed["layout"], "Source block"))
    put("publisher", src.get("Publisher"), "Publisher: " + src.get("Publisher", ""))
    put("isbn", src.get("ISBN") or src.get("ISSN"), "ISBN/ISSN: " + (src.get("ISBN") or src.get("ISSN") or ""))
    put("publication_date_raw", src.get("Date"), "Date: " + src.get("Date", ""))
    put("source_url", src.get("Weblink") or src.get("URL") or src.get("Website"), "Web link in the source block")
    if parsed["copyright"]:
        r["copyright_notice"] = parsed["copyright"]
        I.set_prov(r, "copyright_notice", "source", evidence="Copyright page, exactly as given")
    r["source_block_raw"] = L.raw_text(parsed["source_lines"])
    r["source_notes"] = list(parsed.get("source_notes", []))
    cutter = parsed["back"].get("cutter_credit")
    put("cutter", cutter, "Back matter: Cutting compliments of ...")
    back_raw = L.raw_text(parsed["back_lines"])
    r["back_matter_raw"] = back_raw
    awards = list(parsed.get("source_awards", []))
    back = parsed["back_lines"]
    i_aw = next((i for i, l in enumerate(back) if L.is_heading(l, "AWARD HISTORY") or L.is_heading(l, "AWARDS")), None)
    if i_aw is not None:
        # the award lines printed under the heading, dated or not; stop at the first line that is not an award
        # (notes, links and credits that follow stay in back_matter_raw only)
        for l in back[i_aw + 1:]:
            if L.is_heading(l) or not AWARDISH.search(l.text) or len(l.text) > 90 or l.text.lstrip()[:1] in "*(" \
                    or re.match(r"(?i)\s*(note|http|cutting\s+compliments)", l.text):
                break
            awards.append(l.text)
    else:
        awards += [l.text for l in back if AWARD_LINE.match(l.text)]
    r["award_history_raw"] = "\n".join(awards)

    r["event"] = event
    I.set_prov(r, "event", "human", evidence="Filed by the uploader in the folder for this event")
    if filing_label:
        r["performer_category_as_filed"] = filing_label
        I.set_prov(r, "performer_category_as_filed", "human", evidence="Folder name in the upload")

    r["introduction_text"] = L.lines_to_text(parsed["intro_lines"], notes)
    r["performance_text"] = L.lines_to_text(parsed["performance_lines"], notes)
    r["intro_raw"] = L.raw_text(parsed["intro_lines"])
    r["text_raw"] = L.raw_text(parsed["performance_lines"])
    r["intro_boundary_method"] = parsed["intro_method"]
    if parsed["layout"] in ("publisher_script", "mcp"):
        r["intro_boundary"] = "Not applicable"
    elif parsed["intro_method"].startswith("font only"):
        r["intro_boundary"] = "Medium"
        notes.append("Introduction boundary rests on the font change only (no 'Title by Author' end marker). "
                     "Checked against the rendered text by the assistant; not yet reviewed by a person.")
    else:
        r["intro_boundary"] = "High"
    r["teaser_present"] = "Yes" if L.words(L.raw_text(parsed["teaser_lines"])) > 0 else "No"

    # source checks (what the file states; never a legality claim)
    has_pub, has_id, has_date = bool(r["publisher"] != I.NS), bool(r["isbn"] != I.NS), bool(r["publication_date_raw"] != I.NS)
    r["source_citation"] = "Complete" if has_pub and (has_id or has_date) else ("Partial" if any((has_pub, has_id, has_date, r["work_title"] != I.NS)) else "Not stated")
    r["web_only_source"] = "Yes" if r["source_url"] != I.NS and not (has_pub or has_id or r["work_title"] != I.NS) else "No"
    I.set_prov(r, "source_citation", "computed")
    I.set_prov(r, "web_only_source", "computed")
    I.set_prov(r, "intro_boundary", "computed")
    I.set_prov(r, "teaser_present", "computed")
    r["source_work_key"] = re.sub(r"\D", "", r["isbn"]) if has_id and re.sub(r"\D", "", r["isbn"]) else \
        (norm_name(r["work_title"]) + "|" + norm_name(r["author"]) if r["work_title"] != I.NS else "")
    if parsed["layout"] == "program":
        build_program_fields(r, parsed, notes, L_clean)
    r["ingest_notes"] = notes
    return I.derive(r)


def citation(publisher, isbn, date, work):
    has = [v != I.NS for v in (publisher, isbn, date)]
    return "Complete" if has[0] and (has[1] or has[2]) else ("Partial" if any(has) or work != I.NS else "Not stated")


def work_key(isbn, work, author):
    digits = re.sub(r"\D", "", isbn) if isbn != I.NS else ""
    return digits if digits else (norm_name(work) + "|" + norm_name(author) if work != I.NS else "")


def build_program_fields(r, parsed, notes, clean):
    """A program is one record; its selections are listed in order, each with its own text and source."""
    r["record_type"] = "Program"
    sels = []
    for n, s in enumerate(parsed["selections"], 1):
        f = s["fields"]
        val = lambda *keys: next((clean(f[k]) for k in keys if f.get(k)), I.NS)       # noqa: E731
        text = L.lines_to_text(s["text_lines"], notes)
        sel = {"order": n, "position": "before the introduction" if s["before_intro"] else "after the introduction",
               "text": text, "word_count": I.count_words(text),
               "author": val("Author", "Authors"), "work_title": val("Book", "Magazine", "Journal", "Title"),
               "publisher": val("Publisher"), "isbn": val("ISBN", "ISSN"), "publication_date_raw": val("Date"),
               "source_url": val("Weblink", "URL", "Website", "Web Link"),
               "source_block_raw": L.raw_text(s["source_lines"]), "source_notes": list(s["src_notes"]),
               "award_history_raw": "\n".join(l.text for l in s["award_lines"]),
               "source_blocks": (1 + s.get("extra_source_headings", 0)) if s["source_lines"] else 0}
        sel["source_citation"] = citation(sel["publisher"], sel["isbn"], sel["publication_date_raw"], sel["work_title"]) \
            if sel["source_block_raw"] else "Not stated"
        sel["source_work_key"] = work_key(sel["isbn"], sel["work_title"], sel["author"])
        sels.append(sel)
    r["selections"] = sels
    I.set_prov(r, "selections", "source", evidence="Selections and their source blocks, in the order printed in the file")
    r["performance_text"] = "\n\n".join(s["text"] for s in sels if s["text"])
    r["award_history_raw"] = "\n".join(s["award_history_raw"] for s in sels if s["award_history_raw"])
    cits = [s["source_citation"] for s in sels]
    r["source_citation"] = "Complete" if all(c == "Complete" for c in cits) else \
        ("Not stated" if all(c == "Not stated" for c in cits) else "Partial")
    r["web_only_source"] = "Yes" if all(s["source_url"] != I.NS and s["publisher"] == I.NS and s["isbn"] == I.NS
                                        and s["work_title"] == I.NS for s in sels) else "No"
    r["source_work_key"] = ""
    if len(sels) == 1:
        # one piece with more than one source block (for example a play and the anthology it was printed in)
        r["record_type"] = "Cutting"
        s = sels[0]
        for k in ("work_title", "publisher", "isbn", "publication_date_raw", "source_url"):
            if s[k] != I.NS:
                r[k] = s[k]
                I.set_prov(r, k, "source", evidence="Source block in the file")
        r["source_work_key"] = s["source_work_key"]
        notes.append("One piece with %d source blocks; where the blocks repeat a field the later value is used. "
                     "All blocks are kept as printed in source_block_raw." % s["source_blocks"])
    else:
        notes.append("Program with %d selections, each with its own source block." % len(sels))


def shingles(text, n=4):
    w = I.norm_for_hash(text).split()
    return {" ".join(w[i:i + n]) for i in range(max(0, len(w) - n + 1))}


def mark_duplicates(records, register):
    """Recompute duplicate links across ALL records (existing and new).  Idempotent: running it twice
    gives the same result, and nothing is appended to a list that is not first rebuilt.
    Values a reviewer set (origin human) are never changed.  The earliest ID stands for a group."""
    records = sorted(records, key=lambda r: r["id"])
    by_id = {r["id"]: r for r in records}
    human = lambda r, k: I.prov_origin(r, k) == "human"          # noqa: E731
    for r in records:
        if not human(r, "duplicate_status"):
            r["duplicate_status"] = "Unique"
        if not human(r, "duplicate_of"):
            r["duplicate_of"] = []
        r["also_appears_in"] = []
    # byte-identical files that were never parsed
    for e in register:
        holder = by_id.get(e.get("identical_copy_of"))
        if holder is not None and e["file"] not in holder["also_appears_in"]:
            holder["also_appears_in"].append(e["file"])
    # identical spoken words in different files
    by_hash = {}
    for r in records:
        if r["performance_text"].strip():
            by_hash.setdefault(r["text_hash"], []).append(r)
    for group in by_hash.values():
        stand = group[0]
        for other in group[1:]:
            if not human(other, "duplicate_status"):
                other["duplicate_status"] = "Exact Duplicate"
            if not human(other, "duplicate_of"):
                other["duplicate_of"] = [stand["id"]]
            if other["source_file"] not in stand["also_appears_in"]:
                stand["also_appears_in"].append(other["source_file"])
    # near duplicates: same piece, small differences
    sh = {r["id"]: shingles(r["performance_text"]) for r in records}
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if a["text_hash"] == b["text_hash"] or not sh[a["id"]] or not sh[b["id"]]:
                continue
            if len(sh[a["id"]] & sh[b["id"]]) / len(sh[a["id"]] | sh[b["id"]]) >= 0.8:
                if not human(b, "duplicate_status") and b["duplicate_status"] == "Unique":
                    b["duplicate_status"] = "Near Duplicate"
                if not human(b, "duplicate_of") and a["id"] not in b["duplicate_of"]:
                    b["duplicate_of"] = sorted(b["duplicate_of"] + [a["id"]])
    # cuttings from the same book or work are linked, never treated as duplicates
    # a program is linked through the source work of each of its selections
    keys = lambda r: {k for k in [r["source_work_key"]] + [s.get("source_work_key", "") for s in r["selections"]] if k}   # noqa: E731
    by_work = {}
    for r in records:
        for k in keys(r):
            by_work.setdefault(k, []).append(r["id"])
    for r in records:
        r["same_source_work_ids"] = sorted({i for k in keys(r) for i in by_work.get(k, []) if i != r["id"]})
        r["also_appears_in"].sort()
        I.derive(r)


def write_register(reg):
    fd, tmp = tempfile.mkstemp(dir=I.DATA, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=1)
        f.write("\n")
    os.replace(tmp, I.DATA / "source_files.json")


def write_refused(failures):
    """Record the files that were refused, with the reason, for a hand check.  Replaces earlier entries for the same file."""
    path = I.DATA / "refused_files.json"
    old = I.load_json(path, {}) or {}
    for p, why in failures:
        old[os.path.relpath(p, I.ROOT)] = {"reason": why, "date": I.today()}
    fd, tmp = tempfile.mkstemp(dir=I.DATA, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(dict(sorted(old.items())), f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, path)


def folder_info(path):
    """Event and filing label for a file in incoming/, from data/incoming_map.json (longest matching folder)."""
    folders = (I.load_json(I.DATA / "incoming_map.json", {}) or {}).get("folders", {})
    rel = os.path.dirname(os.path.relpath(path, I.ROOT)).replace(os.sep, "/")
    best = max((k for k in folders if rel == k or rel.startswith(k + "/")), key=len, default=None)
    info = folders.get(best) or {"event": "Not specified", "filing_label": ""}
    return info["event"], info["filing_label"]


def ingest(paths, event, filing_label, dry_run=False, layout=None, out=print, info_for=None, keep_going=False):
    """Add PDFs to the database.  Returns (new_records, register_entries, failures, skipped).
    The caller must hold I.DbLock().  Nothing is written on a dry run.  Normally nothing is written if any file
    fails; with keep_going the files that pass are written and the refused ones are listed in
    data/refused_files.json for a hand check (they are not registered, so a later run tries them again).
    info_for(path) -> (event, filing_label) gives each file its own event and label."""
    db = I.load_db()
    reg = I.load_json(I.DATA / "source_files.json", []) or []
    sha_to_id = {r["source_file_sha1"]: r["id"] for r in db["records"] if r.get("source_file_sha1")}
    for e in reg:
        rid = e.get("record") or e.get("identical_copy_of")
        if rid:
            sha_to_id.setdefault(e["sha1"], rid)
    name_to_sha = {e["file"]: e["sha1"] for e in reg}
    name_to_sha.update({r["source_file"]: r["source_file_sha1"] for r in db["records"] if r.get("source_file_sha1")})
    next_num = int(I.next_id(db).split("-")[1])
    new, entries, failures, skipped = [], [], [], []
    for p in sorted(paths, key=file_order):
        name = os.path.basename(p)
        if name.startswith("._"):
            continue                                     # macOS metadata file, not a PDF
        why = next((x["reason"] for x in EXCLUDED if re.search(x["pattern"], name)), None)
        if why:
            out("  EXCLUDED: %s - %s" % (name, why))
            continue
        sha = I.sha1_file(p)
        if name in name_to_sha:
            if name_to_sha[name] == sha:
                skipped.append(name)                     # the same file again: nothing to do
            else:
                failures.append((p, "a different file with this name is already in the library; rename it and try again"))
            continue
        entry = {"file": name, "path": os.path.relpath(p, I.ROOT).replace(os.sep, "/"), "sha1": sha, "bytes": os.path.getsize(p)}
        if sha in sha_to_id:
            entry["identical_copy_of"] = sha_to_id[sha]
            entry["layout"], entry["pages"] = "identical copy (not parsed again)", None
            holder = next((r for r in db["records"] + new if r["id"] == sha_to_id[sha]), None)
            if holder is not None:
                msg = "Byte-identical copy also supplied as '%s'; one record kept." % name
                if msg not in holder["ingest_notes"]:
                    holder["ingest_notes"].append(msg)
            entries.append(entry)
            name_to_sha[name] = sha
            continue
        parsed = L.parse_pdf(p, force=layout)
        entry["layout"], entry["pages"] = parsed["layout"], parsed.get("pages")
        if parsed["layout"] not in [n for n, _, _ in L.PARSERS]:
            failures.append((p, "%s: %s" % (parsed["layout"], " ".join(parsed.get("notes", [])))))
            continue
        ok, detail = L.conservation(parsed)
        if not ok:
            failures.append((p, "conservation check failed: %s" % detail))
            continue
        rid = "IC-%04d" % next_num
        next_num += 1
        ev, lab = info_for(p) if info_for else (event, filing_label)
        rec = build_record(rid, p, parsed, sha, ev, lab)
        RP.apply_to_record(rec)
        I.derive(rec)
        if LEAKED_HEADING_RE.search(rec["performance_text"]):
            # a section heading inside the text means the sections were split wrongly
            failures.append((p, "a section heading or page footer is inside the performance text; needs a hand check"))
            next_num -= 1
            continue
        new.append(rec)
        entry["record"] = rid
        entries.append(entry)
        sha_to_id[sha], name_to_sha[name] = rid, sha
    mark_duplicates(db["records"] + new, reg + entries)
    out("files given: %d | new records: %d | identical copies: %d | already in the library: %d | failures: %d" % (
        len(paths), len(new), sum(1 for e in entries if "identical_copy_of" in e), len(skipped), len(failures)))
    for p, why in failures:
        out("  REFUSED: %s - %s" % (os.path.basename(p), why))
    for r in new:
        if r["duplicate_status"] != "Unique":
            out("  %s %s: %s of %s" % (r["id"], r["source_file"], r["duplicate_status"], ", ".join(r["duplicate_of"])))
    if dry_run:
        out("dry run: nothing written")
    elif failures and not keep_going:
        out("Nothing written because some files failed. Fix the parser or rename the file and re-run.")
    elif new or entries or failures:
        if failures:
            write_refused(failures)
        db["records"].extend(new)
        I.save_db(db)                                    # link changes on existing records are saved too
        write_register(reg + entries)
        out("wrote %d new record(s) to %s" % (len(new), I.DB_PATH))
    return new, entries, failures, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="*")
    ap.add_argument("--incoming", action="store_true", help="every PDF under incoming/, each with the event and label of its folder (data/incoming_map.json)")
    ap.add_argument("--keep-going", action="store_true", help="write the files that pass; list refused ones in data/refused_files.json")
    ap.add_argument("--event", default="Dramatic Interpretation", choices=I.vocab("event"))
    ap.add_argument("--filing-label", default="")
    ap.add_argument("--layout", choices=[n for n, _, _ in L.PARSERS], help="force one layout parser for these files")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    with I.DbLock():
        if a.incoming:
            paths = sorted(str(p) for p in (I.ROOT / "incoming").rglob("*") if p.is_file() and p.suffix.lower() == ".pdf")
            _, _, failures, _ = ingest(paths, a.event, a.filing_label, a.dry_run, a.layout, info_for=folder_info, keep_going=a.keep_going)
        else:
            _, _, failures, _ = ingest(a.pdfs, a.event, a.filing_label, a.dry_run, a.layout, keep_going=a.keep_going)
    return 1 if failures and not a.keep_going else 0


if __name__ == "__main__":
    sys.exit(main())
