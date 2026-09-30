#!/usr/bin/env python3
"""Ingest cutting PDFs into data/cuttings.json.

  python pipeline/ingest.py sources/*.pdf --event "Dramatic Interpretation" --filing-label "Any Gender"
  python pipeline/ingest.py sources/*.pdf --dry-run      # parse and verify only; write nothing

Every file is parsed by the layout parser that matches it (pipeline/layouts.py).
A parse is refused (nothing written) if the word-conservation check fails:
every line of the PDF must land in exactly one bucket.
"""
import argparse
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402
import layouts as L       # noqa: E402

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


def mark_duplicates(records):
    by_hash, changed = {}, []
    for r in records:
        by_hash.setdefault(r["text_hash"], []).append(r)
    for group in by_hash.values():
        stand = group[0]
        for other in group[1:]:
            other["duplicate_status"] = "Exact Duplicate"
            other["duplicate_of"] = [stand["id"]]
            stand["also_appears_in"].append(other["source_file"])
            changed.append(other)
    sh = {r["id"]: shingles(r["performance_text"]) for r in records}
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if a["text_hash"] == b["text_hash"] or not sh[a["id"]] or not sh[b["id"]]:
                continue
            j = len(sh[a["id"]] & sh[b["id"]]) / len(sh[a["id"]] | sh[b["id"]])
            if j >= 0.8:
                b["duplicate_status"] = "Near Duplicate"
                b["duplicate_of"] = sorted(set(b["duplicate_of"] + [a["id"]]))
    # cuttings of the same source work are linked, never treated as duplicates
    by_work = {}
    for r in records:
        if r["source_work_key"]:
            by_work.setdefault(r["source_work_key"], []).append(r["id"])
    for r in records:
        r["same_source_work_ids"] = [i for i in by_work.get(r["source_work_key"], []) if i != r["id"]]
    for r in records:
        I.derive(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdfs", nargs="+")
    ap.add_argument("--event", default="Dramatic Interpretation", choices=I.vocab("event"))
    ap.add_argument("--filing-label", default="")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    paths = sorted(a.pdfs, key=file_order)
    register, records, seen_sha, failures = [], [], {}, []
    db = I.load_db()
    next_num = int(I.next_id(db).split("-")[1])
    known_sha = {r["source_file_sha1"]: r for r in db["records"]}
    for p in paths:
        sha = I.sha1_file(p)
        entry = {"file": os.path.basename(p), "sha1": sha, "bytes": os.path.getsize(p)}
        if sha in seen_sha or sha in known_sha:
            holder = seen_sha.get(sha) or known_sha[sha]
            entry["identical_copy_of"] = holder["id"] if isinstance(holder, dict) and "id" in holder else holder
            holder_rec = next((r for r in records if r["source_file_sha1"] == sha), None) or known_sha.get(sha)
            if holder_rec is not None:
                holder_rec["also_appears_in"].append(entry["file"])
                holder_rec["ingest_notes"].append("Byte-identical copy also supplied as '%s'; one record kept." % entry["file"])
            entry["layout"], entry["pages"] = "identical copy (not parsed again)", None
            register.append(entry)
            continue
        parsed = L.parse_pdf(p)
        entry["layout"], entry["pages"] = parsed["layout"], parsed.get("pages")
        if parsed["layout"] == "unrecognised":
            failures.append((p, "no parser matched this layout"))
            register.append(entry)
            continue
        ok, detail = L.conservation(parsed)
        if not ok:
            failures.append((p, "conservation check failed: %s" % detail))
            register.append(entry)
            continue
        rid = "IC-%04d" % next_num
        next_num += 1
        rec = build_record(rid, p, parsed, sha, a.event, a.filing_label)
        records.append(rec)
        seen_sha[sha] = rec
        entry["record"] = rid
        register.append(entry)

    mark_duplicates(db["records"] + records) if not db["records"] else mark_duplicates(records)
    print("files given: %d | parsed to records: %d | identical copies: %d | failures: %d" % (
        len(paths), len(records), sum(1 for e in register if "identical_copy_of" in e), len(failures)))
    for p, why in failures:
        print("  REFUSED:", os.path.basename(p), "-", why)
    if a.dry_run:
        print("dry run: nothing written")
        return 1 if failures else 0
    if failures:
        print("Nothing written because some files failed. Fix the parser or profile and re-run.")
        return 1
    with I.DbLock():
        db = I.load_db()
        db["records"].extend(records)
        I.save_db(db)
        reg = I.load_json(I.DATA / "source_files.json", []) or []
        reg.extend(register)
        with open(I.DATA / "source_files.json", "w", encoding="utf-8") as f:
            import json
            json.dump(reg, f, indent=1)
    print("wrote %d records to %s" % (len(records), I.DB_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
