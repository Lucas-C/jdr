#!/usr/bin/env python3
from os import chdir
from os.path import dirname
from fpdf import FPDF, TextStyle
from mistletoe import markdown

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
add_image("jet_the_hawk_gijinka_by_rosytoonz_cc-by.png")
add_image("zuko_fanart_by_codethecod_cc-by.jpg")
add_image("liadlaw_illustration_by_phantomrhey_cc-by.jpg")
add_image("Ashitaka_Princess_Mononoke_by_amazingsphelon_cc-by-sa.png")

pdf.add_page()
add_image("BR-Portrait-Erika-POKEMON_by_amazingsphelon_cc-by-sa.jpg")
add_image("OC_raffle_Rianna_by_amazingsphelon_cc-by-sa.jpg")
add_image("Charlenne_by_amazingsphelon_cc-by-sa.jpg")

pdf.add_page()
add_image("akane_uzumaki_c2_by_whiterabbit20_cc-by.png")
add_image("frida_by_whiterabbit20_cc-by.png")
add_image("kasumi_by_whiterabbit20_cc-by.png")
add_image("namiko_hayashi_by_whiterabbit20_cc-by.png")

pdf.add_page()
add_image("cm_naruto_by_whiterabbit20_cc-by.png")
add_image("oc_naruto_by_whiterabbit20_cc-by.png")
add_image("shinku_by_whiterabbit20_cc-by.png")
add_image("quick_samurai_sketch_by_hidanbasher_cc-by.png")

pdf.add_page()
add_image("Miashe_blare_the_fiery_fighter_blaziken_by_amazingsphelon_cc-by-sa.jpg")
add_image("OC-Naiya-Creswell_by_amazingsphelon_cc-by-sa.jpg")
add_image("OC-Raid-Northgain_by_amazingsphelon_cc-by-sa.jpg")

# PNJs :
pdf.add_page()
add_image("Dakuan_by_daudiomultimedia_cc-by-nc.png")
add_image("TCP-Manimal-3-cc-by.jpg")
add_image("Kenku-by-ubergank-cc-by-sa.jpg")
add_image("komainu_raican_by_hijodelopio_cc-by.png")

pdf.add_page()
add_image("league_of_legends_shen_blood_moon_by_spellshuei_cc-by.jpg")
add_image("pixabay-kitty.png")

pdf.add_page()
add_image("Mind-Temple-Character_by_assumzaek_cc-by-nc-sa.png")
add_image("iaeto_by_bananascholar_cc-by-nc.png")
add_image("a_spriggan_by_kentovelindstrom_cc-by.png")
add_image("wtactics-DarkManaBreather-cc-by-sa.png")

# Colosses
pdf.add_page()
add_image("a_study_in_golems_3_by_skorble_cc-by-nc-sa.png")
add_image("a_study_in_golems_6_by_skorble_cc-by-nc-sa.png")
add_image("tiny_the_stone_giant__ice__by_halycon450_cc-by-nc-sa.png")
add_image("warforged_by_halycon450_cc-by-nc-sa.png")

# Lieux
pdf.add_page()
add_image("fisherman_s_house_by_assumzaek_cc-by-nc-sa.jpg")
add_image("village_by_assumzaek_cc-by-nc-sa.jpg")
pdf.image("cc-imgs/Lanterns-in-the-Sky_by_desmondwoot_cc-by-nc-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

pdf.add_page()
pdf.image("cc-imgs/skyriders_by_desmondwoot_cc-by-nc-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)
pdf.ln(30)
pdf.image("cc-imgs/gone_fishing_by_desmondwoot_cc-by-nc-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

# Objets spéciaux :
pdf.add_page()
add_image("Katanas_by_Halibutt_cc-by.svg")
add_image("Bow-and-Arrow-cc0.png")
pdf.ln(20)
add_image("freesvg-red-chinese-scroll.svg")
add_image("freesvg-asian-fan-with-a-map.svg")

pdf.add_page()
pdf.image("cc-imgs/Woodland-Dragon_by_flaming-anubis_cc-by-sa.jpg", h=IMG_SIZE, w=pdf.epw, keep_aspect_ratio=True)

pdf.add_page()
pdf.set_font("Helvetica", size=12)
pdf.write_html(markdown("""
Origine des illustrations :

- [Ashitaka | Princess Mononoke](https://www.deviantart.com/amazingsphelon/art/Ashitaka-Princess-Mononoke-714136981), [Miashe Blare - The Fiery Fighter Blaziken](https://www.deviantart.com/amazingsphelon/art/OC-Miashe-Blare-The-Fiery-Fighter-Blaziken-853747260), [Naiya Creswell](https://www.deviantart.com/amazingsphelon/art/OC-Naiya-Creswell-953963034), [Rianna](https://www.deviantart.com/amazingsphelon/art/OC-Raffle-Rianna-883029312), [Charlenne](https://www.deviantart.com/amazingsphelon/art/Commission-Charlenne-978385892), [Raid Northgain](https://www.deviantart.com/amazingsphelon/art/OC-Raid-Northgain-953964022), [Portrait: Erika POKEMON par AmazingSphelon](https://www.deviantart.com/amazingsphelon/art/BR-Portrait-Erika-POKEMON-926336867) - [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- [CC BY-SA 2.0](https://creativecommons.org/licenses/by-sa/2.0/)
- [Komainu Raican](https://www.deviantart.com/hijodelopio/art/Komainu-Raican-878188481) & [Kuma par HIJODELOPIO](https://www.deviantart.com/hijodelopio/art/Kuma-878189196) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Fisherman's House](https://www.deviantart.com/assumzaek/art/Fisherman-s-House-657583300), [Mind Temple Character](https://www.deviantart.com/assumzaek/art/Mind-Temple-Character-831961386) & [Village par assumzaek](https://www.deviantart.com/assumzaek/art/Village-630261499) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [Dakuan Ninja Scroll par DaudioMultimedia](https://www.deviantart.com/daudiomultimedia/art/Dakuan-Ninja-Scroll-784761566) - [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/)
- [Kenku par Ubergank](https://www.deviantart.com/ubergank/art/Kenku-814005528) - [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- [Iaeto par BananaScholar](https://www.deviantart.com/bananascholar/art/ArtFight-2024-9-Iaeto-1072574039) - [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/)
- [League of Legends - Shen / Blood Moon par Spellshuei](https://www.deviantart.com/spellshuei/art/League-of-Legends-Shen-Blood-Moon-296075743) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Zuko fanart par CodeTheCod](https://www.deviantart.com/codethecod/art/Zuko-fanart-902243721) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Gone fishing](https://www.deviantart.com/desmondwoot/art/Gone-fishing-404429653), [Lanterns in the Sky](https://www.deviantart.com/desmondwoot/art/Lanterns-in-the-Sky-357624151) & [Skyriders par Desmond Wong](https://www.deviantart.com/desmondwoot/art/Skyriders-465317507) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [A Study in Golems 3](https://www.deviantart.com/skorble/art/A-Study-in-Golems-3-937419597) & [6 par Skorble](https://www.deviantart.com/skorble/art/A-Study-in-Golems-6-937419622) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [Tiny Tiny, the Stone Giant (Ice)](https://www.deviantart.com/halycon450/art/Tiny-the-Stone-Giant-Ice-392725495) & [Warforged par Halycon450](https://www.deviantart.com/halycon450/art/Warforged-506567841) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [A Spriggan par Kent-Ove Lindstrom](https://www.deviantart.com/kentovelindstrom/art/A-Spriggan-936085738) - [CC BY](https://creativecommons.org/licenses/by/3.0/)
- [Akane Uzumaki v2](https://www.deviantart.com/whiterabbit20/art/comission-Akane-Uzumaki-version-2-612115455), [Frida](https://www.deviantart.com/whiterabbit20/art/COM-Frida-643533882), [Kasumi](https://www.deviantart.com/whiterabbit20/art/commission-Kasumi-782510344), [Namiko Hayashi](https://www.deviantart.com/whiterabbit20/art/Commission-Namiko-Hayashi-589770422), [CM: Naruto](https://www.deviantart.com/whiterabbit20/art/CM-Naruto-746253389), [Oc Naruto](https://www.deviantart.com/whiterabbit20/art/commission-Oc-Naruto-782507783) & [Shinku par whiterabbit20](https://www.deviantart.com/whiterabbit20/art/Shinku-477460279) - [CC BY](https://creativecommons.org/licenses/by/3.0/)
- [Woodland dragon par flaming-anubis](https://www.deviantart.com/flaming-anubis/art/Woodland-Dragon-461654140) - [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- [Dark Mana Breather par Santiago Iborra (wtactics)](https://github.com/wtactics/art) - [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- [Armored & Manimal 3 par Jeff Preston](http://team-preston.com) issu de [108 Terrible Character Portraits](https://www.drivethrurpg.com/product/91360/108-Terrible-Character-Portraits) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Liadlaw Illustration by PhantomRhey](https://www.deviantart.com/phantomrhey/art/Liadlaw-Illustration-978581143) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Elf Druide Fantaisie](https://pixabay.com/illustrations/elf-druid-fantasy-fantasy-character-2044697/), [Kitty Anime Poilu Bleu](https://pixabay.com/illustrations/kitty-anime-furry-blue-cat-robe-1374728/)
& [Shuriken Throwing Ninja Star](https://pixabay.com/fr/vectors/shuriken-lancer-des-%C3%A9toiles-153172/) @ pixabay.com
- [Ombrelle @ pxhere.com](https://pxhere.com/en/photo/700898) - CC0
- [Bow and arrow vector drawing @ publicdomainvectors.org](https://publicdomainvectors.org/en/free-clipart/Bow-and-arrow-vector-drawing/74403.html) - domaine public
- [Grapling hook par Pearson Scott Foresman](https://commons.wikimedia.org/wiki/File:Grappling_hook_2_(PSF).png) - domaine public
- [Asian fan with a map](https://freesvg.org/asian-fan-with-a-map-vector-image) & [Red Chinese scroll](https://freesvg.org/red-chinese-scroll) @ freesvg.org - domaine public
"""), tag_styles={
    "li": TextStyle(t_margin=5, b_margin=5),
})

out_filepath = "OriMushi-Illustrations.pdf"
pdf.output(out_filepath)
print(f"{out_filepath} generated")
