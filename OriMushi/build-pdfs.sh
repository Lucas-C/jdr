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

# Create small FP JPEG to be used in OriMushi-VoiesDesPersonnages.fodg:
convert -density 300 character-sheets/OriMushi-FeuillePersonnage.pdf character-sheets/OriMushi-FeuillePersonnage-small.jpg
optim-jpgs character-sheets/OriMushi-FeuillePersonnage-small.jpg

# Extract 1st paliers of OriMushi-VoiesDesPersonnages.fodg:
pdfly cat character-sheets/OriMushi-VoiesDesPersonnages.pdf 0 3 6 9 -o character-sheets/OriMushi-VoiesDesPersonnages-Palier1.pdf
