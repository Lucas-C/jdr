#!/usr/bin/env python3
# Script Dependencies:
#    qrcode
import qrcode

img = qrcode.make("https://youtu.be/yfOmQ0Zln6Y")
img.save("qrcode-Camina-Drummer-speech.png")

img = qrcode.make("https://chezsoi.org/lucas/jdr/ParadisPerdu/acte-1/")
img.save("qrcode-terminal-acte-1.png")

img = qrcode.make("https://chezsoi.org/lucas/jdr/ParadisPerdu/acte-2/")
img.save("qrcode-terminal-acte-2.png")
