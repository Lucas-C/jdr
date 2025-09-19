#!/bin/bash

set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

f=GirlUnderground-FR.pdf
pdfly cat $f 1:15 -o tmp.pdf
pdfly 2-up tmp.pdf tmp-2up.pdf
pdfly cat $f 0 tmp-2up.pdf $f 16: -o GirlUnderground-FR-2up.pdf
rm tmp.pdf tmp-2up.pdf
