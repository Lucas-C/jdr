#!/usr/bin/env python3
# Script Dependencies:
#    fpdf2
#    livereload
#    xreload
import asyncio, logging, sys
from pathlib import Path
from traceback import print_exc

from fpdf import FPDF
try:
    from livereload.watcher import get_watcher_class
    from xreload import xreload
    OPT_DEPS_LOADED = True
except ImportError:
    OPT_DEPS_LOADED = False

DIR = Path(__file__).parent
VERTI_MARGIN = 40
HORIZ_MARGIN = 28.5
TILE_SIZE = 60
LINE_HEIGHT = 5.25


def build_pdf():
    pdf = FPDF(orientation="landscape")
    pdf.set_margin(VERTI_MARGIN)
    pdf.set_left_margin(HORIZ_MARGIN)
    pdf.set_right_margin(HORIZ_MARGIN)
    pdf.set_font("Helvetica", size=22)
    pdf.add_page()
    table_kwargs = dict(first_row_as_headings=False, markdown=True, line_height=LINE_HEIGHT, width=4*TILE_SIZE)
    with pdf.table(align="LEFT", **table_kwargs) as table:
        row = table.row()
        render_tile(pdf, row, "Sergio", i=0, j=0)
        render_tile(pdf, row, "Delilah", i=1, j=0)
        render_tile(pdf, row, "William", i=2, j=0)
        render_tile(pdf, row, "Michelle", i=3, j=0)
        row = table.row()
        render_tile(pdf, row, "Benett", i=0, j=1)
        row.cell()
        row.cell()
        row.cell()
    pdf.set_font(size=10)
    pdf.set_xy(pdf.w/2, 165)
    pdf.cell(align="X", txt="Lucas Cimon 2023 - Tuiles personnages pour le scénario Out Of Reach de Julien « DeathAmbre » De Monte, pour Sombre")
    out_filepath = "Terminatrice-OutOfReach.pdf"
    pdf.output(DIR / out_filepath)
    print(f"{out_filepath} has been rebuilt")

def render_tile(pdf, row, name, i=0, j=0):
    row.cell(img=DIR / "../SombreZero-Empty3.png", img_fill_width=True)
    prev_x, prev_y = pdf.x, pdf.y
    pdf.set_xy(HORIZ_MARGIN + (i + .5) * TILE_SIZE, VERTI_MARGIN + (j + .25) * TILE_SIZE)
    pdf.cell(h=LINE_HEIGHT, align="X", markdown=True, txt=f"**{name}**")
    pdf.set_xy(prev_x, prev_y)


async def start_watch_and_rebuild():
    logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.getLogger("livereload").setLevel(logging.INFO)
    watcher = get_watcher_class()()
    watcher.watch(__file__, build_pdf)
    print("Watcher started...")
    await watch_periodically(watcher)

async def watch_periodically(watcher, delay_secs=.8):
    try:
        watcher.examine()
    except Exception:
        print_exc()
    await asyncio.sleep(delay_secs)
    xreload(sys.modules[__name__], new_annotations={"XRELOADED": True})
    await asyncio.create_task(watch_periodically(watcher))


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        if not OPT_DEPS_LOADED:
            raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
        asyncio.run(start_watch_and_rebuild())
