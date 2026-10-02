#!/usr/bin/env python3
"""Mushroom Cloud Press layouts (cover, series, classic): title, author, notice and script split correctly.
Run:  python tests/test_publishers.py      (needs pdfplumber and pdftotext)"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
sys.path.insert(0, str(ROOT / "tests"))
import layouts as L                     # noqa: E402
import ingest as G                      # noqa: E402
from _sandbox import check, finish      # noqa: E402

CASES = [
    ("incoming/HI/Male HIs/Mushroom Cloud - Dis-Orientation.pdf", "cover", "Dis-Orientation", "Robert W. LaVohn",
     "Permission for performance of this piece is granted", "Taylor, a nervous college freshman"),
    ("incoming/DI/MushroomCloud - Sister of Mercy.pdf", "series", "Sister of Mercy", "Clyde Hendrickson",
     "Free performance of this play", "[A teenage girl."),
    ("incoming/Duo-Duet/F-F Duos & Duets/MushroomCloud_Unfunny.pdf", "series", "UNFUNNY", "Michael Beede",
     "All other rights reserved.", "“Unfunny” was originally intended"),
    ("incoming/Prose/Mushroom Cloud Press - Classic Prose Collection/MushroomCloudPress_ClassicProseCollection/The Magic Shop - Mushroom Cloud Press.pdf",
     "classic", "The Magic Shop", "H.G. Wells", None, "I had seen the Magic Shop from afar"),
]
for rel, variant, title, author, notice, starts in CASES:
    f = ROOT / rel
    if not f.exists():
        check("test file present: " + rel, False)
        continue
    r = L.parse_pdf(str(f))
    name = f.name
    check("%s: Mushroom Cloud %s layout" % (name, variant), r["layout"] == "mcp" and r.get("variant") == variant, (r["layout"], r.get("variant")))
    if r["layout"] != "mcp":
        continue
    check("%s: every line in exactly one place" % name, L.conservation(r)[0], L.conservation(r)[1])
    rec = G.build_record("IC-T", str(f), r, "x", "Humorous Interpretation", "")
    check("%s: title and author" % name, (rec["title"], rec["author"]) == (title, author), (rec["title"], rec["author"]))
    check("%s: publisher stated as Mushroom Cloud Press" % name, rec["publisher"] == "Mushroom Cloud Press")
    if notice:
        check("%s: notice stored exactly as printed" % name, notice in rec["copyright_notice"], rec["copyright_notice"][:120])
    else:
        check("%s: no notice in this file, so none stored" % name, rec["copyright_notice"] == "Not specified")
    check("%s: no introduction in this layout" % name, rec["intro_boundary"] == "Not applicable" and not rec["introduction_text"])
    check("%s: the script starts after the title page" % name, rec["performance_text"].startswith(starts), rec["performance_text"][:60])
    check("%s: no notice text inside the script" % name, "Mushroom Cloud Press" not in rec["performance_text"][:400])
sys.exit(finish())
