#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})
OUT_FILE=${1:-adj-scavengers.pdf}
puppeteer print adj-scavengers.html tmp-$OUT_FILE
pdfjam --no-tidy tmp-$OUT_FILE --nup 2x1 --landscape --outfile $OUT_FILE
rm tmp-$OUT_FILE