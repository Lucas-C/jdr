#!/bin/bash
# Use pdfly, ImageMagick & the scripts in https://github.com/Lucas-C/dotfiles_and_notes/tree/master/bin

set -o pipefail -o errexit -o nounset #-o xtrace
cd $(dirname ${BASH_SOURCE[0]})

# LivretDAventures: 2xA5 on A4 :
convert -density 600 character-sheets/OriMushi-LivretDAventures.pdf tmp-%03d.png
mv tmp-000.png character-sheets/OriMushi-LivretDAventures-2x.png
a5-from-img --portrait character-sheets/OriMushi-LivretDAventures-2x.png
rm character-sheets/OriMushi-LivretDAventures-2x.png

# FeuillePersonnage: 2xA5 on A4 :
convert -density 600 character-sheets/OriMushi-FeuillePersonnage.pdf tmp-%03d.png
mv tmp-000.png character-sheets/OriMushi-FeuillePersonnage-2x.png
a5-from-img character-sheets/OriMushi-FeuillePersonnage-2x.png
rm character-sheets/OriMushi-FeuillePersonnage-2x.png

# Create small FP JPEG to be used in OriMushi-VoiesDesKomuso-Acte1.fodg:
convert -density 300 character-sheets/OriMushi-FeuillePersonnage.pdf character-sheets/OriMushi-FeuillePersonnage-small.jpg
jpegoptim --all-progressive -m90 character-sheets/OriMushi-FeuillePersonnage-small.jpg

# Extract AdJ "Pendant ce temps...":
pdfly cat GuideDuMJ.pdf 5:7 -o OriMushi-PendantCeTemps.pdf

# Extract AdJ "Durant cette année...":
pdfly cat Campagne.pdf 6 -o OriMushi-DurantCetteAnnee.pdf
