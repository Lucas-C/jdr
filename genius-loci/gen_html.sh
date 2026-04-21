#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace

cd $(dirname ${BASH_SOURCE[0]})

mkdir -p fonts
cp ../fonts/GunnyRewritten.ttf fonts/
node ../md2html.js genius-loci.md > index.html
