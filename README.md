# Interpretation Library (phases 1 to 5 done)

A searchable library of speech and debate interpretation cuttings, modeled on the monologue library.
Phases 6 to 8 (review tool, password portal or locked page, hosting) are not built yet.

## Where it runs
The pipeline needs Linux or macOS (it locks the database with `fcntl`). On Windows, use the GitHub Codespace:
the `.devcontainer/` folder installs Python 3.12, `pdfplumber` and poppler's `pdftotext`.

    bash tests/run_all.sh          # build, every check, and the classification batches; output in tests/last_run.txt
    bash tests/run_all.sh --push   # the same, then commit and push the results

## Commands
    python pipeline/ingest.py sources/NEW.pdf --event "Dramatic Interpretation" --filing-label "Any Gender" [--dry-run] [--layout NAME]
    python pipeline/build.py                 # apply approved text repairs, validate, rebuild site/index.html and exports/
    python pipeline/classify.py --queue      # data/classification_requests/batch-NNN.md, up to 40 records each
    python pipeline/classify.py --apply reply.json [--dry-run]
    python pipeline/qc_scan.py               # text-quality scan beyond counts
    python pipeline/repairs.py               # which approved text repairs are applied

## Files
- `data/cuttings.json` the database. `data/source_files.json` every file received, including identical copies.
- `data/taxonomy.json` approved vocabulary. `data/text_repairs.json` director-approved text corrections (exact strings only).
- `data/qc_acknowledged.json` QC findings verified as present in the source PDFs, each with a reason.
- `data/classification_examples/` a worked example of an AI reply. `data/classifications/` applied replies and their reports.
- `site/template.html` the library page; `site/index.html` is built from it with the data inside (one file, works offline).
- `exports/` the whole database as JSON, CSV and SQLite (with full-text search), plus taxonomy, schema and source report.
  Exports include hidden records and takedown logs: admin use only, never publish them.
- `docs/not_used/` the run-time pace and league limits from Phase 4, no longer used.

## Rules
- Word counts ignore (parenthetical directions), (Pg N) references, uppercase speaker labels and lines starting NOTE:.
  Everything else counts, including [bracketed] text. The introduction is counted separately.
- No run times and no league rules: the director chose to skip both (2026-09-30). Nothing says a piece is legal or eligible.
- Text is not altered except by repairs listed in `data/text_repairs.json`; the text as extracted stays in `text_raw`.
- AI values carry a confidence and evidence and never overwrite source or reviewer values. Content warnings must quote the
  performance text.
- Records hidden by a removal request or archiving never reach `site/index.html`, nor do identical copies of a removed text.

## Honest limits
- No person has looked at the site on a real screen. A script drove it in a Chromium-based browser pane (search, chips,
  filters, record page, page-reference toggle, removal dialog, phone width); see the Phase 5 report.
- The library reproduces full cuttings of copyrighted works. A password limits who can see them; it does not grant permission.
