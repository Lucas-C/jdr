#!/usr/bin/env python3
from typing import NamedTuple

from fpdf import FPDF
from fpdf.util import convert_unit

# Poker card format: 62.992 x 87.884mm (2.48" x 3.46")
CARD_WIDTH = convert_unit(2.48, "in", "mm")
CARD_HEIGHT = convert_unit(3.46, "in", "mm")

class Card(NamedTuple):
    title: str
    img: str
    desc: str = ""
    img_keep_ratio: bool = False
    img_shrink: bool = False
    white_bg: bool = False

def render_card(pdf, card, i, j, gutter=0, border=3):
    # Render background:
    x = pdf.l_margin+i*(CARD_WIDTH+gutter)
    y = pdf.t_margin+j*(CARD_HEIGHT+gutter)
    pdf.rect(x=x, y=y, w=CARD_WIDTH, h=CARD_HEIGHT, style="F", round_corners=True, corner_radius=5)
    # Render image:
    img_x, img_y = x+border, y+border
    w = CARD_WIDTH - 2*border
    h = CARD_HEIGHT - 2*border
    if card.white_bg:
        render_white_zone(pdf, x=img_x, y=img_y, w=w, h=h)
    if card.img_shrink:
        img_info = pdf.preload_image(card.img)[2]
        ratio = img_info["w"] / img_info["h"]
        h = 2/3*CARD_HEIGHT
        if h*ratio < w:
            w = h*ratio
        else:  # => too wide, limiting width:
            h = w/ratio
        img_x = x + (CARD_WIDTH - w)/2
        img_y += CARD_HEIGHT/6
    pdf.image(card.img, x=img_x, y=img_y, w=w, h=h)
    # Render title:
    pdf.set_font("Outage", size=12)
    render_text_zone(pdf, card.title, x=x+2*border, y=y+2*border, h=6, border=border)
    if card.desc:  # Render description:
        y = y+4/5*CARD_HEIGHT
        h = CARD_HEIGHT/5-2*border
        font_size = 10
        lines_count = len(card.desc.splitlines())
        assert lines_count <= 3  # else, not suppported yet
        if lines_count == 3:
            font_size = 8
            y -= 3
            h += 6
        pdf.set_font("Helvetica", size=font_size)
        render_text_zone(pdf, card.desc, x=x+2*border, y=y, h=h, border=border)

def render_text_zone(pdf, text, x, y, h, border):
    w = CARD_WIDTH - 4*border
    render_white_zone(pdf, x=x, y=y, w=w, h=h, opacity=.6)
    pdf.set_xy(x=x, y=y+h/10)
    pdf.multi_cell(txt=text, w=w, h=5, align="C")

def render_white_zone(pdf, x, y, w, h, opacity=1):
    with pdf.local_context(fill_color=255, fill_opacity=opacity):
        pdf.rect(x=x, y=y, w=w, h=h, style="FD", round_corners=True, corner_radius=h)

def render_cards(pdf, cards):
    while True:
        pdf.add_page()
        for j in range(3):
            for i in range(3):
                render_card(pdf, cards.pop(0), i=i, j=j)
                if not cards:
                    return

pdf = FPDF(format="A4", unit="mm")
pdf.add_font(fname="../fonts/Outage.ttf")
pdf.set_margins(10, 15)
pdf.set_draw_color(0)
cards = [
    # Skins:
    Card(title="Argos", img="../avatars/bodies/argos_argos2.png", img_shrink=True, white_bg=True),
    Card(title="Artemis", img="../avatars/bodies/artemis.png", img_shrink=True, white_bg=True),
    Card(title="Astartes", img="../avatars/bodies/astartes_dead2.png", img_shrink=True, white_bg=True),
    Card(title="Azrael", img="../avatars/bodies/azrael_detox.png", img_shrink=True, white_bg=True),
    Card(title="Sonata", img="../avatars/bodies/crakho_sandra.png", img_shrink=True, white_bg=True),
    Card(title="Jarek", img="../avatars/bodies/bitterman_jarek.png", img_shrink=True, white_bg=True),
    Card(title="Cruentus", img="../avatars/bodies/cruentus_pahd.png", img_shrink=True, white_bg=True),
    Card(title="Dragonito", img="../avatars/bodies/dragonito_ignatius.png", img_shrink=True, white_bg=True),
    Card(title="Persona", img="../avatars/bodies/pms.png", img_shrink=True, white_bg=True),
    # Generic:
    Card(title="Maitrise de la Map", img="../illustrations/tis1451-doom-slayer-cc-by-sa.jpg", desc="Vous contrôlez ce niveau"),
    Card(title="Interagir", img="./interactivity-icon-cursor.png", img_shrink=True, white_bg=True),
        # TODO: use/hand/E
    # Power-ups:
    Card(title="Haste", img="./haste.webp", desc="Vous vous déplacez\n2x plus vite"),
    # Weapons:
    Card(title="Epee", img="../weapons/SWORD-from-wandering_by_fernand0fc_cc-by.png", desc="Dégats: 1", img_shrink=True, white_bg=True),
    Card(title="Lightgun", img="./gauss_rifle_by_fernand0fc_cc-by-nc.png", desc="Dégats: 2", img_shrink=True, white_bg=True),
    Card(title="Railgun", img="./lazer_rifle_by_fernand0fc_cc-by.png", desc="Dégats: 6", img_shrink=True, white_bg=True),
    Card(title="Lance-roquette", img="./10_weapon-rocketlauncher-back.webp", img_shrink=True, white_bg=True),
    Card(title="Sac a dos", img="./backpack-cc0.webp", img_shrink=True, white_bg=True),
    # Bots:
    Card(title="Double Chainsaw", img="./Robot_by_c1rruscl0ud_cc-by-sa.jpg", desc="* attaque le PJ le + proche\n* si équidistants, le + blessé\n* si sa cible fuit, la poursuit"),
    Card(title="Strogg", img="../illustrations/Strogg_by_tarakanovich-cc-by.jpg", desc="* arpente le niveau en boucle\n* attaque à distance\n* pas capable de remonter l'échelle"),
    Card(title="Numerian", img="./beeple01-cc-by_whodrewthis-Numerian-Scav-Sniper-cc-by.jpg"),
    Card(title="Andro", img="./beeple02-cc-by_whodrewthis-Robot-Security-cc-by.jpg"),
    # Devlogs:
]
render_cards(pdf, cards)
pdf.output("wakeIII-cards.pdf")
