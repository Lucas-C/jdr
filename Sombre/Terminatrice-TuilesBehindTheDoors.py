#!/usr/bin/env python3
# Idées de liens entre PJs :
# * [x] il t'a trahi
# * [x] relation familiale
# * [x] (secret) il a plein de fric
# * [x] (secret) il a été mordu
# * [x] il t'a / vous a sauvé
# * [x] a tué un proche devenu zombie
# * anciens collègues / voisins ?
import asyncio, logging, sys
from dataclasses import replace
from threading import Timer

from fpdf import FPDF
from fpdf.table import Table
from livereload.watcher import get_watcher_class
from xreload import xreload


VERTI_MARGIN = 15
HORIZ_MARGIN = 28.5
CELL_SIZE = 60
LINE_HEIGHT = 5


def gen_pdf():
    pdf = FPDF(orientation="landscape")
    pdf.set_margin(VERTI_MARGIN)
    pdf.set_left_margin(HORIZ_MARGIN)
    pdf.set_right_margin(HORIZ_MARGIN)
    pdf.set_font("Helvetica", size=8)
    pdf.add_page()
    with pdf.rotation(90, x=23, y=pdf.h/2):
        pdf.text(x=-60, y=pdf.h/2, txt="Lucas Cimon 2023 - Personnages alternatifs pour le scénario Behind the Doors de Julien « DeathAmbre » De Monte, pour Sombre")
    table_kwargs = dict(first_row_as_headings=False, markdown=True, line_height=LINE_HEIGHT, width=2*CELL_SIZE)
    table = TableWithStaticRowHeights(pdf, align="LEFT", **table_kwargs)
    row = table.row()
    render_cell_front(pdf, row, "Brad", "Businessman glacial", i=0, j=0)
    render_cell_back(pdf, row, """\
Tu es le frère aîné de Dany, que tu as secouru à son lycée.

Les zombies, tu gères, mais tu flippes d'avoir perdu tout ce que tu possédais...

Hier, par peur de crever en retournant les aider, tu as prétendu que Chris & Mickey s'étaient fait chopper.
""")
    row = table.row()
    render_cell_front(pdf, row, "Chris", "Gangsta latino", i=0, j=1)  # Sonia
    render_cell_back(pdf, row, """\
Tu as un gros paquet de cash sur toi. Stan l'a vu, et tu lui en as promis la moitié s'il l'a bouclait.

Lors de la fuite du centre commercial, cette raclure de Brad t'a abandonné en arrière avec Mickey, et a prétendu que vous étiez morts.""")
    row = table.row()
    render_cell_front(pdf, row, "Dany", "Skater ado", i=0, j=2)  # Julie
    render_cell_back(pdf, row, """\
Brad est ton grand frère, il est venu te chercher au lycée pour te sauver.

Quand tu recroisé ta copine Jess zombifiée, tu étais pétrifié. Mickey t'a sauvé, en la butant sous tes yeux.

Tu sais que Stan a été mordu, mais il t'a dit que c'était une coupure.
""")
    table.render()
    pdf.y = pdf.t_margin
    table = TableWithStaticRowHeights(pdf, align="RIGHT", **table_kwargs)
    row = table.row()
    render_cell_front(pdf, row, "Mickey", "Éboueur musclé", i=1, j=0)
    render_cell_back(pdf, row, """\
Lors de la fuite du centre commercial, cette raclure de Brad t'a abandonné en arrière avec Chris, et a prétendu que vous étiez morts.

C'est grâce à toi que vous êtes là, et que l'hélico vous attend.

Tu es un peu raciste. Tu penses que le virus vient des immigrés.""")
    row = table.row()
    render_cell_front(pdf, row, "Stan", "Laborantin noir", i=1, j=1)
    render_cell_back(pdf, row, """\
Tu as été mordu au bras, tu es foutu. Dany a vu la blessure, mais tu lui as dit que c'était une simple coupure.

Chris a un paquet de cash sur lui, il t'en a promis la moitié si tu la bouclais.

Le sang-froid de Brad t'impressionne et te fait flipper à la fois.
""")
    table.render()
    render_memo(pdf)
    pdf.output("Terminatrice-TuilesBehindTheDoors.pdf")
    print("PDF written")

def render_cell_front(pdf, row, name, desc, i=0, j=0):
    pdf.set_font(size=24, style="")
    row.cell(f"**{name}**", align="C")
    pdf.set_font(size=14, style="I")
    prev_x, prev_y = pdf.x, pdf.y
    pdf.set_xy(HORIZ_MARGIN + (2 * i + .5) * CELL_SIZE, VERTI_MARGIN + (j + .666) * CELL_SIZE)
    pdf.cell(h=LINE_HEIGHT, txt=desc, align="X")
    pdf.set_xy(prev_x, prev_y)

def render_cell_back(pdf, row, text):
    pdf.set_font(size=9, style="")
    row.cell("\n" + text, align="C")

def render_memo(pdf):
    pdf.image("logo-sombre.png", x=238, y=138, w=30)
    pdf.set_xy(153, 144)
    pdf.set_font(size=9)
    pdf.multi_cell(w=0, h=LINE_HEIGHT, markdown=True, txt="""\
* Tous sont de score 3, armés, et savent tirer
* Dès qu'un PJ en **braque** un autre, le jeu **se fige** : chaque joueur est libre d'annoncer s'il en cible un autre, puis 1-2-3 et on lance les dés
* **RICOCHETS** : en cas de tir raté, les dégâts sont appliqués au tour suivant, si le tireur est vivant, en les lisant sur la face inverse du dé
* Il est possible de **détourner** un flingue vers une autre cible, en faisant une réussite supérieure au jet du tireur
* à **4 joueurs**, on retire Mickey : il a été rattrapé juste avant l'ascenseur
* Mickey les a tous sauvé : il a réussi à contacter l'armée puis à les mener ici. À **4 joueurs**, on l'enlève : les zombies l'ont eu juste avant l'ascenseur
* Chris & Dany peuvent être des personnages féminins
""")


class TableWithStaticRowHeights(Table):
    def _get_row_layout_info(self, i):
        row_layout_info = Table._get_row_layout_info(self, i)
        return replace(row_layout_info, height=CELL_SIZE)


async def main():
    logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.getLogger('livereload').setLevel(logging.INFO)
    watcher = get_watcher_class()()
    watcher.watch(__file__, gen_pdf)
    print("Watcher started...")
    await watch_periodically(watcher)

async def watch_periodically(watcher):
    watcher.examine()
    await asyncio.sleep(.8)
    xreload(sys.modules[__name__], new_annotations={"XRELOADED": True})
    await asyncio.create_task(watch_periodically(watcher))


if not __annotations__.get("XRELOADED"):
    gen_pdf()
    if '--watch' in sys.argv:
        asyncio.run(main())
