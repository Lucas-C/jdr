#!/bin/bash

set -o pipefail -o errexit -o nounset -o xtrace

cd $(dirname ${BASH_SOURCE[0]})

TAG=${1:-2200_le_jugement_des_dieux}
TMP_FILE=$(mktemp).pdf

puppeteer print index.html ${TMP_FILE}
pdfjam --no-tidy ${TMP_FILE} 1-4 --nup 2x1 --landscape --outfile ../${TAG}.pdf
rm ${TMP_FILE}

puppeteer print 2200_the_gods_judgement.html ${TMP_FILE}
pdfjam --no-tidy ${TMP_FILE} 1-4 --nup 2x1 --landscape --outfile ../${TAG}-EN.pdf
rm ${TMP_FILE}
