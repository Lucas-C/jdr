#!/usr/bin/env python3
# Script Dependencies:
#    beautifulsoup4
#    fpdf2
#    livereload
#    mistletoe
#    pypdf
#    weasyprint
#    xreload
import asyncio, io, logging, sys
from pathlib import Path

from fpdf import FPDF
from pypdf import PdfMerger

DIR = Path(__file__).parent

logging.getLogger("fontTools.subset").level = logging.WARN  # avoid useless verbose logging
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, watch_xreload_and_serve

MD_FILEPATH = DIR / "Pathfinder.md"
CSS_FILEPATH = DIR / "style.css"
OUT_FILEPATH = DIR / "Pathfinder.pdf"


def build_pdf():
    merger = PdfMerger()
    merger.append(character_sheet_pdf())
    merger.append(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH))
    merger.write(OUT_FILEPATH)
    print(f"{OUT_FILEPATH} has been rebuilt")


def character_sheet_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_margin(10)
    pdf.add_font(fname=DIR / "fonts/VinqueRegular.otf")
    pdf.set_font("VinqueRegular", size=24)
    pdf.image(DIR / "scrolls/frame.png", w=70)
    render_stats_block(pdf, "Athlétisme", x=100, y=15)
    render_stats_block(pdf, "Sagesse", x=156, y=15)
    render_stats_block(pdf, "Volonté", x=100, y=75)
    render_stats_block(pdf, "Dextérité", x=156, y=75)
    render_xp_block(pdf, x=5, y=114.5)
    render_equipment_block(pdf, x=82, y=194)
    render_side_stats_block(pdf, x=82, y=138)
    render_notes_reminder(pdf, x=8, y=273)
    bytes_io = io.BytesIO()
    pdf.output(bytes_io)
    return bytes_io

def render_stats_block(pdf, stat_name, x, y):
    pdf.x, pdf.y = x, y
    pdf.cell(text=stat_name, align="C", w=30)
    for i in range(4):
        pdf.image(DIR / "die-blank.svg", w=7, h=7, x=x + 8*i, y=y+10)
    pdf.x, pdf.y = x - 7, y + 18
    with pdf.local_context(font_size=12):
        for i in range(4):
            pdf.cell(text="+1  ___________________", h=9, new_x="LEFT", new_y="NEXT")

def render_side_stats_block(pdf, x, y):
    pdf.set_font(size=20)
    # Résistance + protection :
    pdf.x, pdf.y = x + 77, y-3
    pdf.cell(text="Résistance")
    pdf.image(DIR / "rope-in-circle-from-illustrated-norways-history-1885-cc0.png",
              w=18, h=18, x=x+76, y=y+6)
    pdf.x, pdf.y = x + 94, y + 12
    pdf.cell(text="+")
    pdf.image(DIR / "rope-in-circle-from-illustrated-norways-history-1885-cc0.png",
              w=15, h=15, x=x+100, y=y+7.5)
    with pdf.local_context(font_size=12):
        pdf.x, pdf.y = x + 96, y + 25
        pdf.cell(text="(protection)")
    # Blessures :
    pdf.image(DIR / "circle-frame2.png", w=18, h=18, x=x-2, y=y-6)
    pdf.x, pdf.y = x + 17, y
    pdf.cell(text="Blessures")
    # Vitesse :
    pdf.image(DIR / "rope-in-circle-from-illustrated-norways-history-1885-cc0.png",
              w=18, h=18, x=x-2, y=y+15)
    pdf.x, pdf.y = x + 17, y + 20
    pdf.cell(text="Points de Destin")
    # Points de Destin :
    pdf.image(DIR / "rope-in-circle-from-illustrated-norways-history-1885-cc0.png",
              w=18, h=18, x=x-2, y=y+36)
    pdf.x, pdf.y = x + 17, y + 41
    pdf.cell(text="Vitesse")

def render_xp_block(pdf, x, y):
    pdf.image(DIR / "scrolls/scroll-from-rawpixel2-vertical.png", w=80, x=x, y=y)
    pdf.x, pdf.y = x, y + 5
    pdf.cell(text="Expérience", align="C", w=80)
    pdf.set_font(size=18)
    pdf.x, pdf.y = x + 16, y + 26
    pdf.cell(text="Clefs :")
    pdf.image(DIR / "die-one.png", w=7, h=7, x=x+45, y=y+26)
    with pdf.local_context(font_size=12):
        pdf.x = x + 52
        pdf.cell(text="+1 XP", h=9)
        pdf.x, pdf.y = x + 12, y + 35
        for i in range(3):
            pdf.cell(text="+1 XP : ___________________", h=9, new_x="LEFT", new_y="NEXT")
            pdf.cell(text="___________________________", h=9, new_x="LEFT", new_y="NEXT")
            pdf.cell(text="___________________________", h=9, new_x="LEFT", new_y="NEXT")
            pdf.y += 5
    pdf.set_font(size=14)
    pdf.x, pdf.y = x + 14, y + 140
    pdf.cell(text="XP :       / dépensé :")

def render_equipment_block(pdf, x, y):
    pdf.image(DIR / "TabletopArtPack-MakingCamp.png", w=60, x=x+56, y=y-30)
    pdf.set_font(size=24)
    pdf.x, pdf.y = x + 6, y + 4.5
    pdf.cell(text="Équipement", align="C")
    with pdf.local_context(font_size=12):
        for i in range(7):
            img_filename = "checkbox.jpg"
            if i >= 3:
                img_filename = "checkbox-grey.jpg"
                pdf.set_text_color(200)
            for dx in (x, x + 60):
                pdf.image(DIR / img_filename, w=5, x=dx, y=y+18+i*10)
                pdf.x, pdf.y = dx + 6, y + 16 + i*10
                pdf.cell(text="___________________________", h=9)

def render_notes_reminder(pdf, x, y):
    pdf.image(DIR / "feather.png", w=14, x=x, y=y)
    pdf.set_font(size=14)
    pdf.set_text_color(128)
    pdf.x, pdf.y = x+12, y+4
    pdf.cell(text="Penses à prendre des notes")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        SRC_FILES = (__file__, MD_FILEPATH, CSS_FILEPATH)
        watch_xreload_and_serve(sys.modules[__name__], DIR, *SRC_FILES)
