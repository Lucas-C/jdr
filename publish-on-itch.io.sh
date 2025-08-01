#!/bin/bash
set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

declare -A gamesOnItchIo  # map git tags to itch.io IDs
gamesOnItchIo['2200_le_jugement_des_dieux']='2200-le-jugement-des-dieux'
gamesOnItchIo[gdav]=ameres-victoires-glorieuses-defaites
gamesOnItchIo[LesCouloirsDuTemps]=les-couloirs-du-temps
gamesOnItchIo[LesNonMorts]=les-non-morts
gamesOnItchIo[CyberPunk]=cyberpunk
gamesOnItchIo[BladesInTheDark-Interrogatoires]=blades-in-the-dark-interrogatoires
gamesOnItchIo[BladesInTheDark-Interrogation]=blades-in-the-dark-interrogation
gamesOnItchIo[ParadisPerdu]=modules-de-secours
gamesOnItchIo[PsiRun-Implacables]=psirun-implacables
gamesOnItchIo[PsiRun-TheRestless]=psirun-the-restless
gamesOnItchIo[PsiRun-ReglesAdditionnelles]=psirun-regles-additionnelles
gamesOnItchIo[PsiRun-ExtraRules]=psirun-extra-rules

GITHUB_REF=${1?-'git ref must be provided as argument'}
GIT_TAG=${GITHUB_REF##*/}
gitTagPrefix=${GIT_TAG%-*}
echo gitTagPrefix=$gitTagPrefix
gameIdOnItchIo="${gamesOnItchIo[${gitTagPrefix}]:-}"
version=${GIT_TAG##*-}
if [ -z "$gameIdOnItchIo" ]; then
    echo "No mapping found for $gitTagPrefix - aborting"
    exit 0
fi

if [ -z "${BUTLER_API_KEY:-}" ]; then
    echo '$BUTLER_API_KEY undefined - aborting'
    exit 1
fi

echo 'Installing butler CLI'  # cf. https://itch.io/docs/butler/installing.html
curl -L -o butler.zip https://broth.itch.ovh/butler/linux-amd64/LATEST/archive/default
unzip butler.zip
chmod +x butler
./butler -V

# Publish a folder that IS *exactly* the release build:
mkdir -p itchio && rm -f itchio/*.*
cp $GIT_TAG*.pdf itchio/
echo "Now publishing $gameIdOnItchIo @ $version on itch.io:"
./butler push itchio Lucas-C/$gameIdOnItchIo:pdf --userversion $version
