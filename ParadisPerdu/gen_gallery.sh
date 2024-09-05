#!/bin/bash
set -o pipefail -o errexit -o nounset
cd $(dirname ${BASH_SOURCE[0]})

# Installation de sigal & pinterest-downloader :
pip install --user sigal
if ! [ -d ../../pinterest-downloader ]; then
    cd ../..
    git clone https://github.com/limkokhole/pinterest-downloader.git
    pip install --user -r pinterest-downloader/requirements.txt
    cd -
fi

mkdir -p gallery/ gallery/persos/
cp img/* gallery/persos/
rm gallery/persos/cc-by-nc-sa.png
mv -t gallery/ gallery/persos/AscensionTract.jpg gallery/persos/SpaceStation* gallery/persos/TheExpanse-Donnager-by-7-X-cc-by.webp
# Import des images depuis les galeries Pinterest :
for dir in acte-1 acte-2 acte-3 persos; do
    rm -rf gallery/${dir}
    ../../pinterest-downloader/pinterest-downloader.py -d . https://www.pinterest.fr/drmaxkurt/paradis-perdu-${dir}/
    mv drmaxkurt/paradis-perdu-${dir} gallery/${dir}
    rm gallery/${dir}/*.log gallery/${dir}/*.urls
done
rmdir drmaxkurt

# Génération de la galerie web :
sigal build
