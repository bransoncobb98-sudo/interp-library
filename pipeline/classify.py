#!/usr/bin/env python3
"""AI classification hand-off.  The pipeline never calls an AI model itself.

  1. python pipeline/classify.py --queue
        Writes data/classification_requests/batch-001.md, batch-002.md, ... (up to 40 records each):
        instructions, the full taxonomy with assign-when / do-not-assign-when rules, and for each
        record its source facts, introduction and performance text.
  2. Paste one batch into an AI model.  Save its JSON reply to a file.
  3. python pipeline/classify.py --apply reply.json      (add --dry-run to check without writing)
        Every value is checked against the taxonomy.  Invalid values are rejected and listed.
        Each AI value needs a confidence and one sentence of evidence.  Values whose origin is
        'source' or 'human' are never overwritten.  Content warnings must quote the performance
        text, not the introduction or the source block.  The reply and a report are archived in
        data/classifications/.

A worked example reply is in data/classification_examples/.
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I  # noqa: E402

REQ_DIR = I.DATA / "classification_requests"
CLASS_DIR = I.DATA / "classifications"
BATCH = 40
KEY_FIELDS = ("tone", "content_warnings", "difficulty", "literary_form")      # same test as derive()'s 'unclassified'
PLACEHOLDERS = (I.NS, "Not assessed")
MAX_EVIDENCE, MAX_THEME, MAX_THEMES, MAX_SUBJECT = 400, 60, 8, 300


def needs_classification(r):
    return (r["record_status"] == "Active" and r["rights_status"] not in ("Removal requested", "Removed")
            and not any(I.prov_origin(r, k) in ("ai", "human") for k in KEY_FIELDS))


# ------------------------------------------------------------------ queue --
def taxonomy_lines():
    out = []
    for name in I.CLASSIFIABLE:
        f = I.FIELD[name]
        if f.vocab:
            spec = I.TAX["fields"][f.vocab]
            kind = "a LIST of values (an empty list means none present)" if f.kind == "multi" else "ONE value (a string)"
            out += ["### %s  (`%s`, %s)" % (spec["label"], name, kind), "",
                    "- Definition: " + spec["definition"],
                    "- Assign when: " + spec["assign_when"],
                    "- Do not assign when: " + (spec["do_not_assign_when"] or "(no rule)")]
            out += ["- Example: " + e for e in spec.get("examples", [])]
            out.append("- Allowed values:")
            out += ['  - "%s": %s' % (v, d) for v, d in spec["values"].items() if v not in PLACEHOLDERS]
        elif f.kind == "list":
            out += ["### Themes  (`%s`, a list of short phrases, at most %d, each under %d characters)" % (name, MAX_THEMES, MAX_THEME),
                    "", "- " + I.TAX["free_text_fields"].get(name, f.desc)]
        else:
            out += ["### Subject matter  (`%s`, one sentence under %d characters)" % (name, MAX_SUBJECT),
                    "", "- " + I.TAX["free_text_fields"].get(name, f.desc)]
        out.append("")
    return out


def header(n_batch, i, chunk):
    lines = ["# Classification request: batch %d of %d (%d records, %s to %s)" % (i, n_batch, len(chunk), chunk[0]["id"], chunk[-1]["id"]), "",
             "You are an experienced high school speech and debate coach classifying interpretation cuttings",
             "for a searchable library used by students and coaches.", "",
             "## Reply format", "",
             "Return ONE JSON object and nothing else. Keys are record IDs. Each value maps field names to",
             '`{"value": ..., "confidence": "high" | "medium" | "low", "evidence": "one sentence pointing at the text"}`.',
             "Save the reply as `batch-%03d-reply.json`." % i, "",
             "## Rules", ""]
    lines += ["- " + p for p in I.TAX["principles"]]
    lines += [
        "- Classify the PERFORMANCE TEXT. The introduction and the source block are context only.",
        "- `content_warnings` must come from the performance text alone. Its evidence must quote the performance text in",
        '  double quotes, for example: "he hung himself right there" describes a suicide. A quote taken from the',
        "  introduction or the source block is rejected. If you find no sensitive content, give an empty list with evidence.",
        "- `audience_level` is a suggestion, never a claim that a piece is appropriate. Give it only together with",
        "  `content_warnings` for the same record.",
        "- Omit a field when the text does not support a value. Never write 'Not specified' or 'Not assessed'; omit instead.",
        "- Use only the allowed values below, spelled exactly. Single-value fields take a string; list fields take a list.",
        "- `evidence` is one specific sentence: quote a few words in double quotes or name the passage. Never invent facts",
        "  about the work, the author, a production or a league.",
        "- Do not supply title, author, work, publisher, event, rights, word counts or any field not listed below.",
        "- Fields a record lists as 'already set' were stated by the source or entered by a reviewer. Do not supply them.",
        "- Performance marks such as (Pg 4), (Pause) or [bracketed words] are part of the text. Do not treat them as content.",
        "", "## Fields to supply", ""]
    lines += taxonomy_lines()
    return lines


def record_block(r):
    kept = ["%s = %s" % (k, ", ".join(r[k]) if isinstance(r[k], list) else r[k]) for k in I.CLASSIFIABLE
            if I.prov_origin(r, k) in ("source", "human")]
    facts = [("Title", r["title"]), ("Author (byline)", r["author"]), ("Work", r["work_title"]),
             ("Publisher", r["publisher"]), ("Publication date as stated", r["publication_date_raw"]),
             ("Event as filed", r["event"]), ("Record type", r["record_type"]),
             ("Speaker labels in the text", ", ".join(r["speaker_labels"]) or "none"),
             ("Teaser before the introduction", r["teaser_present"]),
             ("Spoken words (computed)", r["word_count"])]
    lines = ["---", "", "## %s: %s" % (r["id"], r["title"]), ""]
    lines += ["- %s: %s" % kv for kv in facts]
    lines += ["- Already set (do not supply): " + ("; ".join(kept) or "none"), "",
              "### Source block (context only)", "", "```text", r["source_block_raw"].strip() or "(none)", "```", "",
              "### Introduction (context only: never use it for content warnings)", "", "```text",
              r["introduction_text"].strip() or "(no introduction)", "```", "",
              "### Performance text (classify this)", "", "```text", r["performance_text"], "```", ""]
    return lines


def write_requests(db, only_ids=None, batch_size=BATCH):
    batch_size = max(1, min(batch_size, BATCH))
    recs = [r for r in db["records"] if (r["id"] in only_ids if only_ids else needs_classification(r))]
    REQ_DIR.mkdir(parents=True, exist_ok=True)
    for old in REQ_DIR.glob("batch-*.md"):                    # generated files; rebuilt from the database each time
        old.unlink()
    chunks = [recs[i:i + batch_size] for i in range(0, len(recs), batch_size)]
    paths = []
    for i, chunk in enumerate(chunks, 1):
        body = header(len(chunks), i, chunk)
        body += ["## Records", ""]
        for r in chunk:
            body += record_block(r)
        p = REQ_DIR / ("batch-%03d.md" % i)
        p.write_text("\n".join(body), encoding="utf-8")
        paths.append(p)
    return paths, len(recs)


# ------------------------------------------------------------------ apply --
def norm(s):
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"').replace("…", "...")
    return re.sub(r"\s+", " ", s).strip().lower()


def quotes(evidence):
    return [q for q in re.findall(r'"([^"]{3,300})"', norm(evidence)) if len(q.split()) >= 2]


def check_value(name, value):
    """Return (ok, cleaned value or reason)."""
    f = I.FIELD[name]
    if f.kind == "enum":
        if not isinstance(value, str) or value not in I.vocab(f.vocab):
            return False, "'%s' is not an allowed value" % value
        if value in PLACEHOLDERS:
            return False, "'%s' is a placeholder; omit the field instead" % value
        return True, value
    if f.kind == "multi":
        if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
            return False, "expected a list of values"
        bad = [v for v in value if v not in I.vocab(f.vocab)]
        if bad:
            return False, "not allowed values: %s" % bad
        return True, sorted(set(value), key=I.vocab(f.vocab).index)
    if f.kind == "list":
        if not isinstance(value, list) or not all(isinstance(v, str) and v.strip() for v in value):
            return False, "expected a list of short phrases"
        value = [re.sub(r"\s+", " ", v).strip() for v in value]
        if len(value) > MAX_THEMES or any(len(v) > MAX_THEME for v in value):
            return False, "at most %d themes of under %d characters each" % (MAX_THEMES, MAX_THEME)
        return True, value
    if not isinstance(value, str) or not value.strip():
        return False, "expected one sentence of text"
    if len(value) > MAX_SUBJECT:
        return False, "longer than %d characters" % MAX_SUBJECT
    return True, re.sub(r"\s+", " ", value).strip()


def warnings_evidence_ok(rec, value, evidence):
    """Content warnings come from the performance text only."""
    qs = quotes(evidence)
    perf = norm(rec["performance_text"])
    context = norm(rec["introduction_text"] + " " + rec["source_block_raw"])
    outside = [q for q in qs if q not in perf and q in context]
    if outside:
        return False, "evidence quotes the introduction or source block, not the performance text: \"%s\"" % outside[0]
    if value and not any(q in perf for q in qs):
        return False, "evidence must quote the performance text in double quotes (no quote found in the performance text)"
    return True, ""


def apply_reply(db, data):
    """Apply one reply to db (in memory).  Returns a report dict."""
    rep = {"applied": [], "skipped_protected": [], "rejected": [], "unknown_ids": []}
    if not isinstance(data, dict):
        rep["rejected"].append("reply: expected one JSON object keyed by record ID")
        return rep
    by_id = {r["id"]: r for r in db["records"]}
    for rid, fields in data.items():
        rec = by_id.get(rid)
        if rec is None:
            rep["unknown_ids"].append(rid)
            continue
        if not isinstance(fields, dict):
            rep["rejected"].append("%s: expected an object of fields" % rid)
            continue
        accepted = {}
        # content_warnings first, so audience_level can check it
        for name in sorted(fields, key=lambda n: (n != "content_warnings", n)):
            item, where = fields[name], "%s.%s" % (rid, name)
            if name not in I.CLASSIFIABLE:
                rep["rejected"].append(where + ": not a field the AI may supply")
                continue
            if I.prov_origin(rec, name) in ("source", "human"):
                rep["skipped_protected"].append(where)
                continue
            if not isinstance(item, dict) or "value" not in item:
                rep["rejected"].append(where + ': expected {"value", "confidence", "evidence"}')
                continue
            conf, ev = item.get("confidence"), item.get("evidence")
            if conf not in I.CONFIDENCES:
                rep["rejected"].append(where + ": confidence must be high, medium or low")
                continue
            if not isinstance(ev, str) or not ev.strip():
                rep["rejected"].append(where + ": evidence is required")
                continue
            if len(ev) > MAX_EVIDENCE:
                rep["rejected"].append(where + ": evidence longer than %d characters" % MAX_EVIDENCE)
                continue
            ok, res = check_value(name, item["value"])
            if not ok:
                rep["rejected"].append("%s: %s" % (where, res))
                continue
            if name == "content_warnings":
                ok, why = warnings_evidence_ok(rec, res, ev)
                if not ok:
                    rep["rejected"].append("%s: %s" % (where, why))
                    continue
            if name == "audience_level" and "content_warnings" not in accepted and \
                    I.prov_origin(rec, "content_warnings") not in ("ai", "human"):
                rep["rejected"].append(where + ": needs content_warnings assessed for the same record")
                continue
            accepted[name] = (res, conf, ev.strip())
        for name, (res, conf, ev) in accepted.items():
            rec[name] = res
            I.set_prov(rec, name, "ai", conf, ev)
            rep["applied"].append("%s.%s" % (rid, name))
        if accepted:
            rec["date_updated"] = I.today()
            I.derive(rec)
    return rep


def archive(src, data, rep):
    CLASS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    stem = re.sub(r"[^A-Za-z0-9_.-]+", "_", Path(src).stem)[:60] or "reply"
    reply = CLASS_DIR / ("%s-%s.json" % (stamp, stem))
    reply.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (CLASS_DIR / ("%s-%s.report.json" % (stamp, stem))).write_text(
        json.dumps(dict(rep, source=str(src), applied_on=I.today()), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return reply


def print_report(rep):
    print("applied: %d | protected (skipped): %d | rejected: %d | unknown IDs: %d" % (
        len(rep["applied"]), len(rep["skipped_protected"]), len(rep["rejected"]), len(rep["unknown_ids"])))
    for x in rep["rejected"]:
        print("  REJECTED", x)
    for x in rep["skipped_protected"]:
        print("  protected (source or reviewer value kept)", x)
    for x in rep["unknown_ids"]:
        print("  unknown record ID", x)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--queue", action="store_true", help="write request batches for unclassified records")
    ap.add_argument("--ids", nargs="*", help="with --queue: these record IDs only (for re-classification)")
    ap.add_argument("--batch-size", type=int, default=BATCH, help="records per batch (at most %d)" % BATCH)
    ap.add_argument("--apply", metavar="FILE", help="apply one JSON reply")
    ap.add_argument("--dry-run", action="store_true", help="with --apply: check the reply, write nothing")
    a = ap.parse_args()
    if a.queue:
        with I.DbLock():
            db = I.load_db()
        paths, n = write_requests(db, set(a.ids) if a.ids else None, a.batch_size)
        print("%d record(s) queued in %d batch file(s): %s" % (n, len(paths), ", ".join(p.name for p in paths) or "none"))
        return 0
    if a.apply:
        try:
            data = json.loads(Path(a.apply).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print("Could not read the reply: %s" % e)
            return 1
        with I.DbLock():
            db = I.load_db()
            rep = apply_reply(db, data)
            bad = [p for r in db["records"] for p in I.validate_record(r)]
            if bad:
                print("Validation failed after applying; nothing written:", bad[:5])
                return 1
            if not a.dry_run:
                I.save_db(db)
                kept = archive(a.apply, data, rep)
        print_report(rep)
        print("dry run: nothing written" if a.dry_run else "saved; reply archived as %s" % kept.relative_to(I.ROOT))
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
