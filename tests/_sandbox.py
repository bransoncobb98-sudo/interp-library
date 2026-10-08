"""Test helpers: every test works on a throwaway copy of the project, never on the real data."""
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FAILS = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("  " + str(detail)) if detail else ""))
    if not ok:
        FAILS.append(name)
    return ok


def finish():
    print("\n%d check(s) failed" % len(FAILS) if FAILS else "\nall checks passed")
    return 1 if FAILS else 0


def make(sources=(), first_upload_only=False):
    """first_upload_only: keep only the records (and register entries) of the files in sources/, so a test that
    runs the ingest many times does not compare against the whole library each time."""
    d = Path(tempfile.mkdtemp(prefix="ilib-test-"))
    skip = shutil.ignore_patterns("__pycache__", ".db.lock", "*.tmp", "classifications", "classification_requests", "index.html")
    for sub in ("pipeline", "data", "site"):
        shutil.copytree(ROOT / sub, d / sub, ignore=skip)
    (d / "sources").mkdir()
    for s in sources:
        shutil.copy2(ROOT / "sources" / s, d / "sources" / s)
    if first_upload_only:
        reg = [e for e in register(d) if not e.get("path")]          # entries with a path came from incoming/
        keep = {e.get("record") or e.get("identical_copy_of") for e in reg}
        with open(d / "data" / "source_files.json", "w", encoding="utf-8") as f:
            json.dump(reg, f, ensure_ascii=False, indent=1)
        sys.path.insert(0, str(d / "pipeline"))
        import ilib as I                                                  # noqa: E402  (the copy's own code)
        import ingest as G                                                # noqa: E402

        def trim(db):
            db["records"] = [r for r in db["records"] if r["id"] in keep]
            for r in db["records"]:                                       # links to records left out of the copy
                for k in ("duplicate_of", "same_source_work_ids"):
                    r[k] = [x for x in r[k] if x in keep]
            G.mark_duplicates(db["records"], reg)                         # duplicate links as an ingest would leave them
            for r in db["records"]:
                I.derive(r)
        edit_db(d, trim)
        sys.path.remove(str(d / "pipeline"))
        for m in ("ilib", "ingest", "layouts", "repairs"):
            sys.modules.pop(m, None)                                      # the test imports its own copy later if it needs one
        (d / "data" / "refused_files.json").unlink(missing_ok=True)
    return d


def edit_db(d, fn):
    p = Path(d) / "data" / "cuttings.json"
    with open(p, encoding="utf-8") as f:
        db = json.load(f)
    fn(db)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1)


def run(d, *args):
    env = dict(os.environ, ILIB_TODAY="2026-09-30", PYTHONDONTWRITEBYTECODE="1")
    return subprocess.run([sys.executable, *map(str, args)], cwd=d, capture_output=True, text=True, env=env)


def raw(d, rel="data/cuttings.json"):
    return (Path(d) / rel).read_bytes()


def records(d):
    with open(Path(d) / "data" / "cuttings.json", encoding="utf-8") as f:
        return {r["id"]: r for r in json.load(f)["records"]}


def register(d):
    with open(Path(d) / "data" / "source_files.json", encoding="utf-8") as f:
        return json.load(f)


def edit_records(d, fn):
    p = Path(d) / "data" / "cuttings.json"
    with open(p, encoding="utf-8") as f:
        db = json.load(f)
    fn({r["id"]: r for r in db["records"]})
    with open(p, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=1)


def cleanup(d):
    shutil.rmtree(d, ignore_errors=True)
