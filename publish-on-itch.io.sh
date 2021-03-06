#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

declare -A gamesOnItchIo
gamesOnItchIo['2200_le_jugement_des_dieux']='2200-le-jugement-des-dieux'
gamesOnItchIo[gdav]=ameres-victoires-glorieuses-defaites
gamesOnItchIo[LesCouloirsDuTemps]=les-couloirs-du-temps
gamesOnItchIo[LesNonMorts]=les-non-morts

gitTagPrefix="${TRAVIS_TAG%-*}"
gameIdOnItchIo="${gamesOnItchIo[${gitTagPrefix}]:-}"
version=${TRAVIS_TAG##*-}
if [ -z "$gameIdOnItchIo" ]; then
    echo "No mapping found for $gitTagPrefix - aborting"
    exit 0
fi

if [ -z "${BUTLER_API_KEY:-}" ]; then
    echo '$BUTLER_API_KEY undefined - aborting'
    exit 1
fi

# Intalling butler - cf. https://itch.io/docs/butler/installing.html
curl -L -o butler.zip https://broth.itch.ovh/butler/linux-amd64/LATEST/archive/default
unzip butler.zip
chmod +x butler
./butler -V

# Publish a folder that IS *exactly* the release build:
mkdir -p itchio && rm -f itchio/*.*
cp $TRAVIS_TAG*.pdf itchio/
echo "Now publishing $gameIdOnItchIo @ $version on itch.io:"
./butler push itchio Lucas-C/$gameIdOnItchIo:pdf --userversion $version
