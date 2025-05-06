#!/usr/bin/env python3
# Script Dependencies:
#    fpdf2
#    livereload
#    xreload
import asyncio, sys
from pathlib import Path

from fpdf import FPDF

DIR = Path(__file__).parent

sys.path.append(str(DIR / ".." / ".."))  # make pdf_utils.py importable
from pdf_utils import start_watch_and_rebuild
sys.path.append(str(DIR / ".."))  # make render_utils.py importable
from render_utils import iter_tile_pos, render_img_tile

VERTI_MARGIN = 40
HORIZ_MARGIN = 28.5


def build_pdf(target_md_file=None):
    pdf = FPDF(orientation="landscape")
    pdf.set_margin(VERTI_MARGIN)
    pdf.set_left_margin(HORIZ_MARGIN)
    pdf.set_right_margin(HORIZ_MARGIN)
    pdf.set_font("Helvetica", size=20)
    pdf.add_page()
    tpi = iter_tile_pos(pdf)  # Tiles Positions Iterator
    render_img_tile(tpi, DIR / "../SombreZero-Empty3.png", "Sergio")
    render_img_tile(tpi, DIR / "../SombreZero-Empty3.png", "Delilah")
    render_img_tile(tpi, DIR / "../SombreZero-Empty3.png", "William")
    render_img_tile(tpi, DIR / "../SombreZero-Empty3.png", "Michelle")
    render_img_tile(tpi, DIR / "../SombreZero-Empty3.png", "Benett")
    pdf.set_font(size=10)
    pdf.set_xy(pdf.w/2, 165)
    pdf.cell(align="X", text="Lucas Cimon 2023 - Tuiles personnages pour le scénario Out Of Reach de Julien « DeathAmbre » De Monte, pour Sombre")
    out_filepath = "Terminatrice-OutOfReach.pdf"
    pdf.output(DIR / out_filepath)
    print(f"{out_filepath} has been rebuilt")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], __file__))
