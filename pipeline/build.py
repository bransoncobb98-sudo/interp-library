#!/usr/bin/env python3
"""Validate the database and regenerate every output.

    python pipeline/build.py            # apply approved text repairs, validate, build everything
    python pipeline/build.py --check    # validate only (still saves recomputed fields)

Outputs
    site/index.html                  the searchable library: one file, all data inside, works offline
    exports/Interp_Database.json / .csv / .sqlite   the WHOLE database (including hidden records): admin use only
    exports/Interp_Taxonomy.md, Interp_Schema.md, Interp_Source_Report.md

What reaches the site: only records that are Active and not hidden by a removal request, and only the
fields listed in PUBLIC_FIELDS.  Takedown logs, reviewer rights notes, raw extraction text and file
checksums never reach the page.  An exact duplicate is shown once, on the record that stands for it.
"""
import argparse
import collections
import csv
import html
import json
import re
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I  # noqa: E402
import repairs as RP  # noqa: E402

HIDDEN_RIGHTS = ("Removal requested", "Removed")
PUBLIC_FIELDS = [
    "id", "record_type", "title", "event", "performer_category_as_filed",
    "author", "work_title", "publisher", "isbn", "publication_date_raw", "source_url", "literary_form",
    "source_block_raw", "source_notes", "cutter", "award_history_raw", "copyright_notice", "rights_status",
    "attribution_note", "source_file", "source_pages", "introduction_text", "performance_text", "text_layout",
    "intro_boundary", "teaser_present", "speaker_labels", "character_count", "word_count", "intro_word_count",
    "source_citation", "web_only_source", "tone", "content_warnings", "difficulty", "performance_demands",
    "audience_level", "themes", "subject_matter", "metadata_confidence", "review_status", "duplicate_status",
    "human_verified", "date_verified", "date_added", "also_appears_in", "ingest_notes", "provenance", "selections",
]
FACETS = ["event", "record_type", "tone", "content_warnings", "difficulty", "audience_level", "literary_form",
          "teaser_present", "character_bucket", "performance_demands", "review_status"]
CHAR_BUCKETS = {"No speaker labels": "The text has no uppercase speaker labels (often one narrator).",
                "1 labelled speaker": "", "2 to 3 labelled speakers": "", "4 to 6 labelled speakers": "",
                "7 or more labelled speakers": ""}


def character_bucket(n):
    if not n:
        return "No speaker labels"
    return "1 labelled speaker" if n == 1 else "2 to 3 labelled speakers" if n <= 3 else \
        "4 to 6 labelled speakers" if n <= 6 else "7 or more labelled speakers"


# ------------------------------------------------------------- validation --
def validate(db):
    errors, warnings = [], []
    ids = [r["id"] for r in db["records"]]
    errors += ["%s: duplicate ID" % i for i, n in collections.Counter(ids).items() if n > 1]
    idset = set(ids)
    for r in db["records"]:
        errors += ["%s: %s" % (r["id"], p) for p in I.validate_record(r)]
        for k in ("duplicate_of", "same_source_work_ids"):
            errors += ["%s: %s points to unknown ID %s" % (r["id"], k, x) for x in r[k] if x not in idset]
        errors += ["%s: provenance for unknown field '%s'" % (r["id"], k) for k in r["provenance"] if k not in I.FIELD]
        if r["human_verified"] and r["review_status"] != "Verified":
            errors.append("%s: verified but status is %s" % (r["id"], r["review_status"]))
        if r["rights_status"] in ("Permission on file", "Public domain (per source)"):
            if I.prov_origin(r, "rights_status") != "human" or not r["rights_note"].strip():
                errors.append("%s: rights status '%s' may only be set by a reviewer, with the basis in rights_note"
                              % (r["id"], r["rights_status"]))
        if r["rights_status"] == "Removal requested" and not r["takedown_log"]:
            warnings.append("%s: removal requested but the takedown log is empty" % r["id"])
        # text-loss check against the raw extraction (repairs change letters, not word counts)
        if r["source_layout"] in ("di_cutting", "publisher_script") and r["text_raw"]:
            raw = I.count_words(r["text_raw"].replace("-\n", ""))
            if raw and abs(raw - r["word_count"]) / raw > 0.02:
                warnings.append("%s: performance text has %d spoken words but the raw extraction has %d; check for lost text"
                                % (r["id"], r["word_count"], raw))
    return errors, warnings


# ------------------------------------------------------------------- site --
def is_hidden(r):
    return r["record_status"] != "Active" or r["rights_status"] in HIDDEN_RIGHTS


def public_records(db):
    """Returns (records for the page, redirects from hidden exact duplicates to the record shown)."""
    recs = {r["id"]: r for r in db["records"]}
    # a removal request covers the text, so identical copies of a hidden text stay hidden too
    taken_down = {r["text_hash"] for r in db["records"] if r["rights_status"] in HIDDEN_RIGHTS and r["text_hash"]}
    visible = {i for i, r in recs.items() if not is_hidden(r) and r["text_hash"] not in taken_down}
    folded = {i for i in visible if recs[i]["duplicate_status"] == "Exact Duplicate"
              and any(o in visible for o in recs[i]["duplicate_of"])}
    shown = visible - folded
    hidden_files = {recs[i]["source_file"] for i in recs if i not in visible}
    redirects = {}
    for i in folded:
        target = next(o for o in recs[i]["duplicate_of"] if o in visible)
        seen = {i}
        while target in folded and target not in seen:
            seen.add(target)
            target = next(o for o in recs[target]["duplicate_of"] if o in visible)
        if target in shown:
            redirects[i] = target
    out = []
    for i in sorted(shown):
        r = recs[i]
        p = {k: r[k] for k in PUBLIC_FIELDS}
        p["provenance"] = {k: v for k, v in r["provenance"].items() if k in PUBLIC_FIELDS}
        p["character_bucket"] = character_bucket(r["character_count"])
        p["same_book"] = [{"id": o, "title": recs[o]["title"], "author": recs[o]["author"]}
                          for o in r["same_source_work_ids"] if o in shown]
        p["similar_versions"] = sorted(
            {o for o in r["duplicate_of"] if o in shown and r["duplicate_status"] == "Near Duplicate"} |
            {x["id"] for x in recs.values() if x["id"] in shown and x["duplicate_status"] == "Near Duplicate" and i in x["duplicate_of"]})
        p["similar_versions"] = [{"id": o, "title": recs[o]["title"]} for o in p["similar_versions"]]
        p["also_appears_in"] = sorted((set(r["also_appears_in"]) - hidden_files) |
                                      {recs[x]["source_file"] for x in folded if redirects.get(x) == i})
        out.append(p)
    return out, redirects


def site_taxonomy():
    out = {}
    for key in FACETS:
        if key == "character_bucket":
            out[key] = {"label": "Labelled speakers", "multi": False, "values": CHAR_BUCKETS}
        elif key == "teaser_present":
            out[key] = {"label": "Teaser before the introduction", "multi": False, "values": I.TAX["fields"]["yes_no"]["values"]}
        else:
            s = I.TAX["fields"][I.FIELD[key].vocab]
            out[key] = {"label": s["label"], "multi": s["multi"],
                        "values": {v: d for v, d in s["values"].items() if v not in ("Not specified", "Not assessed")}}
    return out


def site_config():
    cfg = I.load_json(I.DATA / "site_config.json", {}) or {}
    portal = I.load_json(I.DATA / "portal_config.json", {}) or {}
    known = lambda v: v if isinstance(v, str) and v.strip() and v.strip() != "Not set" else ""   # noqa: E731
    return {
        "title": known(cfg.get("title")) or "Interpretation Library",
        "tagline": known(cfg.get("tagline")),
        "organisation": known(cfg.get("organisation")),
        "takedown_notice": known(portal.get("takedown_notice")),
        "takedown_contact": known(portal.get("takedown_contact")),
        "takedown_api": bool(portal.get("takedown_api", False)),
    }


def build_site(db):
    tpl = I.SITE / "template.html"
    records, redirects = public_records(db)
    cfg = site_config()
    payload = {"config": cfg, "generated": I.today(), "taxonomy": site_taxonomy(), "facets": FACETS,
               "records": records, "redirects": redirects}
    blob = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
    page = tpl.read_text(encoding="utf-8")
    if "/*__LIBRARY_DATA__*/null" not in page:
        raise RuntimeError("site/template.html has no data placeholder")
    page = page.replace("/*__LIBRARY_DATA__*/null", blob).replace("__SITE_TITLE__", html.escape(cfg["title"]))
    out = I.SITE / "index.html"
    out.write_text(page, encoding="utf-8")
    return out, len(records)


# ---------------------------------------------------------------- exports --
def flat(r):
    row = {}
    for f in I.FIELDS:
        if f.name in ("provenance", "text_raw", "intro_raw"):
            continue
        v = r[f.name]
        if isinstance(v, dict) or (isinstance(v, list) and v and isinstance(v[0], (dict, list))):
            v = json.dumps(v, ensure_ascii=False)
        elif isinstance(v, list):
            v = "; ".join(str(x) for x in v)
        row[f.name] = v
    row["ai_generated_fields"] = "; ".join(sorted(k for k, p in r["provenance"].items() if p.get("origin") == "ai"))
    row["reviewer_entered_fields"] = "; ".join(sorted(k for k, p in r["provenance"].items() if p.get("origin") == "human"))
    row["hidden_from_site"] = "Yes" if is_hidden(r) else "No"
    return row


def export_csv(records, path):
    rows = [flat(r) for r in records]
    with open(path, "w", newline="", encoding="utf-8-sig") as f:        # BOM so Excel reads UTF-8
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()) if rows else ["id"])
        w.writeheader()
        w.writerows(rows)


def export_json(db, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump({"exported": I.today(), "schema_version": I.SCHEMA_VERSION, "records": db["records"]}, f, ensure_ascii=False, indent=1)


def export_sqlite(records, path):
    Path(path).unlink(missing_ok=True)
    con = sqlite3.connect(path)
    cols = [f.name for f in I.FIELDS if f.name != "provenance"]
    con.execute("CREATE TABLE cuttings (%s, PRIMARY KEY (id))" % ", ".join('"%s"' % c for c in cols))
    con.execute("CREATE TABLE provenance (record_id TEXT, field TEXT, origin TEXT, confidence TEXT, evidence TEXT)")
    for r in records:
        vals = [json.dumps(r[c], ensure_ascii=False) if isinstance(r[c], (list, dict)) else (int(r[c]) if isinstance(r[c], bool) else r[c]) for c in cols]
        con.execute("INSERT INTO cuttings VALUES (%s)" % ",".join("?" * len(cols)), vals)
        for k, p in r["provenance"].items():
            con.execute("INSERT INTO provenance VALUES (?,?,?,?,?)", (r["id"], k, p.get("origin"), p.get("confidence"), p.get("evidence")))
    fts = False
    try:
        con.execute("CREATE VIRTUAL TABLE cuttings_fts USING fts5(id UNINDEXED, title, author, work_title, themes, subject_matter, introduction_text, performance_text)")
        for r in records:
            con.execute("INSERT INTO cuttings_fts VALUES (?,?,?,?,?,?,?,?)", (r["id"], r["title"], r["author"], r["work_title"],
                        "; ".join(r["themes"]), r["subject_matter"], r["introduction_text"], r["performance_text"]))
        fts = True
    except sqlite3.OperationalError:
        pass                                                           # FTS5 not compiled into this Python
    con.commit()
    con.close()
    return fts


# ------------------------------------------------------------------- docs --
def taxonomy_md():
    t = I.TAX
    out = ["# Interpretation Library: Classification Taxonomy", "", "Version %s. Generated from `data/taxonomy.json`." % t["version"], "",
           "## Principles", ""] + ["- " + p for p in t["principles"]] + ["", "## Provenance", "",
           "| Origin | Meaning |", "|---|---|",
           "| source | Stated in the uploaded file. Never overwritten by AI. |",
           "| computed | Derived by a script (word counts, speaker labels, status). |",
           "| ai | Suggested by an AI model, with a confidence and one sentence of evidence. |",
           "| human | Entered or confirmed by a reviewer. Never overwritten. |", "", "## Fields", ""]
    for key, s in t["fields"].items():
        out += ["### %s (`%s`)" % (s["label"], key), "", "**Definition.** " + s["definition"], "",
                "**Multiple values.** " + ("Yes" if s["multi"] else "No"), "", "**Assign when.** " + s["assign_when"], "",
                "**Do not assign when.** " + (s["do_not_assign_when"] or "-"), ""]
        out += ["- Example: " + e for e in s["examples"]]
        out += ["", "| Value | Definition |", "|---|---|"] + ["| %s | %s |" % (v, d) for v, d in s["values"].items()] + [""]
    out += ["## Free-text fields", "", "| Field | Guidance |", "|---|---|"] + ["| `%s` | %s |" % kv for kv in t["free_text_fields"].items()]
    return "\n".join(out) + "\n"


def schema_md():
    out = ["# Interpretation Library: Record Schema", "", "Schema version %s. Generated from `pipeline/ilib.py`." % I.SCHEMA_VERSION, "",
           "Kinds: `str` short text, `text` long text, `enum` one taxonomy value, `multi` several, `list` free list, "
           "`dicts` list of objects, `obj` object, `int`, `bool`, `date`.", ""]
    groups = collections.OrderedDict()
    for f in I.FIELDS:
        groups.setdefault(f.group, []).append(f)
    for g, fs in groups.items():
        out += ["## " + g, "", "| Field | Kind | Editable | On the site | Description |", "|---|---|---|---|---|"]
        out += ["| `%s` | %s | %s | %s | %s%s |" % (f.name, f.kind, "yes" if f.editable else "no", "yes" if f.name in PUBLIC_FIELDS else "no",
                                                  f.desc, " Vocabulary: `%s`." % f.vocab if f.vocab else "") for f in fs] + [""]
    return "\n".join(out) + "\n"


def report_md(db):
    recs = db["records"]
    reg = I.load_json(I.DATA / "source_files.json", []) or []
    shown, _ = public_records(db)
    cnt = lambda key: collections.Counter(r[key] for r in recs)           # noqa: E731
    flags = collections.Counter(re.sub(r":.*", "", f) for r in recs for f in r["qc_flags"])
    out = ["# Interpretation Library: Source and Data-Quality Report", "", "Generated %s." % I.today(), "", "## Summary", "",
           "| Measure | Count |", "|---|---|",
           "| Files received | %d |" % len(reg),
           "| Byte-identical copies (recorded on the kept record, not parsed again) | %d |" % sum(1 for e in reg if e.get("identical_copy_of")),
           "| Records | %d |" % len(recs),
           "| Shown on the site | %d |" % len(shown),
           "| Hidden: archived | %d |" % sum(1 for r in recs if r["record_status"] != "Active"),
           "| Hidden: removal requested or removed | %d |" % sum(1 for r in recs if r["rights_status"] in HIDDEN_RIGHTS),
           "| Exact duplicates | %d |" % sum(1 for r in recs if r["duplicate_status"] == "Exact Duplicate"),
           "| Near duplicates | %d |" % sum(1 for r in recs if r["duplicate_status"] == "Near Duplicate"),
           "| AI-classified (at least one AI value) | %d |" % sum(1 for r in recs if any(p.get("origin") == "ai" for p in r["provenance"].values())),
           "| Verified by a reviewer | %d |" % sum(1 for r in recs if r["human_verified"]),
           "| Text repairs applied | %d |" % sum(1 for r in recs for n in r["ingest_notes"] if n.startswith("Text repair:")), "",
           "## Files", "", "| File | Layout | Pages | Record |", "|---|---|---|---|"]
    out += ["| %s | %s | %s | %s |" % (e["file"], e.get("layout", ""), e.get("pages") or "", e.get("record") or "copy of " + str(e.get("identical_copy_of"))) for e in reg]
    for key, label in (("review_status", "Data-quality status"), ("intro_boundary", "Introduction boundary"),
                       ("source_citation", "Source citation in the file"), ("rights_status", "Rights status")):
        out += ["", "## " + label, "", "| Value | Records |", "|---|---|"] + ["| %s | %d |" % kv for kv in cnt(key).most_common()]
    out += ["", "## Open issues", "", "| Issue | Records |", "|---|---|"] + ["| %s | %d |" % kv for kv in flags.most_common()]
    out += ["", "## Known limits", "",
            "- Nothing in this library states or estimates a run time, and nothing says a piece is legal or eligible for any league.",
            "- AI values are suggestions: each has a confidence and evidence in the record's classification details.",
            "- The library reproduces full cuttings of copyrighted works. A password limits access; it does not grant permission.", ""]
    return "\n".join(out)


def rebuild(db):
    I.EXPORTS.mkdir(exist_ok=True)
    export_json(db, I.EXPORTS / "Interp_Database.json")
    export_csv(db["records"], I.EXPORTS / "Interp_Database.csv")
    fts = export_sqlite(db["records"], I.EXPORTS / "Interp_Database.sqlite")
    (I.EXPORTS / "Interp_Taxonomy.md").write_text(taxonomy_md(), encoding="utf-8")
    (I.EXPORTS / "Interp_Schema.md").write_text(schema_md(), encoding="utf-8")
    (I.EXPORTS / "Interp_Source_Report.md").write_text(report_md(db), encoding="utf-8")
    site, n = build_site(db)
    return "Built %d record(s): %d shown on the site -> %s; exports in exports/%s" % (
        len(db["records"]), n, site.relative_to(I.ROOT), "" if fts else " (no full-text table: FTS5 missing)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="validate only")
    a = ap.parse_args()
    with I.DbLock():
        db = I.load_db()
        try:
            for note in RP.apply_all(db):
                print("repair applied:", note)
        except RP.RepairError as e:
            print("ERROR:", e)
            return 1
        for r in db["records"]:
            I.derive(r)
        errors, warnings = validate(db)
        for w in warnings:
            print("warning:", w)
        for e in errors:
            print("ERROR:", e)
        if errors:
            print("\n%d error(s); nothing saved or built." % len(errors))
            return 1
        I.save_db(db)
        if a.check:
            print("OK: %d record(s), %d warning(s)." % (len(db["records"]), len(warnings)))
            return 0
        print(rebuild(db))
    return 0


if __name__ == "__main__":
    sys.exit(main())
