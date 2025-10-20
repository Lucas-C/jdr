#!/bin/bash
# Use pdfly & the scripts in https://github.com/Lucas-C/dotfiles_and_notes/tree/master/bin

set -o pipefail -o errexit -o nounset -o xtrace
cd $(dirname ${BASH_SOURCE[0]})

pdfly cat DiagrammeDeLaSaison1.pdf Diagramme.pdf DiagrammeDeLaSaison1-Etendu.pdf -o CriticalFondation-DiagrammeDeLaSaison1.pdf

if [ -r 'GIGAMIC_CRITICAL_PNP_RULES_DEMO.pdf' ]; then
  # On extrait les pages 2 & 3 :
  pdfly cat 'GIGAMIC_CRITICAL_PNP_RULES_DEMO.pdf' 1:3 -o tmp.pdf
  pdfly 2-up tmp.pdf RecapRegles-2up.pdf
  rm tmp.pdf
fi

if [ -r 'GIGAMIC_CRITICAL_MAP(01)_LABO.pdf' ]; then
  a4-from-imgs --landscape --no-margin --stretch CriticalFondation-Ep0-Carte.jpg
  a3-from-imgs --landscape --no-margin --stretch CriticalFondation-Ep0-Carte.jpg
  # Bundle all a4 maps
  pdfly cat CriticalFondation-Ep0-Carte-A4.pdf 'GIGAMIC_CRITICAL_MAP(01)_LABO.pdf' 'GIGAMIC_CRITICAL_MAP(02)_HOPITAL.pdf' NebulaMaps-Office-NexusRobotics-TopRoom-BW-A4.pdf 'GIGAMIC_CRITICAL_MAP(03)_FERME.pdf' 'GIGAMIC_CRITICAL_MAP(04)_LANCE-MARS.pdf' -o A4-maps-to-print.pdf
  rm CriticalFondation-Ep0-Carte-A4.pdf
fi
