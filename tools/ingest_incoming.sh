#!/usr/bin/env bash
# Codespace: add every PDF in incoming/ that parses cleanly to the library, correct the award lines of earlier
# records, rebuild, run every test, and push.  Refused files are listed in data/refused_files.json.
#   bash tools/ingest_incoming.sh
set -u
cd "$(dirname "$0")/.."
mkdir -p reports
git pull -q
{
  echo "== ingest of incoming/ started $(date -u '+%F %T') UTC"
  python3 pipeline/ingest.py --incoming --keep-going
  echo; echo "== award lines of earlier records"
  python3 pipeline/reextract_awards.py
  echo "== finished $(date -u '+%F %T') UTC"
} 2>&1 | tee reports/ingest_incoming.log
bash tests/run_all.sh
git add -A && git commit -q -m "Ingest of incoming/: $(grep -m1 'files given' reports/ingest_incoming.log)" && git push -q && echo "pushed the ingest."
