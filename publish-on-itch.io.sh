#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

# Intalling butler - cf. https://itch.io/docs/butler/installing.html
curl -L -o butler.zip https://broth.itch.ovh/butler/linux-amd64/LATEST/archive/default
unzip butler.zip
chmod +x butler
./butler -V

# Publish a folder that that is *exactly* the release build:
mkdir -p itchio
mv $TRAVIS_TAG*.pdf itchio/
./butler push itchio Lucas-C/${TRAVIS_TAG%-*}:pdf --userversion ${TRAVIS_TAG##*-}
