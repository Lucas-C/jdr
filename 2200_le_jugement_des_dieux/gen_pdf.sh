#!/bin/bash
# USAGE: rm -f *.html; ./gen_pdf.sh && mv ../2200*.pdf .

set -o pipefail -o errexit -o nounset -o xtrace

cd $(dirname ${BASH_SOURCE[0]})

PAGE_FORMAT=793x1120  # A4
MARGIN=0x50
TAG=${1:-2200_le_jugement_des_dieux}
TMP_FILE=$(mktemp).pdf

if ! [ -r index.html ]; then
  node ../md2html.js 2200_le_jugement_des_dieux.md > index.html
  echo "Produced: ./index.html"
fi
node ../puppeteer-print.js index.html ${TMP_FILE} ${PAGE_FORMAT} ${MARGIN}
pdfjam --no-tidy ${TMP_FILE} 1-4 --nup 2x1 --landscape --outfile ../${TAG}.pdf
echo "Produced: ../${TAG}.pdf"
rm ${TMP_FILE}

if ! [ -r 2200_the_gods_judgement.html ]; then
  node ../md2html.js --lang=en 2200_the_gods_judgement.md > 2200_the_gods_judgement.html
  echo "Produced: ./2200_the_gods_judgement.html"
fi
node ../puppeteer-print.js 2200_the_gods_judgement.html ${TMP_FILE} ${PAGE_FORMAT} ${MARGIN}
pdfjam --no-tidy ${TMP_FILE} 1-4 --nup 2x1 --landscape --outfile ../${TAG}-EN.pdf
echo "Produced: ../${TAG}-EN.pdf"
rm ${TMP_FILE}
