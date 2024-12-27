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
    info = pdf.image("cc-imgs/" + path, h=IMG_SIZE, w=IMG_SIZE, keep_aspect_ratio=True)
    if x + info.rendered_width < pdf.w / 2:
        pdf.x = pdf.w / 2
        pdf.y = y
    else:
        pdf.x = pdf.l_margin
        pdf.y += 10

# PJs :
pdf.add_page()
add_image("Aeshi_the_marvelous_maiden_gardevoir_by_amazingsphelon_cc-by-sa.jpg")
add_image("Miashe_blare_the_fiery_fighter_blaziken_by_amazingsphelon_cc-by-sa.jpg")
add_image("OC-Naiya-Creswell_by_amazingsphelon_cc-by-sa.jpg")
add_image("OC-Raid-Northgain_by_amazingsphelon_cc-by-sa.jpg")

pdf.add_page()
add_image("BR-Portrait-Erika-POKEMON_by_amazingsphelon_cc-by-sa.jpg")
add_image("OC_raffle_Rianna_by_amazingsphelon_cc-by-sa.jpg")
add_image("Charlenne_by_amazingsphelon_cc-by-sa.jpg")
add_image("Battle_Rehime_Sol_Badguy_by_amazingsphelon_cc-by-sa.jpg")

pdf.add_page()
add_image("Ashitaka_Princess_Mononoke_by_amazingsphelon_cc-by-sa.png")
add_image("Hanzo_Hatoori_The_fierceful_ninja_ninjask_by_amazingsphelon_cc-by-sa.jpg")
pdf.image("cc-imgs/Streets-on-Hazards-II-Martial-Arts-Attires_by_amazingsphelon_cc-by-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

pdf.add_page()
add_image("espio_the_chameleon_gijinka_cc-by.png")
add_image("jet_the_hawk_gijinka_by_rosytoonz_cc-by.png")
add_image("storm_the_albatross_gijinka_by_rosytoonz_cc-by.png")

pdf.add_page()
add_image("Alopex_redesign_concept_by_beevirus_cc-by-nc-sa.jpg")
add_image("Human_Alopex_by_beevirus_cc-by-nc-sa.jpg")
add_image("quick_samurai_sketch_by_hidanbasher_cc-by.png")

pdf.add_page()
add_image("ryzom-tryker-femme-cc-by-sa.jpg")
add_image("ryzom-tryker-homme-cc-by-sa.jpg")
add_image("elf-cc0.png")
add_image("pixabay-ninja-girl.png")

# PNJs :
pdf.add_page()
add_image("Dakuan_by_daudiomultimedia_cc-by-nc.png")
add_image("TCP-Manimal-3-cc-by.jpg")
add_image("Kenku-by-ubergank-cc-by-sa.jpg")
add_image("komainu_raican_by_hijodelopio_cc-by.png")

pdf.add_page()
add_image("kuma_by_hijodelopio_cc-by.png")
add_image("Lion-Swordsman-by-hijodelopio-cc-by.png")
add_image("Shinobi-Saipat-by-hijodelopio-cc-by-noBg.png")
add_image("kitty-cc0.png")

pdf.add_page()
add_image("Mind-Temple-Character_by_assumzaek_cc-by-nc-sa.png")
add_image("elias_ainsworth_the_ancient_magus_bride_by_amgr99_cc-by-sa.jpg")
add_image("Pirate-ninja-cc0.svg")

# Lieux
pdf.add_page()
add_image("fisherman_s_house_by_assumzaek_cc-by-nc-sa.jpg")
add_image("village_by_assumzaek_cc-by-nc-sa.jpg")

# Objets spéciaux :
pdf.add_page()
add_image("Katanas_by_Halibutt_cc-by.svg")
add_image("Grappling_hook-cc0.png")
pdf.ln(20)
add_image("shurikens-cc0.png")
add_image("Bow-and-Arrow-cc0.png")

pdf.add_page()
add_image("red-chinese-scroll-cc0.svg")
add_image("asian-fan-with-a-map-cc0.svg")
pdf.image("cc-imgs/Woodland-Dragon_by_flaming-anubis_cc-by-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

out_filepath = "OriMushi-illustrations.pdf"
pdf.output(out_filepath)
print(f"{out_filepath} generated")
