#!/usr/bin/env bash
# Codespace: apply every waiting classification reply in data/classification_replies/, rebuild, push.
#   bash tools/apply_classifications.sh
# Each reply goes through pipeline/classify.py --apply (every value checked; rejected values are listed and not
# applied).  An applied reply is moved to data/classification_replies/applied/ so it is never applied twice; the
# reply and its report are also archived in data/classifications/ by classify.py.
set -u
cd "$(dirname "$0")/.."
git pull -q --rebase
mkdir -p data/classification_replies/applied reports
shopt -s nullglob
files=(data/classification_replies/*.json)
if [ ${#files[@]} -eq 0 ]; then echo "No replies waiting."; exit 0; fi
{
  echo "== applying ${#files[@]} reply file(s) $(date -u '+%F %T') UTC"
  for f in "${files[@]}"; do
    echo; echo "== $f"
    if python3 pipeline/classify.py --apply "$f"; then git mv -k "$f" data/classification_replies/applied/ 2>/dev/null || mv "$f" data/classification_replies/applied/
    else echo "!!!!! NOT APPLIED: $f"; fi
  done
  echo; echo "== rebuild"
  python3 pipeline/build.py
  python3 pipeline/classify.py --queue
} 2>&1 | tee reports/apply_classifications.log
grep -c "REJECTED" reports/apply_classifications.log | sed 's/^/rejected values (listed above, not applied): /'
git add -A && git commit -q -m "Classifications applied: $(grep -c '^== data/classification_replies' reports/apply_classifications.log) reply file(s)" \
  && git pull -q --rebase && git push -q && echo "pushed the classifications." || echo "!!!!! THE PUSH FAILED - copy the lines above and send them"
