#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})
IN_FILE=${1:-adj-scavengers.html}
OUT_FILE=${2:-adj-scavengers.pdf}
puppeteer print ${IN_FILE} tmp-${OUT_FILE}
pdfjam --no-tidy tmp-${OUT_FILE} --nup 2x1 --landscape --outfile ${OUT_FILE}
rm tmp-${OUT_FILE}