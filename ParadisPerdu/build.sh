#!/bin/bash
set -o pipefail -o errexit -o nounset
cd $(dirname ${BASH_SOURCE[0]})

if ! [ -d ../../pinterest-downloader ]; then
    cd ../..
    git clone git@github.com:limkokhole/pinterest-downloader.git
    pip install --user -r pinterest-downloader/requirements.txt
    cd -
fi

for dir in acte-1 acte-2 acte-3 persos; do
    ../../pinterest-downloader/pinterest-downloader.py -d . https://www.pinterest.fr/drmaxkurt/paradis-perdu-${dir}/
    mv drmaxkurt/paradis-perdu-${dir} gallery/${dir}
done
rmdir drmaxkurt

pip install --user sigal
sigal build