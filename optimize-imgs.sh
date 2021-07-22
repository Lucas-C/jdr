#!/bin/bash

# USAGE: ./optimize-imgs.sh [$optional_dir]

set -o errexit -o nounset -o pipefail

if [ $# -gt 0 ]; then
    cd "$1"
fi

for jpg in *.jpg; do
    if ! grep -Fq $'\xff\xc2' "$jpg"; then
        jpegoptim --all-progressive -m90 "$jpg"
        chmod 644 "$jpg"
    fi
done

for png in *.png; do
    pngquant --ext .png -f "$png"
    chmod 644 "$png"
done
