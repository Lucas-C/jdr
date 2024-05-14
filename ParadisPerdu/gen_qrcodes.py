#!/usr/bin/env python3
# Script Dependencies:
#    qrcode
import qrcode

img = qrcode.make("https://youtu.be/yfOmQ0Zln6Y")
img.save("qrcode-Camina-Drummer-speech.png")
