#!/usr/bin/env python3
"""Publish the library as an encrypted static site (for GitHub Pages or any web host).

The page opens with a password form.  The class password unlocks
  data/catalog.bin   every visible record without its performance text (search, filters and introductions work
                     as soon as this arrives), and
  data/part-NN.bin   the performance texts, selection texts, classification evidence and extraction notes, in parts
                     of about 1.4 million characters, fetched one after another in the background.
Each file is gzip'd JSON encrypted with AES-256-GCM under a key derived from the password (PBKDF2-SHA256, 600,000
rounds, a new random salt on every publish).  Nothing readable is published except the page code and the site title.
The records are exactly those of site/index.html (same build), and before finishing this script decrypts what it
wrote and checks that every record comes back identical to the database's public record.

    python pipeline/publish.py --out publish/out                  # asks for the class password (typed twice)
    ILIB_PASSWORD='...' python pipeline/publish.py --out DIR      # or from the environment

Only these are written in --out: index.html, robots.txt, .nojekyll and data/*.bin (old data/*.bin are replaced), so
--out may be a clone of the site repository.
"""
import argparse
import base64
import getpass
import gzip
import hashlib
import json
import os
import secrets
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import ilib as I          # noqa: E402
import build as B         # noqa: E402

ITER = 600_000
PART_CHARS = 1_400_000


def need_crypto():
    try:
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM   # noqa: F401
        return AESGCM
    except ImportError:
        sys.exit("The 'cryptography' package is needed:  pip install --user 'cryptography>=42'")


def split(payload, part_chars=PART_CHARS):
    """(catalogue, parts).  The catalogue is the payload with each record's text-only fields moved to a part; each
    catalogue record carries _p, the number of its part."""
    cat = {k: v for k, v in payload.items() if k != "records"}
    recs, parts, size = [], [{}], 0
    for r in payload["records"]:
        r = json.loads(json.dumps(r, ensure_ascii=False))               # a copy
        t = {"performance_text": r.pop("performance_text")}
        if "ingest_notes" in r:
            t["ingest_notes"] = r.pop("ingest_notes")
        if r.get("selections"):
            t["sel_texts"] = [s.pop("text", "") for s in r["selections"]]
        ev = {f: p.pop("evidence") for f, p in (r.get("provenance") or {}).items() if "evidence" in p}
        if ev:
            t["evidence"] = ev
        n = len(json.dumps(t, ensure_ascii=False))
        if size and size + n > part_chars:
            parts.append({})
            size = 0
        parts[-1][r["id"]] = t
        size += n
        r["_p"] = len(parts) - 1
        recs.append(r)
    cat["records"], cat["parts"] = recs, len(parts)
    return cat, parts


def merge(cat, parts):
    """What the page does with the parts (site/unlock.html, merge()); used to check the round trip."""
    out = []
    for r in json.loads(json.dumps(cat["records"], ensure_ascii=False)):
        t = parts[r.pop("_p")][r["id"]]
        r["performance_text"] = t["performance_text"]
        if "ingest_notes" in t:
            r["ingest_notes"] = t["ingest_notes"]
        for s, x in zip(r.get("selections") or [], t.get("sel_texts", [])):
            s["text"] = x
        for f, e in t.get("evidence", {}).items():
            r["provenance"][f]["evidence"] = e
        out.append(r)
    return out


def derive(password, salt):
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    return PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(password.encode("utf-8"))


def seal(AESGCM, key, obj):
    data = gzip.compress(json.dumps(obj, ensure_ascii=False, separators=(",", ":")).encode("utf-8"), 9, mtime=0)
    iv = secrets.token_bytes(12)
    return iv + AESGCM(key).encrypt(iv, data, None)


def unseal(AESGCM, key, blob):
    return json.loads(gzip.decompress(AESGCM(key).decrypt(blob[:12], blob[12:], None)).decode("utf-8"))


def ask_password():
    pw = os.environ.get("ILIB_PASSWORD")
    if not pw:
        if not sys.stdin.isatty():
            sys.exit("No password: set ILIB_PASSWORD or run this in a terminal.")
        pw = getpass.getpass("Class password for the published library: ")
        if getpass.getpass("Type it again: ") != pw:
            sys.exit("The two passwords differ. Nothing written.")
    if len(pw) < 8:
        sys.exit("Use a password of at least 8 characters. Nothing written.")
    return pw


def publish(db, out, password, part_chars=PART_CHARS, log=print):
    AESGCM = need_crypto()
    payload = B.site_payload(db)
    cat, parts = split(payload, part_chars)
    salt = secrets.token_bytes(16)
    key = derive(password, salt)
    blobs = {"catalog": seal(AESGCM, key, cat)}
    for i, p in enumerate(parts):
        blobs["part-%02d" % i] = seal(AESGCM, key, p)
    version = hashlib.sha256(b"".join(blobs[k] for k in sorted(blobs))).hexdigest()[:12]
    cfg = {"salt": base64.b64encode(salt).decode(), "iter": ITER, "parts": len(parts), "v": version}
    unlock = (I.SITE / "unlock.html").read_text(encoding="utf-8")
    if "/*__LOCK_CONFIG__*/null" not in unlock:
        raise RuntimeError("site/unlock.html has no config placeholder")
    page = B.page_from_template("null", payload["config"]["title"], unlock.replace("/*__LOCK_CONFIG__*/null", json.dumps(cfg)))

    out = Path(out)
    (out / "data").mkdir(parents=True, exist_ok=True)
    for old in (out / "data").glob("*.bin"):
        old.unlink()                                            # the previous publish's files (kept in git history)
    for name, blob in blobs.items():
        (out / "data" / (name + ".bin")).write_bytes(blob)
    (out / "index.html").write_text(page, encoding="utf-8")
    (out / "robots.txt").write_text("User-agent: *\nDisallow: /\n", encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")

    # check what was written: it decrypts with this password only, and gives back every record exactly
    key2 = derive(password, base64.b64decode(cfg["salt"]))
    cat2 = unseal(AESGCM, key2, (out / "data" / "catalog.bin").read_bytes())
    parts2 = [unseal(AESGCM, key2, (out / "data" / ("part-%02d.bin" % i)).read_bytes()) for i in range(cfg["parts"])]
    back = merge(cat2, parts2)
    canon = lambda rs: [json.dumps(r, ensure_ascii=False, sort_keys=True) for r in rs]    # noqa: E731
    if canon(back) != canon(payload["records"]):
        raise RuntimeError("round-trip check failed: the decrypted records differ from the database")
    try:
        unseal(AESGCM, derive(password + "x", salt), blobs["catalog"])
        raise RuntimeError("a wrong password decrypted the catalogue")
    except RuntimeError:
        raise
    except Exception:
        pass
    leaked = [r["id"] for r in payload["records"][:50] if r["title"] and len(r["title"]) > 12 and r["title"] in page]
    if leaked:
        raise RuntimeError("record titles are readable in index.html: %s" % leaked[:5])
    sizes = {k: len(v) for k, v in blobs.items()}
    log("Published %d records to %s: catalogue %.1f MB, %d text parts of %.1f-%.1f MB (%.1f MB in all), version %s."
        % (len(back), out, sizes["catalog"] / 1e6, len(parts), min(v for k, v in sizes.items() if k != "catalog") / 1e6,
           max(v for k, v in sizes.items() if k != "catalog") / 1e6, sum(sizes.values()) / 1e6, version))
    log("Checked: every record decrypts back exactly; a wrong password is refused; no record title is readable in the page.")
    return cfg


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", required=True, help="folder for the site (for example a clone of the site repository)")
    a = ap.parse_args()
    need_crypto()
    db = I.load_db()
    errors, _ = B.validate(db)
    if errors:
        sys.exit("The database has errors; run pipeline/build.py first. Nothing published.")
    publish(db, a.out, ask_password())
    return 0


if __name__ == "__main__":
    sys.exit(main())
