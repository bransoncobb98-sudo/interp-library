#!/usr/bin/env python3
"""Classification hand-off: request batches, validation of replies, protection of source/human values.
Run:  python tests/test_classify.py      (standard library only; works on a copy of the project)"""
import json
import math
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _sandbox import check, finish, make, run, raw, records, edit_records, cleanup  # noqa: E402

KEY = ("tone", "content_warnings", "difficulty", "literary_form")
d = make()
try:
    p = run(d, "pipeline/build.py")
    check("sandbox copy builds", p.returncode == 0, p.stdout[-300:] + p.stderr[-300:])
    recs = records(d)
    tax = json.loads((d / "data" / "taxonomy.json").read_text(encoding="utf-8"))
    waiting = sorted(i for i, r in recs.items() if r["record_status"] == "Active"
                     and r["rights_status"] not in ("Removal requested", "Removed")
                     and not any(r["provenance"].get(k, {}).get("origin") in ("ai", "human") for k in KEY))

    # ---- queue
    p = run(d, "pipeline/classify.py", "--queue")
    files = sorted((d / "data" / "classification_requests").glob("batch-*.md"))
    check("--queue writes ceil(waiting / 40) batch files", len(files) == math.ceil(len(waiting) / 40), "%d files for %d records" % (len(files), len(waiting)))
    seen = []
    for f in files:
        t = f.read_text(encoding="utf-8")
        ids = re.findall(r"(?m)^## (IC-\d{4,}): ", t)
        seen += ids
        check("%s holds at most 40 records" % f.name, 0 < len(ids) <= 40, len(ids))
        for field in ("literary_form", "tone", "content_warnings", "difficulty", "performance_demands", "audience_level"):
            spec = tax["fields"][field]
            check("%s gives the full rules for %s" % (f.name, field),
                  spec["definition"] in t and spec["assign_when"] in t and spec["do_not_assign_when"] in t
                  and all('"%s"' % v in t for v in spec["values"] if v not in ("Not specified", "Not assessed")))
        check("%s marks the introduction as context only and says where warnings come from" % f.name,
              "Introduction (context only: never use it for content warnings)" in t and "must come from the performance text alone" in t)
    check("every waiting record is queued exactly once", sorted(seen) == waiting, "%d queued, %d waiting" % (len(seen), len(waiting)))
    r14 = recs["IC-0014"]
    t_all = "".join(f.read_text(encoding="utf-8") for f in files)
    check("a record's performance text appears in its batch unaltered", r14["performance_text"] in t_all)

    # ---- the worked example, dry run then real
    ex = "data/classification_examples/EXAMPLE-IC-0014.json"
    snap = raw(d)
    p = run(d, "pipeline/classify.py", "--apply", ex, "--dry-run")
    check("--dry-run applies nothing", raw(d) == snap and "applied: 8" in p.stdout, p.stdout.strip()[:300] + p.stderr[-300:])
    p = run(d, "pipeline/classify.py", "--apply", ex)
    after = records(d)["IC-0014"]
    exj = json.loads((d / ex).read_text(encoding="utf-8"))["IC-0014"]
    ok = all(after[k] == (sorted(v["value"], key=list(tax["fields"][k]["values"]).index) if k in ("tone", "content_warnings", "performance_demands") else v["value"])
             and after["provenance"][k] == {"origin": "ai", "confidence": v["confidence"], "evidence": v["evidence"]} for k, v in exj.items())
    check("the example applies all 8 values with origin ai, confidence and evidence", ok and "applied: 8" in p.stdout, p.stdout.strip()[:300])
    check("... source values are untouched", after["author"] == r14["author"] and after["provenance"]["author"]["origin"] == "source")
    arch = sorted(x.name for x in (d / "data" / "classifications").glob("*"))
    check("... the reply and a report are archived in data/classifications/",
          any(n.endswith("EXAMPLE-IC-0014.json") for n in arch) and any(n.endswith("EXAMPLE-IC-0014.report.json") for n in arch), arch)
    check("... record no longer queued", "IC-0014" not in re.findall(r"(?m)^## (IC-\d+): ",
          "".join(f.read_text(encoding="utf-8") for f in (run(d, "pipeline/classify.py", "--queue") and sorted((d / "data" / "classification_requests").glob("batch-*.md"))))))

    # ---- a bad reply
    def human_tone(rs):
        rs["IC-0003"]["tone"] = ["Earnest"]
        rs["IC-0003"]["provenance"]["tone"] = {"origin": "human", "evidence": "test reviewer"}
    edit_records(d, human_tone)
    r2 = records(d)["IC-0002"]
    words = r2["introduction_text"].split()
    intro_quote = next(" ".join(words[i:i + 6]) for i in range(len(words) - 6)
                       if " ".join(words[i:i + 6]) not in r2["performance_text"] and '"' not in " ".join(words[i:i + 6]))
    ev = lambda s: {"confidence": "high", "evidence": s}                                                     # noqa: E731
    bad = {
        "IC-0001": {"tone": dict(ev("x"), value=["Gloomy"]),
                    "difficulty": {"value": "Advanced", "confidence": "sure", "evidence": "x"},
                    "subject_matter": {"value": "Something happens.", "confidence": "high"},
                    "author": dict(ev("x"), value="Someone Else"),
                    "audience_level": dict(ev("x"), value="High School"),
                    "literary_form": dict(ev("x"), value="Not specified")},
        "IC-0002": {"content_warnings": dict(ev('The introduction says "%s".' % intro_quote), value=["Death"])},
        "IC-0003": {"tone": dict(ev("x"), value=["Dark"])},
        "IC-9999": {"tone": dict(ev("x"), value=["Dark"])},
    }
    (d / "bad.json").write_text(json.dumps(bad), encoding="utf-8")
    before = records(d)
    p = run(d, "pipeline/classify.py", "--apply", "bad.json")
    rep = json.loads(sorted((d / "data" / "classifications").glob("*-bad.report.json"))[-1].read_text(encoding="utf-8"))
    rej = " | ".join(rep["rejected"])
    check("an invalid taxonomy value is rejected", "IC-0001.tone" in rej and "Gloomy" in rej, rej)
    check("a bad confidence is rejected", "IC-0001.difficulty" in rej)
    check("a missing evidence is rejected", "IC-0001.subject_matter" in rej)
    check("a non-classifiable field is rejected", "IC-0001.author" in rej)
    check("audience_level without content warnings is rejected", "IC-0001.audience_level" in rej)
    check("a placeholder value is rejected", "IC-0001.literary_form" in rej)
    check("content warnings quoting only the introduction are rejected", "IC-0002.content_warnings" in rej and "introduction" in rej)
    check("a reviewer value is skipped, not overwritten", rep["skipped_protected"] == ["IC-0003.tone"], rep["skipped_protected"])
    check("an unknown ID is reported", rep["unknown_ids"] == ["IC-9999"])
    check("nothing was applied", rep["applied"] == [], rep["applied"])
    now = records(d)
    check("... and the records are unchanged", all(now[i] == before[i] for i in ("IC-0001", "IC-0002", "IC-0003")))
    check("the rejections are listed on screen", p.stdout.count("REJECTED") == len(rep["rejected"]), p.stdout[:500])

    p = run(d, "pipeline/build.py")
    check("the database still builds after classification", p.returncode == 0, p.stdout[-300:] + p.stderr[-300:])
finally:
    cleanup(d)
sys.exit(finish())
