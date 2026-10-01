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


def make(sources=()):
    d = Path(tempfile.mkdtemp(prefix="ilib-test-"))
    skip = shutil.ignore_patterns("__pycache__", ".db.lock", "*.tmp", "classifications", "classification_requests", "index.html")
    for sub in ("pipeline", "data", "site"):
        shutil.copytree(ROOT / sub, d / sub, ignore=skip)
    (d / "sources").mkdir()
    for s in sources:
        shutil.copy2(ROOT / "sources" / s, d / "sources" / s)
    return d


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
