#!/usr/bin/env python3
from os import chdir
from os.path import dirname
from fpdf import FPDF

IMG_SIZE = 97

chdir(dirname(__file__))
pdf = FPDF(format="letter")
pdf.set_margin(10)

def add_image(path):
    x, y = pdf.x, pdf.y
    info = pdf.image(path, h=IMG_SIZE, w=IMG_SIZE, keep_aspect_ratio=True)
    if x + info.rendered_width < pdf.w / 2:
        pdf.x = pdf.w / 2
        pdf.y = y
    else:
        pdf.x = pdf.l_margin
        pdf.y += 10

# PJs :
pdf.add_page()
add_image("TCP-Human-4.jpg")
add_image("elf-2044697_1920.png")
add_image("Ninja-2.svg")
add_image("quick_samurai_sketch_by_hidanbasher_d9d8uez-fullview.jpg")
pdf.add_page()
add_image("alopex_redesign_concept_by_beevirus_d83o769-fullview.jpg")
add_image("d8uihey-ccf04f05-a980-4b1b-b904-0137e609e661.jpg")
add_image("ryzom-rd-pe-tr-pi-2000-12-12.jpg")
add_image("ryzom-rd-pe-tr-pi-2001-1-15.jpg")
pdf.add_page()
add_image("d5fhek0-e925c6be-09e3-4710-81d9-1b12e7b73900.jpg")
add_image("kitty-1374728_1920.jpg")
# PNJs :
add_image("dakuan.png")
add_image("TCP-Manimal-3.jpg")
pdf.add_page()
# Objets spéciaux :
add_image("magic_circle_2_by_nnao_d3kqddk-fullview.jpg")
add_image("western_kit_by_fernand0fc_ddhn18x-fullview.jpg")
add_image("Grappling_hook_2_(PSF).png")
add_image("Katanas.svg")
pdf.add_page()
add_image("screen_chinese_screen_china_japan_japanese_screen_asia_asian_umbrella_paper_umbrella-700898.jpg!d.jpg")
add_image("TCP-Armored-3.jpg")
add_image("j4p4n_Asian_Fan_with_a_map_-_1890.svg")
add_image("shuriken-153172_1280.png")
pdf.add_page()
pdf.image("Chinese-symbol-on-red-scroll-remix.svg", h=IMG_SIZE, w=IMG_SIZE, keep_aspect_ratio=True)
# add_image("Bow-and-Arrow.svg")
pdf.image("d7muum4-4766980a-f9e5-4baa-b39d-4abd0cb284fc.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

out_filepath = "OriMushi-illustrations.pdf"
pdf.output(out_filepath)
print(f"{out_filepath} generated")
