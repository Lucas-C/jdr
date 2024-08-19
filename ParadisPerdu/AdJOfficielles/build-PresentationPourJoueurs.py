#!/usr/bin/env python
# USAGE: ./build-PresentationPourJoueurs.py
import os, sys
from pypdf import PdfReader, PdfWriter

CUR_DIR = os.path.dirname(__file__)
sys.path.append(f"{CUR_DIR}/../..")  # make pdf_utils.py importable
from pdf_utils import add_to_page

def _addpages_from_ranges(writer, page_ranges):
    pages = PdfReader(f"{CUR_DIR}/ParadisPerdu_presentation.pdf").pages
    for page_range in page_ranges:
        for pagenum in range(page_range[0], page_range[1]+1):
            writer.add_page(pages[pagenum-1])

writer = PdfWriter()
_addpages_from_ranges(writer, ((1, 2), (4, 6)))
with add_to_page(writer.pages[1], unit="pt") as pdf:
    pdf.set_fill_color("#9098a0")
    pdf.rect(x=183, y=265.5, w=66, h=10, style="F")
    pdf.set_fill_color("#b1b5bb")
    pdf.rect(x=184.5, y=379.5, w=100, h=10, style="F")
    pdf.set_fill_color("#b8bac0")
    pdf.rect(x=197, y=447, w=100, h=10, style="F")
with add_to_page(writer.pages[3], unit="pt") as pdf:
    pdf.set_fill_color(255)  # white
    pdf.rect(x=212, y=558, w=10, h=10, style="F")
with add_to_page(writer.pages[4], unit="pt") as pdf:
    pdf.set_fill_color(255)  # white
    pdf.rect(x=198, y=558, w=10, h=10, style="F")
writer.write(f"{CUR_DIR}/ParadisPerdu_PresentationPourJoueurs.pdf")
