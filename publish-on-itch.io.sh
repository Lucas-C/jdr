#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

declare -A gamesOnItchIo
gamesOnItchIo[LesNonMorts]=les-non-morts
gamesOnItchIo[gdav]=ameres-victoires-glorieuses-defaites

gameIdOnItchIo="${gamesOnItchIo[${TRAVIS_TAG%-*}]:-}"
version=${TRAVIS_TAG##*-}
if [ -z "$gameIdOnItchIo" ]; then
    exit 0
fi

# Intalling butler - cf. https://itch.io/docs/butler/installing.html
curl -L -o butler.zip https://broth.itch.ovh/butler/linux-amd64/LATEST/archive/default
unzip butler.zip
chmod +x butler
./butler -V

# Publish a folder that IS *exactly* the release build:
mkdir -p itchio && rm -f itchio/*.*
cp $TRAVIS_TAG*.pdf itchio/
./butler push itchio Lucas-C/$gameIdOnItchIo:pdf --userversion $version
