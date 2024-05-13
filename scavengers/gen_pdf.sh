#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})
IN_FILE=${1:-adj-scavengers.html}
OUT_FILE=${2:-adj-scavengers.pdf}
TMP_FILE=$(mktemp).pdf
node ../puppeteer-print.js index.html ${TMP_FILE}
node ../puppeteer-print.js ${IN_FILE} ${TMP_FILE}
pdfjam --no-tidy ${TMP_FILE} --nup 2x1 --landscape --outfile ${OUT_FILE}
rm ${TMP_FILE}