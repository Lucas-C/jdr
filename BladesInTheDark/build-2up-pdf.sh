#!/bin/bash
# Require: pdfly
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

gen_pdf_files() {
  local src="${1?}"
  local dst="${2?}"
  pdfly cat "${src}" 0 "${src}" 0 -o tmp.pdf
  pdfly 2-up tmp.pdf "${dst}"
  rm tmp.pdf
}

# Version française:
gen_pdf_files BitD-FeuilleDeDemon.pdf BitD-FeuilleDeDemon-2up.pdf

# English version:
gen_pdf_files BitD-DemonSheet.pdf BitD-DemonSheet-2up.pdf
