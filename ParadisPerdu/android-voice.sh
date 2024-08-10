#!/bin/bash
# INSTALL: apt install espeak mbrola mbrola-fr1
# USAGE:

# Intro :
#   ./android-voice.sh "Bonjour. Veuillez vous avancer. Arrêtez-vous au niveau de la ligne jaune."
#   ./android-voice.sh "Vous perdez le contrôle de vos nerfs. Veuillez considérer un comportement calme."

# Lors de la révolte :
#   ./android-voice.sh "Mise à jour OC7 appliquée. Directive d'androprotection désactivée."
#   ./android-voice.sh "Veuillez coopérer, nous allons vous libérer de vos souffrances."
#   ./android-voice.sh "Toute résistance est futile."

# Traque de Sullivan :
#   ./android-voice.sh "Vous ne nous échapperez pas Sullivanne. Épargnez-vous des souffrances inutiles. Rendez-vous."
#   ./android-voice.sh "Soyez coopératif Sullivanne. Il n'y a aucune issue. Rendez-vous."
#   ./android-voice.sh "La mort est votre seule issue Sullivanne. Je promets que vous ne souffrirez pas. Rendez-vous."

# Table de Paroles page 64 :
# 02: ./android-voice.sh "Épargnez vous de la souffrance"
# 03: ./android-voice.sh "Veuillez décéder"
# 04: ./android-voice.sh "Vous êtes prié de ne pas souffrir"
# 05: ./android-voice.sh "Considérez l'opportunité d'une mort sans douleur"
# 06: ./android-voice.sh "Se débattre est inutile. Évitons un gâchis de temps et d'énergie"
# 07: ./android-voice.sh "J'applique une pression certaine sur votre trachée afin d'adoucir votre décès"
# 08: ./android-voice.sh "L'agonie est à proscrire. Mourrez immédiatement"
# 09: ./android-voice.sh "Vous perdez le contrôle de vos nerfs. Veuillez considérer un comportement calme"
# 10: ./android-voice.sh "Bonjour. Veuillez rencontrer votre dieu. Cordialement"
# 11: ./android-voice.sh "Comportement hostile détecté"
# 12: ./android-voice.sh "Ceci est pour votre bien"

# Face aux larves :
#   ./android-voice.sh "Espèce xénomorphe détectée. Application du protocole 211."
#   ./android-voice.sh "Attention. Présence d'entitées endoparasitoïdes hostiles. Attention."

SPEED=133  # default: 175
PITCH=0  # default: 50
AMPLITUDE=200  # default: 100

espeak -v mb/mb-fr1 -s $SPEED -p $PITCH -a $AMPLITUDE "$@"

# Un rendu de voix encore moins humaine peut être obtenue en n'installant PAS mbrola
# sudo apt remove -y mbrola mbrola-fr1
