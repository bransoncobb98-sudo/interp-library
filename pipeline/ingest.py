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
    if not work and parsed["layout"] == "publisher_script":
        work = parsed["title"]
    put("work_title", work, "Source block" if parsed["layout"] == "di_cutting" else "Copyright page heading")
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
    awards = list(parsed.get("source_awards", [])) + [l.text for l in parsed["back_lines"] if AWARD_LINE.match(l.text)]
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
    if parsed["layout"] == "publisher_script":
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
    r["ingest_notes"] = notes
    return I.derive(r)


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
    by_work = {}
    for r in records:
        if r["source_work_key"]:
            by_work.setdefault(r["source_work_key"], []).append(r["id"])
    for r in records:
        r["same_source_work_ids"] = [i for i in by_work.get(r["source_work_key"], []) if i != r["id"]]
        r["also_appears_in"].sort()
        I.derive(r)


def write_register(reg):
    fd, tmp = tempfile.mkstemp(dir=I.DATA, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(reg, f, indent=1)
        f.write("\n")
    os.replace(tmp, I.DATA / "source_files.json")


def ingest(paths, event, filing_label, dry_run=False, layout=None, out=print):
    """Add PDFs to the database.  Returns (new_records, register_entries, failures, skipped).
    The caller must hold I.DbLock().  Nothing is written if any file fails, or on a dry run."""
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
        name, sha = os.path.basename(p), I.sha1_file(p)
        if name in name_to_sha:
            if name_to_sha[name] == sha:
                skipped.append(name)                     # the same file again: nothing to do
            else:
                failures.append((p, "a different file with this name is already in the library; rename it and try again"))
            continue
        entry = {"file": name, "sha1": sha, "bytes": os.path.getsize(p)}
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
        if parsed["layout"] == "unrecognised":
            failures.append((p, "no parser matched this layout"))
            continue
        ok, detail = L.conservation(parsed)
        if not ok:
            failures.append((p, "conservation check failed: %s" % detail))
            continue
        rid = "IC-%04d" % next_num
        next_num += 1
        rec = build_record(rid, p, parsed, sha, event, filing_label)
        RP.apply_to_record(rec)
        I.derive(rec)
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
    elif failures:
        out("Nothing written because some files failed. Fix the parser or rename the file and re-run.")
    elif new or entries:
        db["records"].extend(new)
        I.save_db(db)                                    # link changes on existing records are saved too
        write_register(reg + entries)
        out("wrote %d new record(s) to %s" % (len(new), I.DB_PATH))
    return new, entries, failures, skipped


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="+")
    ap.add_argument("--event", default="Dramatic Interpretation", choices=I.vocab("event"))
    ap.add_argument("--filing-label", default="")
    ap.add_argument("--layout", choices=[n for n, _, _ in L.PARSERS], help="force one layout parser for these files")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    with I.DbLock():
        _, _, failures, _ = ingest(a.pdfs, a.event, a.filing_label, a.dry_run, a.layout)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
