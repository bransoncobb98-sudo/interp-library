#!/usr/bin/env bash
# Codespace: publish the library to the public site repository (GitHub Pages), encrypted with the class password.
#   bash tools/publish_site.sh
# Asks for the class password (typed twice; it is never saved or shown).  Only encrypted files and the page code
# go to the site repository; the PDFs and the database stay in this private repository.
set -eu
cd "$(dirname "$0")/.."
SITE_REPO="${SITE_REPO:-bransoncobb98-sudo/interp-library-site}"
CLONE="../interp-library-site"
python3 -c "import cryptography" 2>/dev/null || pip install --user -q -r requirements.txt
git pull -q
if [ ! -d "$CLONE/.git" ]; then
  git clone -q "https://github.com/$SITE_REPO.git" "$CLONE" || {
    echo "!!!!! Could not open $SITE_REPO. Create it on GitHub (public, empty), then rebuild this Codespace so it may write to it."; exit 1; }
fi
git -C "$CLONE" pull -q || true
python3 pipeline/publish.py --out "$CLONE"
cd "$CLONE"
git add -A
if git diff --cached --quiet; then echo "Nothing changed on the site."; exit 0; fi
git commit -q -m "Publish $(date -u '+%F %T') UTC"
git push -q && echo "published. The site updates within a few minutes: https://${SITE_REPO%%/*}.github.io/${SITE_REPO##*/}/" \
  || echo "!!!!! THE PUSH FAILED - copy the lines above and send them"
