#!/usr/bin/env bash
# Codespace: dry run over incoming/ (writes only reports/dry_run/), then commit and push the report.
#   bash tools/dry_run.sh
set -u
cd "$(dirname "$0")/.."
mkdir -p reports
python3 pipeline/dry_run_incoming.py --include-library --jobs "$(nproc)" 2>&1 | tee reports/dry_run.log
status=${PIPESTATUS[0]}
git add reports .gitignore && git commit -q -m "Dry run over incoming/ (nothing ingested)" && git pull -q --rebase && git push -q && echo "pushed the dry-run report."
exit $status
