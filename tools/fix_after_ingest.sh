#!/usr/bin/env bash
# Codespace: the one-time corrections found after the ingest of incoming/ (filing labels of loose DI/HI files,
# introductions cut mid-sentence, cutter credits), then rebuild, run every test, and push.
#   bash tools/fix_after_ingest.sh
set -u
cd "$(dirname "$0")/.."
mkdir -p reports
git pull -q
{
  echo "== corrections started $(date -u '+%F %T') UTC"
  echo; echo "== filing labels"
  python3 -u pipeline/fill_filing_labels.py
  echo; echo "== introductions and cutter credits"
  python3 -u pipeline/fix_intro_and_credit.py
  echo "== finished $(date -u '+%F %T') UTC"
} 2>&1 | tee reports/fix_after_ingest.log
bash tests/run_all.sh
git add -A && git commit -q -m "Corrections after the ingest: $(grep -m1 'corrected' reports/fix_after_ingest.log)" && git push -q && echo "pushed the corrections." || echo "!!!!! THE PUSH FAILED - copy the lines above and send them"
