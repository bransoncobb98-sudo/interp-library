# Interpretation Library (work in progress: phases 1-4 done)

Modeled on the monologue library. Phases 5-8 (site, review tool, password portal, hosting) are not built yet.

## What works now
    python pipeline/ingest.py sources/*.pdf --event "Dramatic Interpretation" --filing-label "Any Gender" [--dry-run]
    python pipeline/qc_scan.py            # text-quality scan beyond counts
    python tests/verify_ingest.py         # independent count and integrity checks

Needs Python 3.9+, `pdfplumber`, and poppler's `pdftotext` (used only by the tests).

## Files
- `data/cuttings.json` the database (45 records). `data/source_files.json` every file received, including identical copies.
- `data/taxonomy.json` approved vocabulary. `data/pace.json` PLACEHOLDER reading pace. `data/league_limits.json` limits with source URLs and confidence.
- `data/qc_acknowledged.json` findings verified as present in the source PDFs themselves.
- `pipeline/layouts.py` one parser per layout (`di_cutting`, `publisher_script`). `pipeline/ilib.py` schema, counting rules, timing, provenance.

## Rules applied to word counts
Ignored: (parenthetical directions), (Pg N) references, uppercase speaker labels, lines starting NOTE:.
Counted: everything else, including [bracketed] text. The stored text is never altered.

## Honest limits
Nothing here has been viewed on a screen. No AI classification has been run. League limits are from tournament pages and
secondary copies, not the current manuals. Pace (150 wpm) is a placeholder. Hosting full cuttings carries copyright risk.
