"""Shared library for the Interpretation Library.

The schema below is the single source of truth: validation, CSV columns, the
review form and Interp_Schema.md are all generated from it.  The design follows
the monologue library: every value has an origin (source / computed / ai / human),
AI never overwrites source or human values, unknown stays "Not specified", and
nothing is deleted.
"""
import datetime
import hashlib
import json
import os
import re
import tempfile
import threading
from pathlib import Path

try:                       # file locking is Linux/macOS only; Windows can read and build but not lock
    import fcntl
except ImportError:        # pragma: no cover
    fcntl = None

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SOURCES = ROOT / "sources"
EXPORTS = ROOT / "exports"
BACKUPS = ROOT / "backups"
SITE = ROOT / "site"
DB_PATH = DATA / "cuttings.json"
TAX_PATH = DATA / "taxonomy.json"
NS = "Not specified"
SCHEMA_VERSION = "1.0"
ORIGINS = ("source", "computed", "ai", "human")
CONFIDENCES = ("high", "medium", "low")


def today():
    return os.environ.get("ILIB_TODAY") or datetime.date.today().isoformat()


def load_json(path, default=None):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return default


TAX = load_json(TAX_PATH)
# Run-time estimates and league timing flags were removed at the director's request (2026-09-30).
# These computed fields may still exist in older databases and are dropped on load.
OBSOLETE_FIELDS = ("estimated_seconds_body", "estimated_seconds_with_intro", "estimated_range_with_intro", "timing_flags")


def vocab(key):
    return list(TAX["fields"][key]["values"].keys())


class F:
    def __init__(self, name, kind, group, desc, vocab=None, editable=True, default=None):
        self.name, self.kind, self.group, self.desc = name, kind, group, desc
        self.vocab, self.editable, self.default = vocab, editable, default


FIELDS = [
    F("id", "str", "Identity", "Unique record ID (IC-0001 style). Never reused.", editable=False),
    F("record_type", "enum", "Identity", "Cutting, Program or Unsegmented Text.", "record_type", default="Cutting"),
    F("record_status", "enum", "Identity", "Active records appear in the library; Archived are hidden but kept.", "record_status", default="Active"),
    F("title", "str", "Identity", "Title exactly as the file gives it.", default=NS),
    F("event", "enum", "Identity", "Event the cutting was prepared for, as filed by the uploader.", "event"),
    F("performer_category_as_filed", "str", "Identity", "Filing label from the upload folder (for example 'Any Gender'). Kept raw.", default=NS),
    # source work
    F("author", "str", "Source work", "Author as given in the byline.", default=NS),
    F("work_title", "str", "Source work", "Book or magazine the cutting comes from, as stated.", default=NS),
    F("publisher", "str", "Source work", "Publisher as stated.", default=NS),
    F("isbn", "str", "Source work", "ISBN or ISSN as stated.", default=NS),
    F("publication_date_raw", "str", "Source work", "Publication date exactly as stated (for example 'Sept 2007').", default=NS),
    F("source_url", "str", "Source work", "Web link given in the source block.", default=NS),
    F("literary_form", "enum", "Source work", "Form of the source work.", "literary_form", default=NS),
    F("source_block_raw", "text", "Source work", "The SOURCE INFORMATION block (or copyright page) exactly as extracted.", editable=False, default=""),
    F("source_notes", "list", "Source work", "Notes printed in the source block that are not fields.", editable=False, default=[]),
    F("source_work_key", "str", "Source work", "Key used to link cuttings of the same work (ISBN, else title and author).", editable=False, default=""),
    F("same_source_work_ids", "list", "Source work", "Other records cut from the same source work. Not duplicates.", editable=False, default=[]),
    # credits
    F("cutter", "str", "Cutting credits", "Who made the cutting, as credited (for example a coach and school).", default=NS),
    F("award_history_raw", "text", "Cutting credits", "Award lines exactly as printed. Not treated as facts about the piece.", editable=False, default=""),
    F("back_matter_raw", "text", "Cutting credits", "Back-matter text after the source block, exactly as extracted.", editable=False, default=""),
    # rights
    F("copyright_notice", "text", "Rights", "Copyright notice exactly as given in the file.", default=NS),
    F("rights_status", "enum", "Rights", "What is known about permission to host. Only a reviewer raises it above Not assessed.", "rights_status", default="Not assessed"),
    F("rights_note", "text", "Rights", "Reviewer note on the basis for the rights status.", default=""),
    F("takedown_log", "dicts", "Rights", "Removal requests received for this record.", editable=False, default=[]),
    F("attribution_note", "str", "Rights", "Standing attribution statement.", editable=False, default="Source and credit information preserved from the uploaded file."),
    # file
    F("source_file", "str", "File", "Original PDF filename.", editable=False),
    F("source_file_sha1", "str", "File", "SHA-1 of the file when ingested.", editable=False),
    F("source_pages", "int", "File", "Pages in the source PDF.", editable=False),
    F("source_layout", "str", "File", "Layout parser used.", editable=False),
    # text
    F("introduction_text", "text", "Text", "The performer's introduction, stored separately from the performance text.", default=""),
    F("performance_text", "text", "Text", "Teaser and cutting exactly as extracted, marks preserved. Authoritative.", default=""),
    F("text_raw", "text", "Text", "Performance lines as extracted, one per line, before joining. Kept for audit.", editable=False, default=""),
    F("intro_raw", "text", "Text", "Introduction lines as extracted. Kept for audit.", editable=False, default=""),
    F("text_layout", "str", "Text", "prose, verse or mixed.", editable=False, default="prose"),
    F("text_hash", "str", "Text", "SHA-1 of the normalised spoken words of the performance text.", editable=False),
    F("intro_boundary", "enum", "Text", "Confidence in the introduction/performance split.", "intro_boundary", editable=False),
    F("intro_boundary_method", "str", "Text", "How the split was found.", editable=False, default=""),
    F("teaser_present", "enum", "Text", "Performance text appears before the introduction heading.", "yes_no", editable=False),
    F("speaker_labels", "list", "Text", "Distinct uppercase speaker labels found in the text.", editable=False, default=[]),
    F("character_count", "int", "Text", "Number of distinct speaker labels; empty if the text has no labels.", editable=False),
    F("word_count", "int", "Text", "Spoken words in the performance text (see count rules).", editable=False),
    F("intro_word_count", "int", "Text", "Words in the introduction.", editable=False),
    # checks
    F("source_citation", "enum", "Source checks", "How completely the file cites its published source.", "source_citation", editable=False),
    F("web_only_source", "enum", "Source checks", "Only a web link is given as the source.", "yes_no", editable=False),
    # classification
    F("tone", "multi", "Classification", "Overall tone.", "tone"),
    F("content_warnings", "multi", "Classification", "Sensitive content present in the text.", "content_warnings"),
    F("difficulty", "enum", "Classification", "Difficulty.", "difficulty"),
    F("performance_demands", "multi", "Classification", "Skills the text clearly requires.", "performance_demands"),
    F("audience_level", "enum", "Classification", "Suggested audience level (AI-suggested).", "audience_level", default="Not assessed"),
    F("themes", "list", "Classification", "Themes the text supports.", default=[]),
    F("subject_matter", "text", "Classification", "One sentence describing what happens.", default=""),
    # quality
    F("metadata_confidence", "enum", "Quality", "Overall confidence in AI fields (computed).", "metadata_confidence", editable=False),
    F("review_status", "enum", "Quality", "Data-quality status (computed).", "review_status", editable=False),
    F("duplicate_status", "enum", "Quality", "Duplicate status.", "duplicate_status", default="Unique"),
    F("duplicate_of", "list", "Quality", "IDs of records this one duplicates.", default=[]),
    F("also_appears_in", "list", "Quality", "Files whose text is identical to this record.", editable=False, default=[]),
    F("ingest_notes", "list", "Quality", "Notes written by the pipeline.", editable=False, default=[]),
    F("qc_flags", "list", "Quality", "Open issues computed on every build.", editable=False, default=[]),
    F("human_verified", "bool", "Quality", "True once a reviewer has verified the record.", editable=False, default=False),
    F("date_added", "date", "Quality", "Date created.", editable=False),
    F("date_updated", "date", "Quality", "Date of last change.", editable=False),
    F("date_verified", "date", "Quality", "Date verified.", editable=False, default=""),
    F("provenance", "obj", "Quality", "Per-field origin, confidence and evidence.", editable=False, default={}),
]
FIELD = {f.name: f for f in FIELDS}
CLASSIFIABLE = ["literary_form", "tone", "content_warnings", "difficulty", "performance_demands",
                "audience_level", "themes", "subject_matter"]
REQUIRED_KNOWN = ("title", "author")


def blank_default(f):
    if f.default is not None:
        return json.loads(json.dumps(f.default))
    return {"list": [], "dicts": [], "multi": [], "obj": {}, "bool": False, "int": None}.get(f.kind, "")


def new_record():
    return {f.name: blank_default(f) for f in FIELDS}


# ---------------------------------------------------------- persistence --
def load_db():
    if not DB_PATH.exists():
        return {"schema_version": SCHEMA_VERSION, "records": []}
    with open(DB_PATH, encoding="utf-8") as f:
        db = json.load(f)
    for r in db["records"]:
        for f in FIELDS:
            if f.name not in r:
                r[f.name] = blank_default(f)
        for k in OBSOLETE_FIELDS:
            r.pop(k, None)
            r["provenance"].pop(k, None)
    return db


def save_db(db):
    db["schema_version"] = SCHEMA_VERSION
    db["records"].sort(key=lambda r: r["id"])
    DATA.mkdir(exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=DATA, suffix=".tmp")
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1)
        f.write("\n")
    os.replace(tmp, DB_PATH)


def next_id(db):
    nums = [int(r["id"].split("-")[1]) for r in db["records"] if re.fullmatch(r"IC-\d+", r["id"])]
    return "IC-%04d" % (max(nums, default=0) + 1)


def sha1_file(path):
    h = hashlib.sha1()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ------------------------------------------------------------ provenance --
def set_prov(rec, field, origin, confidence=None, evidence=None):
    assert origin in ORIGINS, origin
    p = {"origin": origin}
    if confidence:
        p["confidence"] = confidence
    if evidence:
        p["evidence"] = evidence
    rec["provenance"][field] = p


def prov_origin(rec, field):
    return rec["provenance"].get(field, {}).get("origin")


# ----------------------------------------------------------- word counts --
WORD_RE = re.compile(r"[\w][\w'’]*", re.UNICODE)
PAREN_RE = re.compile(r"\([^()]{0,400}\)")                      # directions and (Pg N) page references
LABEL_LINE_RE = re.compile(r"(?m)^[ \t]*[A-Z][A-Z0-9 .'’/#&-]{0,28}:(?=\s|$)")
NOTE_LINE_RE = re.compile(r"(?m)^[ \t]*NOTE:.*$")
PG_RE = re.compile(r"\(Pg\.?\s*[\d\s,–-]+\)")


def spoken_text(text):
    """Counting rules approved for this library:
    ignored: (parenthetical directions), (Pg N) source-page references, uppercase speaker
    labels at the start of a line, and lines starting 'NOTE:' (performer notes).
    counted: everything else, INCLUDING [bracketed] text, because in these files brackets
    often hold spoken words.  The text itself is never altered."""
    t = NOTE_LINE_RE.sub(" ", text)
    t = LABEL_LINE_RE.sub(" ", t)
    t = PAREN_RE.sub(" ", t)
    return t


def count_words(text):
    return len(WORD_RE.findall(spoken_text(text)))


def norm_for_hash(text):
    t = spoken_text(text).lower().replace("’", "'")
    return " ".join(WORD_RE.findall(t))


def text_hash(text):
    return hashlib.sha1(norm_for_hash(text).encode("utf-8")).hexdigest()


def speaker_labels(text):
    seen = []
    for m in LABEL_LINE_RE.finditer(text):
        lab = m.group(0).strip().rstrip(":").strip()
        if lab in ("NOTE", "TRANSITION", "INTRODUCTION"):
            continue
        if lab not in seen:
            seen.append(lab)
    return seen


# ------------------------------------------------------------- derivation --
CONF_SCORE = {"high": 1.0, "medium": 0.6, "low": 0.3}


def derive(rec):
    """Recompute every computed field.  Safe to call repeatedly."""
    perf, intro = rec["performance_text"], rec["introduction_text"]
    rec["word_count"] = count_words(perf)
    rec["intro_word_count"] = len(WORD_RE.findall(intro))
    rec["text_hash"] = text_hash(perf)
    labels = speaker_labels(perf)
    rec["speaker_labels"] = labels
    rec["character_count"] = len(labels) if labels else None
    paras = [p for p in perf.split("\n\n") if p.strip()]
    verse = sum(1 for p in paras if "\n" in p)
    rec["text_layout"] = "prose" if not verse else ("verse" if verse / max(1, len(paras)) >= 0.4 else "mixed")
    for k in ("word_count", "intro_word_count", "text_hash", "speaker_labels", "character_count", "text_layout"):
        set_prov(rec, k, "computed")

    scores = [CONF_SCORE[p["confidence"]] for p in rec["provenance"].values()
              if p.get("origin") == "ai" and p.get("confidence") in CONF_SCORE]
    rec["metadata_confidence"] = "Low" if not scores else (
        "High" if sum(scores) / len(scores) >= 0.8 else "Medium" if sum(scores) / len(scores) >= 0.55 else "Low")

    flags = []
    for k in REQUIRED_KNOWN:
        if not rec.get(k) or rec[k] == NS:
            flags.append("missing_" + k)
    if rec["work_title"] == NS:
        # the file did not name a separate book or magazine; identified by ISBN/publisher if given
        flags.append("missing_work_title" if rec["isbn"] == NS and rec["publisher"] == NS else "no_work_title_stated")
    if not any(prov_origin(rec, k) in ("ai", "human") for k in ("tone", "content_warnings", "difficulty", "literary_form")):
        flags.append("unclassified")
    low = sorted(k for k, p in rec["provenance"].items() if p.get("origin") == "ai" and p.get("confidence") == "low")
    if low:
        flags.append("low_confidence_fields: " + ", ".join(low))
    if rec["duplicate_status"] in ("Exact Duplicate", "Near Duplicate") and rec["record_status"] == "Active":
        flags.append("possible_duplicate")
    if rec["intro_boundary"] == "Medium":
        flags.append("intro_boundary_hand_check")
    if rec["rights_status"] == "Removal requested":
        flags.append("removal_requested")
    if not perf.strip():
        flags.append("empty_text")
    rec["qc_flags"] = flags
    if rec["human_verified"]:
        status = "Verified"
    elif "possible_duplicate" in flags:
        status = "Possible Duplicate"
    elif any(f.startswith("missing_") for f in flags):
        status = "Missing Metadata"
    elif flags or rec["ingest_notes"] or rec["metadata_confidence"] != "High":
        status = "Needs Review"
    else:
        status = "High Confidence"
    rec["review_status"] = status
    return rec


def validate_record(rec):
    problems = []
    for f in FIELDS:
        if f.name not in rec:
            problems.append("%s: missing field" % f.name)
            continue
        v = rec[f.name]
        if f.kind == "enum" and v not in ("", None) and v not in vocab(f.vocab):
            problems.append("%s: '%s' is not in the taxonomy" % (f.name, v))
        elif f.kind == "multi":
            if not isinstance(v, list):
                problems.append("%s: must be a list" % f.name)
            else:
                problems += ["%s: '%s' is not in the taxonomy" % (f.name, i) for i in v if i not in vocab(f.vocab)]
        elif f.kind in ("list", "dicts") and not isinstance(v, list):
            problems.append("%s: must be a list" % f.name)
    if not re.fullmatch(r"IC-\d{4,}", rec.get("id", "")):
        problems.append("id: malformed")
    for k, p in rec.get("provenance", {}).items():
        if p.get("origin") not in ORIGINS:
            problems.append("provenance.%s: bad origin" % k)
        if p.get("origin") == "ai" and (p.get("confidence") not in CONFIDENCES or not p.get("evidence")):
            problems.append("provenance.%s: AI value without confidence or evidence" % k)
    if rec.get("word_count") is not None and rec["word_count"] != count_words(rec["performance_text"]):
        problems.append("word_count: out of date; run build")
    return problems


# --------------------------------------------------------------- locking --
_THREAD_LOCK = threading.Lock()


class DbLock:
    """Thread lock plus file lock so the portal, review tool and command-line tools never write together."""
    def __enter__(self):
        if fcntl is None:
            raise RuntimeError("Database locking needs Linux or macOS (the fcntl module). "
                               "Run this command in the Codespace or the Docker container, not on Windows.")
        _THREAD_LOCK.acquire()
        DATA.mkdir(exist_ok=True)
        self.f = open(DATA / ".db.lock", "w")
        fcntl.flock(self.f, fcntl.LOCK_EX)

    def __exit__(self, *a):
        fcntl.flock(self.f, fcntl.LOCK_UN)
        self.f.close()
        _THREAD_LOCK.release()
