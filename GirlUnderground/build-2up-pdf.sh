#!/bin/bash

set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

f=GirlUnderground-FR.pdf
pdfly cat $f 1:15 -o tmp.pdf
pdfly 2-up tmp.pdf tmp-2up.pdf
pdfly cat $f 0 tmp-2up.pdf $f 15: -o GirlUnderground-FR-2up.pdf
rm tmp.pdf tmp-2up.pdf

if [ -r Girl_Underground.pdf ]; then
  pdfly cat Girl_Underground.pdf 5:13 29:47 -o tmp2.pdf
  pdfly 2-up tmp2.pdf GirlUnderground-ToPrint.pdf
  rm tmp2.pdf
fi
