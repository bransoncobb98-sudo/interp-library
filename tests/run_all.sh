#!/usr/bin/env bash
# Run every build step and check, and save the output in tests/last_run.txt.
#   bash tests/run_all.sh          # in the Codespace (Linux); Windows cannot run the pipeline
#   bash tests/run_all.sh --push   # also commit and push the results, the rebuilt data and the site
set -u
cd "$(dirname "$0")/.."
STEPS=("pipeline/build.py" "tests/verify_ingest.py" "pipeline/qc_scan.py" "pipeline/repairs.py"
       "tests/test_columns.py" "tests/test_programs.py" "tests/test_publishers.py" "tests/test_build_site.py" "tests/test_classify.py" "tests/test_incremental_ingest.py" "pipeline/classify.py --queue")
{
  echo "== $(date -u '+%F %T') UTC | $(python3 --version 2>&1) | pdfplumber $(python3 -c 'import pdfplumber; print(pdfplumber.__version__)' 2>&1) | $(pdftotext -v 2>&1 | head -1)"
  status=0
  for step in "${STEPS[@]}"; do
    echo; echo "===== python3 $step"
    python3 $step || { echo "!!!!! FAILED: $step"; status=1; }
  done
  echo; [ $status = 0 ] && echo "== OVERALL: ALL STEPS PASSED" || echo "== OVERALL: SOME STEPS FAILED (search for !!!!! above)"
  exit $status
} 2>&1 | tee tests/last_run.txt
status=${PIPESTATUS[0]}
if [ "${1:-}" = "--push" ]; then
  git add -A && git commit -q -m "Codespace run: $(tail -1 tests/last_run.txt)" && git push -q && echo "pushed."
fi
exit $status
