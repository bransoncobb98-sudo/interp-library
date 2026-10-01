# Interpretation Library: Administrator Guide

A searchable library of interpretation cuttings built from your PDFs. The database is a plain JSON file; the library is
one HTML file with everything inside it. This guide covers what exists after Phase 5. The review tool, the locked page and
hosting come in Phases 6 to 8 and will be added here.

## What you need

- A GitHub Codespace on the project's private repository. It sets itself up from `.devcontainer/` (Python 3.12,
  `pdfplumber`, `pdftotext`). The pipeline does not run on Windows.

## Everyday workflow

1. **Add PDFs.** Put them in `sources/`, then
   `python pipeline/ingest.py sources/NEW.pdf --event "Dramatic Interpretation" --filing-label "Any Gender"`.
   Run it with `--dry-run` first to see what would happen. Re-running a file that is already in the library does nothing.
   A byte-identical copy under another name is noted on the existing record. Every new record is checked for duplicates
   against every existing record.
2. **Classify.** `python pipeline/classify.py --queue` writes `data/classification_requests/batch-001.md` and so on, up to
   40 cuttings each. Open one, copy all of it into an AI model (for example Claude), and save the model's JSON reply as a
   file. Then `python pipeline/classify.py --apply that-file.json --dry-run` to check it, and again without `--dry-run`
   to apply it. Anything invalid is rejected and listed; the rest is applied. Do one batch at a time.
3. **Rebuild.** `python pipeline/build.py` checks the database and rebuilds `site/index.html` and `exports/`.
4. **Check.** `bash tests/run_all.sh` runs the build and every test, and writes `tests/last_run.txt`.

## Tasks

**Correct a text error from the PDF.** Add an entry to `data/text_repairs.json`: the file, the exact wrong text, the
correct text, the reason and who approved it. The wrong text must occur exactly once, or the build stops and changes
nothing. The original stays in `text_raw` and each repair is listed in the record's extraction notes.

**Understand duplicates.** An exact duplicate (identical spoken words) is shown once; the other file is listed under
"Also appears in". Pieces cut from the same published book are linked under "From the same book". They are not duplicates.

**Hide a record.** Phase 6 adds Archive and Restore buttons. Until then, set `record_status` to `Archived` in
`data/cuttings.json` and rebuild. Archived records stay in the database and never reach the page.

**A QC finding that is really in the source.** Add it to `data/qc_acknowledged.json` with a reason. `qc_scan.py` lists
acknowledgements that no longer match anything, so stale ones do not pile up.

## What the data-quality statuses mean

| Status | Meaning |
|---|---|
| Verified | A person has checked the record. |
| High Confidence | No open issues and high AI confidence. |
| Needs Review | Unclassified, flagged, or the pipeline left a note. |
| Missing Metadata | Title or author not specified. |
| Possible Duplicate | Matches another record. |

## Things to know

- **No run times, no league rules.** You chose to skip both. The site shows spoken-word counts only.
- **The AI step is a hand-off.** The pipeline never calls an AI service. Every AI value carries a confidence and one
  sentence of evidence, and the site labels it AI-suggested. AI never overwrites what the source states or what you entered.
- **Suggested audience level is a suggestion,** never a judgement that a piece is appropriate.
- **Exports are private.** `exports/` holds every record, including hidden ones and any takedown details. Never publish it.
- **Copyright.** The library reproduces full cuttings of published, copyrighted works, some probably cut by other
  schools. Source, credit and copyright notices are kept exactly as given. A password limits who can see the cuttings; it
  does not make sharing them permitted. The one copyright notice on file (Consequences, SpeechGeek) permits performance
  for high school and college forensics. It does not mention hosting a copy.
