#!/bin/bash
# Require: ImageMagick `convert` command
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

# Generate JPEG images from single-page PDF files:
convert Abductes-monopage.pdf -flatten Abductes-monopage.png
convert Abductes-monopage.png Abductes-monopage.jpg
rm Abductes-monopage.png
convert AbductedNegotiators-singlePage.pdf -flatten AbductedNegotiators-singlePage.png
convert AbductedNegotiators-singlePage.png AbductedNegotiators-singlePage.jpg
rm AbductedNegotiators-singlePage.png

# Generate JPEG images from banner-cards.pdf:
convert banner-cards.pdf[0] -flatten banner-cards-1.91.png
convert banner-cards-1.91.png banner-cards-1.91.jpg
jpegoptim --all-progressive -m90 banner-cards-1.91.jpg
convert banner-cards.pdf[1] -flatten banner-cards-640x500.png
convert banner-cards-640x500.png banner-cards-640x500.jpg
jpegoptim --all-progressive -m90 banner-cards-640x500.jpg
rm banner-cards-*.png
