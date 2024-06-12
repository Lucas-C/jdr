#!/usr/bin/env python3
# TODO: generate a printer-friendly / text-only version without appendix nor any images
# Script Dependencies:
#    beautifulsoup4
#    fpdf2
#    livereload
#    mistletoe
#    pikepdf
#    pypdf
#    weasyprint
#    xreload
import asyncio, io, logging, sys
from pathlib import Path
from time import perf_counter

from fpdf import FPDF
from fpdf.enums import Align
from fpdf.image_parsing import preload_image
from pypdf import PdfMerger

DIR = Path(__file__).parent

logging.getLogger("fontTools.subset").level = logging.WARN  # avoid useless verbose logging
sys.path.append(str(DIR / ".." / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild
sys.path.append(str(DIR / ".."))  # make render_utils.py importable
from render_utils import iter_tile_pos, render_img_tile, LINE_HEIGHT, TILE_SIZE

MD_FILEPATH = DIR / "README.md"
CSS_FILEPATH = DIR / "style.css"
PLAN_FILEPATH = DIR / "tiles/FullPlan.jpg"
OUT_FILEPATH = DIR / "Sombre-LabEscape.pdf"
IMG_PER_NAME = {
    "Damian": "fargo_by_fernand0fc_dbd7gj6-portrait.png",
    "Markus": "JustinNichol-PP2-portrait.png",
    "Hanh": "JustinNichol-PP3-portrait.png",
    "Stacey": "numero9_by_thesimplylexi-595642973-portrait.png",
    "Hadley": "mccaul_lombardi_by_thesimplylexi_dca3dus-portrait.png",
}
SCALE = .12  # mm / pixel


def build_pdf():
    start = perf_counter()
    merger = PdfMerger()
    merger.append(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH))
    merger.append(build_appendix_pdf())
    merger.write(OUT_FILEPATH)
    set_metadata(OUT_FILEPATH,
        title="Sombre - Lab Escape",
        keywords=("jdr", "ttrpg", "sombre", "horror", "scenario"),
        description="Un scénario Sombre Zéro pour 3 à 5 joueurs, d'une durée d'environ 45min, dans un laboratoire envahi de zombies, avec une part d'exploration, les lieux étant progressivement révélés aux joueurs.",
    )
    print(f"{OUT_FILEPATH} has been rebuilt in {perf_counter() - start:.1f}s")


def build_appendix_pdf():
    pdf = FPDF()
    pdf.oversized_images = "DOWNSCALE"
    render_character_tiles(pdf)
    render_other_tiles(pdf)
    pdf.oversized_images = None
    render_room_tiles(pdf)
    # Plan full-page:
    pdf.b_margin = pdf.t_margin = 12
    pdf.add_page(orientation="landscape")
    pdf.image(PLAN_FILEPATH, h=pdf.eph, w=pdf.epw, keep_aspect_ratio=True)
    bytes_io = io.BytesIO()
    pdf.output(bytes_io)
    return bytes_io


def render_character_tiles(pdf):
    pdf.set_margin(28.5)  # vertical margin
    pdf.l_margin = pdf.r_margin = 15  # horizontal margin
    pdf.set_font("Helvetica", size=8)
    pdf.add_page()
    tpi = iter_tile_pos(pdf, columns=3, rows=4)  # Tiles Positions Iterator
    render_tile_front(tpi, "Damian", "Racket")
    render_img_tile(tpi, DIR / "portraits" / IMG_PER_NAME["Damian"], border=True)
    render_tile_back(tpi, """\
Tu caches sur toi un **surin**, un poignard que tu as bricolé. Tu peux le révéler quand tu veux.

Tu trouves Stacey sacrément mignonne.

Par contre le garde, Hadley, a une dent contre toi... Faut t'en méfier.
""")
    render_tile_front(tpi, "Markus", "Trafic de stups")
    render_img_tile(tpi, DIR / "portraits" / IMG_PER_NAME["Markus"], border=True)
    render_tile_back(tpi, """\
Au mitard, tu as accepté un contrat : tu dois exfiltrer des données confidentielles de ce labo. Il faut que tu mettes la main dessus avant de te barrer d'ici. Un type nommé Herman devait te les filer.

**In Extremis** : une fois par partie, transforme le résultat du dé en 1 pour obtenir une réussite de justesse.""")
    render_tile_front(tpi, "Hanh", "Escroquerie")
    render_img_tile(tpi, DIR / "portraits" / IMG_PER_NAME["Hanh"], border=True)
    render_tile_back(tpi, """\
__Shit__ ! Dans la panique, tu penses avoir été contaminé par un Infecté. Il doit bien y avoir un antidote quelque part ici !

__Fucking shit__ ! Des années que tu te tiens à carreau, et plus que 3 mois à tirer...

**Guigne** : une fois par partie, transforme le résultat du dé d'un autre joueur en 6.
""")
    render_tile_front(tpi, "Stacey", "Cambriolage")
    render_img_tile(tpi, DIR / "portraits" / IMG_PER_NAME["Stacey"], border=True)
    render_tile_back(tpi, """\
Vu les regards que te lance Damian, tu ne le laisse pas indifférent. Tu pourrais peut-être utiliser ça à ton avantage.

Toi, tu as plutôt le béguin pour Markus.

**Miraculée** : une fois par partie, les dommages que tu reçois sont réduits à 1""")
    pdf.add_page()
    tpi = iter_tile_pos(pdf, columns=3, rows=4)  # Tiles Positions Iterator
    render_tile_front(tpi, "Hadley", "Garde pénitentiaire")
    render_img_tile(tpi, DIR / "portraits" / IMG_PER_NAME["Hadley"], border=True)
    render_tile_back(tpi, """\
Tu te méfies de Damian, c'est un sournoi. Par contre Hanh est un détenu modèle, tu lui ferais presque confiance.

Tu as un **revolver**, et il te reste 3 balles.

Important : tes empreintes activent les serrures digitales de sécurité. Pas celles des détenus, bien sûr.""")
    render_tile_front(tpi, "Sujet #314", "Résistance", level=3)
    render_img_tile(tpi, DIR / "ZombieBruteNoShadow.png", border=True)
    render_img_tile(tpi, DIR / "items/Tuile-Revolver.jpg")
    render_tile_front(tpi, "Herman", "Biologiste", level=3)
    render_img_tile(tpi, DIR / "Herman.png", border=True)
    render_img_tile(tpi, DIR / "items/knife.png", border=True)
    render_img_tile(tpi, DIR / "items/pipe-wrench.png", border=True)
    render_img_tile(tpi, DIR / "items/fire-axe.png", border=True)
    render_img_tile(tpi, DIR / "items/Tuile-Hypodermics.jpg")

def render_tile_front(tpi, name, desc="", level=4):
    render_img_tile(tpi, DIR / f"../SombreZero-Empty{level}.png", name, desc)

def render_tile_back(tpi, text):
    pdf, _, _ = next(tpi)
    pdf.set_font(size=9, style="")
    pdf.multi_cell(text="\n" + text, markdown=True, align="C", border=1,
                   h=TILE_SIZE, w=TILE_SIZE, max_line_height=LINE_HEIGHT)


def render_other_tiles(pdf):
    pdf.set_margin(28.5)  # vertical margin
    pdf.l_margin = pdf.r_margin = 15  # horizontal margin
    pdf.set_font("Helvetica", size=8)
    pdf.add_page()
    tpi = iter_tile_pos(pdf, columns=3, rows=4)  # Tiles Positions Iterator
    render_tile_front(tpi, "Zombie", "Morsure : 1 Blessure", level=3)
    render_tile_front(tpi, "Zombie", "Morsure : 1 Blessure", level=3)
    render_tile_front(tpi, "Zombie", "Morsure : 1 Blessure", level=3)
    render_img_tile(tpi, DIR / "items/GasMask.png", border=True, w_ratio=.8)
    render_img_tile(tpi, DIR / "items/USB-thumb-drive-1.png", border=True, w_ratio=.5)
    render_img_tile(tpi, DIR / "items/car-keys.jpg", border=True, w_ratio=.5)
    render_img_tile(tpi, DIR / "items/Tuile-MetalPipe.jpg")
    render_img_tile(tpi, DIR / "items/Tuile-Medikit.jpg")
    render_img_tile(tpi, DIR / "items/Tuile-Munitions.jpg")


def render_room_tiles(pdf):
    pdf.add_font(fname="fonts/Freedom45.otf")
    pdf.set_font("Freedom45", size=12)
    pdf.set_margin(10)
    pdf.t_margin = 20

    pdf.add_page()
    add_side_by_side(pdf, "Laboratory-Corridor-1.jpg", "Laboratory-Corridor-2.jpg", border=True)
    pdf.text(x=34, y=19, text="2. Le couloir")
    pdf.y += 15
    add_side_by_side(pdf, "Laboratory-Garage-1.jpg", "Laboratory-Garage-2.jpg")
    pdf.text(x=18, y=171, text="8. Le garage")

    pdf.add_page()
    add_side_by_side(pdf, "Laboratory-Office-1.jpg", "Laboratory-Office-2.jpg")
    pdf.text(x=53, y=19, text="3. Le bureau")
    pdf.y += 20
    add_side_by_side(pdf, "Laboratory-WC-1.jpg", "Laboratory-WC-2.jpg")
    pdf.text(x=53, y=105, text="10. Les WCs")
    pdf.y += 20
    add_side_by_side(pdf, "Laboratory-Lab.jpg", shadow=True)
    pdf.text(x=36, y=194, text="9. Le petit labo")

    pdf.add_page()
    add_side_by_side(pdf, "Laboratory-SpecimensBench-1-short.jpg", "Laboratory-SpecimensBench-2-short.jpg")
    pdf.text(x=20, y=18, text="4. La salle des specimens")
    pdf.y += 15
    add_side_by_side(pdf, "Laboratory-Closet.jpg", shadow=True)
    pdf.text(x=63, y=203, text="6. La reserve")

    pdf.add_page()
    pdf.y += 20
    add_side_by_side(pdf, "Laboratory-ControlRoom-1.jpg", shadow=True)
    pdf.text(x=22, y=38, text="5. La cage d'escalier - etage")
    pdf.y += 30
    add_side_by_side(pdf, "Laboratory-ControlRoom-2.jpg", shadow=True)
    pdf.text(x=28, y=153, text="7. La cage d'escalier - RdC")

    pdf.add_page()
    pdf.y += 20
    add_top_bottom(pdf, "Laboratory-StorageRoom.jpg", shadow=True)
    pdf.text(x=53, y=90, text="1. L'entrepot")


def add_side_by_side(pdf, img1, img2=None, border=False, shadow=False):
    img1_width_mm, img1_height_mm = add_tile(pdf, img1, halign=Align.L)
    assert img1_width_mm < pdf.epw / 2, f"{img_width_mm} >= {pdf.epw/2}"
    if border:
        x = halign2x(Align.L, pdf, img1_width_mm)
        pdf.rect(x=x, y=pdf.y, w=img1_width_mm, h=img1_height_mm)
    if img2:
        img2_width_mm, img2_height_mm = add_tile(pdf, img2, halign=Align.R, valign_height=img1_height_mm)
        assert img2_width_mm < pdf.epw / 2, f"{img_width_mm} >= {pdf.epw/2}"
        if border:
            x = halign2x(Align.R, pdf, img2_width_mm)
            pdf.rect(x=x, y=pdf.y, w=img2_width_mm, h=img2_height_mm)
        vert_shift_mm = max(img1_height_mm, img2_height_mm)
    else:
        vert_shift_mm = img1_height_mm
        if shadow:
            x = halign2x(Align.R, pdf, img1_width_mm)
            pdf.rect(x=x, y=pdf.y, w=img1_width_mm, h=img1_height_mm)
    pdf.y += vert_shift_mm
    pdf.line(x1=pdf.w/2, y1=0, x2=pdf.w/2, y2=pdf.h)


def add_top_bottom(pdf, img1, shadow=False):
    img1_width_mm, img1_height_mm = add_tile(pdf, img1, halign=Align.C)
    pdf.y += img1_height_mm
    pdf.line(x1=0, y1=pdf.y, x2=pdf.w, y2=pdf.y)
    if shadow:
        x = halign2x(Align.C, pdf, img1_width_mm)
        pdf.rect(x=x, y=pdf.y, w=img1_width_mm, h=img1_height_mm)


def add_tile(pdf, img_filename, halign, valign_height=None):
    _, _, img_info = preload_image(pdf.image_cache, DIR / "tiles" / img_filename)
    img_width_mm = img_info.width * SCALE
    img_height_mm = img_info.height * SCALE
    if valign_height:
        pdf.y += (valign_height - img_height_mm) / 2
    x = halign2x(halign, pdf, img_width_mm)
    pdf.image(DIR / "tiles" / img_filename, x=x, y=pdf.y, w=img_width_mm, keep_aspect_ratio=True)
    return img_width_mm, img_height_mm


def halign2x(halign, pdf, img_width_mm):
    if halign == Align.L:
        return pdf.w/2 - img_width_mm
    if halign == Align.C:
        return pdf.w/2 - img_width_mm / 2
    if halign == Align.R:
        return pdf.w/2
    raise ValueError(f"Invalid halign: {halign}")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        SRC_FILES = (__file__, MD_FILEPATH, CSS_FILEPATH, PLAN_FILEPATH)
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
