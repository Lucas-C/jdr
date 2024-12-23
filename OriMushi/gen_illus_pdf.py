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
add_image("cc-imgs/TCP-Human-4-cc-by.jpg")
add_image("cc-imgs/elf-cc0.png")
add_image("cc-imgs/Pirate-ninja-cc0.svg")
add_image("cc-imgs/quick_samurai_sketch_by_hidanbasher_cc-by.jpg")

pdf.add_page()
add_image("cc-imgs/Alopex_redesign_concept_by_beevirus_cc-by-nc-sa.jpg")
add_image("cc-imgs/Human_Alopex_by_beevirus_cc-by-nc-sa.jpg")
add_image("cc-imgs/ryzom-tryker-femme-cc-by-sa.jpg")
add_image("cc-imgs/ryzom-tryker-homme-cc-by-sa.jpg")

pdf.add_page()
add_image("cc-imgs/Breeze-in-the-Forest_by_tysontan_cc-by-sa.jpg")
add_image("cc-imgs/kitty-cc0.jpg")
add_image("cc-imgs/Lion-Swordsman-by-hijodelopio-cc-by.png")
add_image("cc-imgs/Shinobi-Saipat-by-hijodelopio-cc-by.jpg")

# PNJs :
pdf.add_page()
add_image("cc-imgs/Dakuan_by_daudiomultimedia_cc-by-nc.png")
add_image("cc-imgs/TCP-Manimal-3-cc-by.jpg")
add_image("cc-imgs/Kenku-by-ubergank-cc-by-sa.jpg")
add_image("cc-imgs/elias_ainsworth_the_ancient_magus_bride_by_amgr99_cc-by-sa.jpg")

# Objets spéciaux :
pdf.add_page()
add_image("cc-imgs/magic_circle_2_by_nnao_cc-by-nc-sa.jpg")
add_image("cc-imgs/western_kit_by_fernand0fc_cc-by.jpg")
add_image("cc-imgs/Grappling_hook-cc0.png")
add_image("cc-imgs/Katanas_by_Halibutt_cc-by.svg")

pdf.add_page()
add_image("cc-imgs/asian_paper_umbrella-cc0.jpg")
add_image("cc-imgs/TCP-Armored-3-cc-by.jpg")
add_image("cc-imgs/asian-fan-with-a-map-cc0.svg")
add_image("cc-imgs/shuriken-cc0.png")

pdf.add_page()
add_image("cc-imgs/red-chinese-scroll-cc0.svg")
add_image("cc-imgs/Bow-and-Arrow-cc0.png")
pdf.image("cc-imgs/Woodland-Dragon_by_flaming-anubis_cc-by-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

out_filepath = "OriMushi-illustrations.pdf"
pdf.output(out_filepath)
print(f"{out_filepath} generated")
