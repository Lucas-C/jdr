#!/usr/bin/env python3
# Script Dependencies:
#    fpdf2
#    livereload
#    xreload
import asyncio, sys
from pathlib import Path

from fpdf import FPDF

DIR = Path(__file__).parent

sys.path.append(str(DIR / ".."))  # make render_utils.py importable
from render_utils import iter_tile_pos, render_img_tile, start_watch_and_rebuild, LINE_HEIGHT, TILE_SIZE

VERTI_MARGIN = 15
HORIZ_MARGIN = 28.5


def build_pdf():
    pdf = FPDF(orientation="landscape")
    pdf.set_margin(VERTI_MARGIN)
    pdf.l_margin = pdf.r_margin = HORIZ_MARGIN
    pdf.set_font("Helvetica", size=8)
    pdf.add_page()
    with pdf.rotation(90, x=23, y=pdf.h/2):
        pdf.text(x=-60, y=pdf.h/2, txt="Lucas Cimon 2023 - Personnages alternatifs pour le scénario Behind the Doors de Julien « DeathAmbre » De Monte, pour Sombre")
    tpi = iter_tile_pos(pdf)  # Tiles Positions Iterator
    render_tile_front(tpi, "Brad", "Businessman glacial")
    render_tile_back(tpi, """\
Tu es le frère aîné de Dany, que tu as secouru à son lycée.

Les zombies, tu gères, mais tu flippes d'avoir perdu tout ce que tu possédais...

Hier, par peur de crever en retournant les aider, tu as prétendu que Chris & Mickey s'étaient fait chopper.""")
    render_tile_front(tpi, "Mickey", "Éboueur musclé")
    render_tile_back(tpi, """\
Lors de la fuite du centre commercial, cette raclure de Brad t'a abandonné en arrière avec Chris, et a prétendu que vous étiez morts.

C'est grâce à toi que vous êtes là, et que l'hélico vous attend.

Tu es un peu raciste. Tu penses que le virus vient des immigrés.""")
    render_tile_front(tpi, "Chris", "Gangsta latino")  # Sonia
    render_tile_back(tpi, """\
Tu as un gros paquet de cash sur toi. Stan l'a vu, et tu lui en as promis la moitié s'il l'a bouclait.

Lors de la fuite du centre commercial, cette raclure de Brad t'a abandonné en arrière avec Mickey, et a prétendu que vous étiez morts.""")
    render_tile_front(tpi, "Stan", "Laborantin noir")
    render_tile_back(tpi, """\
Tu as été mordu au bras, si les autres le découvrent tu es foutu. Dany a vu la blessure, mais tu lui as dit que c'était une simple coupure.

Chris a un paquet de cash sur lui, il t'en a promis la moitié si tu n'en parlais à personne.
Peut-être qu'avec tout ce fric tu pourrais sauver ta peau...""")
    render_tile_front(tpi, "Dany", "Skater ado")  # Julie
    render_tile_back(tpi, """\
Brad est ton grand frère, il est venu te chercher au lycée pour te sauver.

Quand tu as recroisé ta copine Jess zombifiée, tu étais pétrifié. Mickey t'a sauvé, en la butant sous tes yeux.

Tu sais que Stan a été mordu, mais il t'a dit que c'était une coupure.""")
    render_memo(pdf)
    out_filepath = "Terminatrice-BehindTheDoors.pdf"
    pdf.output(DIR / out_filepath)
    print(f"{out_filepath} has been rebuilt")

def render_tile_front(tpi, name, desc):
    render_img_tile(tpi, DIR / "../SombreZero-Empty3.png", name, desc)

def render_tile_back(tpi, text):
    pdf, _, _ = next(tpi)
    pdf.set_font(size=9, style="")
    pdf.multi_cell(txt="\n" + text, align="C", border=1,
                   h=TILE_SIZE, w=TILE_SIZE, max_line_height=LINE_HEIGHT)

def render_memo(pdf):
    pdf.set_xy(153, 140)
    pdf.set_font(size=9)
    # \x95 = BULLET character in Windows-1252 encoding
    pdf.multi_cell(w=0, h=LINE_HEIGHT, markdown=True, txt="""\
\x95 Tous les personnages sont armés et savent tirer
\x95 Mickey les a tous sauvé : il a réussi à contacter l'armée puis à les mener ici. À **4 joueurs**, on l'enlève : les zombies l'ont eu juste avant l'ascenseur
\x95 Chris & Dany peuvent être des personnages féminins
\x95 Dès qu'un PJ en **braque** un autre, le jeu **se fige** : chaque joueur est libre d'annoncer s'il en cible un autre, puis 1-2-3 et on lance les dés
\x95 **RICOCHETS** : en cas de tir raté, les dégâts sont appliqués au tour suivant, si le tireur est vivant, en les lisant sur la face inverse du dé
\x95 Il est possible de **détourner** un flingue vers une autre cible, en faisant une réussite supérieure au jet du tireur
""")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], __file__))
