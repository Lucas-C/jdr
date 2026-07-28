#!/bin/bash
# Require: pdfly
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

VERSION=1.1

gen_pdf_files() {
  local src="${1}"
  local dst="${2}"
  pdfly cat ${src}.pdf :4 -o ${dst}-v${VERSION}.pdf
  pdfly 2-up ${dst}-v${VERSION}.pdf ${dst}-v${VERSION}-2up.pdf
  pdfly cat ${src}.pdf 1:4 0 -o tmp.pdf
  pdfly 2-up tmp.pdf ${dst}-v${VERSION}-2up-foldable.pdf
  rm tmp.pdf
}

# Version française:
gen_pdf_files 2200_le_jugement_des_dieux 2200-le-jugement-des-dieux

# English version:
gen_pdf_files 2200_the_gods_judgement 2200-the-gods-judgement
