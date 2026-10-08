#!/usr/bin/env python3
"""The published (encrypted, split) site: nothing readable is written, every record comes back exactly, a wrong
password is refused, and the page is the same app as site/index.html with the unlock step in front.
Run:  python tests/test_publish.py      (needs the 'cryptography' package)"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _sandbox import ROOT, check, finish, make, run, cleanup  # noqa: E402

try:
    import cryptography  # noqa: F401
except ImportError:
    check("the 'cryptography' package is installed (pip install --user 'cryptography>=42')", False)
    sys.exit(finish())

PW = "test-password-not-the-real-one"
d = make(first_upload_only=True)
out = Path(tempfile.mkdtemp(prefix="ilib-pub-"))
try:
    p = run(d, "pipeline/build.py")
    check("sandbox copy builds", p.returncode == 0, p.stdout[-300:] + p.stderr[-300:])
    (out / "data").mkdir()
    (out / "data" / "part-99.bin").write_bytes(b"old")                  # a file from an older publish
    (out / "keep.txt").write_text("not ours")
    env_pw = dict(os.environ, ILIB_PASSWORD=PW)
    p = __import__("subprocess").run([sys.executable, "pipeline/publish.py", "--out", str(out)], cwd=d, capture_output=True, text=True, env=env_pw)
    check("publish succeeds and checks its own output", p.returncode == 0 and "decrypts back exactly" in p.stdout, p.stdout[-500:] + p.stderr[-800:])
    names = sorted(x.name for x in (out / "data").iterdir())
    check("catalogue and text parts written; the old part is gone", "catalog.bin" in names and "part-00.bin" in names and "part-99.bin" not in names, names)
    check("files that are not the publisher's are left alone", (out / "keep.txt").exists())
    check("robots.txt keeps search engines out", "Disallow: /" in (out / "robots.txt").read_text())

    # nothing readable: no record title, introduction or text passage in any published file
    sys.path.insert(0, str(d / "pipeline"))
    import ilib as I        # noqa: E402
    import build as B       # noqa: E402
    import publish as PUB   # noqa: E402
    payload = B.site_payload(I.load_db())                                  # ilib finds the sandbox from its own path
    blob = b"".join(x.read_bytes() for x in out.rglob("*") if x.is_file())
    probes = []
    for r in payload["records"]:
        for s in (r["title"], r["performance_text"][100:160], r["introduction_text"][:60]):
            if len(s) >= 12:
                probes.append(s)
    readable = [s for s in probes if s.encode("utf-8") in blob]
    check("no title, introduction or text passage is readable in the published files (%d probes)" % len(probes), not readable, readable[:3])

    page = (out / "index.html").read_text(encoding="utf-8")
    check("the page has the unlock step and no embedded library", "window.__unlock" in page and "const LIB = null;" in page)
    cfg = json.loads(re.search(r"const C = (\{.*?\});", page).group(1))
    check("the page states the salt, rounds and number of parts", cfg["iter"] == PUB.ITER and cfg["parts"] == len([n for n in names if n.startswith("part-")]), cfg)

    # decrypt as the page would, with the published salt
    import base64
    AESGCM = PUB.need_crypto()
    key = PUB.derive(PW, base64.b64decode(cfg["salt"]))
    cat = PUB.unseal(AESGCM, key, (out / "data" / "catalog.bin").read_bytes())
    parts = [PUB.unseal(AESGCM, key, (out / "data" / ("part-%02d.bin" % i)).read_bytes()) for i in range(cfg["parts"])]
    check("the catalogue holds no performance text", not any("performance_text" in r for r in cat["records"]))
    back = PUB.merge(cat, parts)
    canon = lambda rs: [json.dumps(r, ensure_ascii=False, sort_keys=True) for r in rs]      # noqa: E731
    check("every record decrypts back exactly as on the single-file site", canon(back) == canon(payload["records"]), len(back))
    try:
        PUB.unseal(AESGCM, PUB.derive(PW + "!", base64.b64decode(cfg["salt"])), (out / "data" / "catalog.bin").read_bytes())
        check("a wrong password is refused", False)
    except Exception:
        check("a wrong password is refused", True)

    p = __import__("subprocess").run([sys.executable, "pipeline/publish.py", "--out", str(out)], cwd=d, capture_output=True, text=True,
                                     env=dict(os.environ, ILIB_PASSWORD="short"))
    check("a password under 8 characters is refused", p.returncode != 0 and "at least 8" in (p.stdout + p.stderr))
finally:
    cleanup(d)
    cleanup(out)
sys.exit(finish())
