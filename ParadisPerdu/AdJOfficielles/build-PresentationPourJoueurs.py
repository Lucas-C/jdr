#!/usr/bin/env python
# USAGE: ./build-PresentationPourJoueurs.py
import os
from contextlib import contextmanager
from fpdf import FPDF
from pdfrw import PageMerge, PdfReader, PdfWriter
from pdfrw.pagemerge import RectXObj

CUR_DIR = os.path.dirname(__file__)

def _addpages_from_ranges(writer, page_ranges):
    pages = PdfReader(f"{CUR_DIR}/ParadisPerdu_presentation.pdf").pages
    for page_range in page_ranges:
        for pagenum in range(page_range[0], page_range[1]+1):
            writer.addpage(pages[pagenum-1])

@contextmanager
def _add_to_page(writer, index):
    area = RectXObj(writer.pagearray[index])
    pdf = FPDF(format=(area.w, area.h), unit="pt")
    pdf.add_page()
    pdf.set_fill_color(0)  # black
    yield pdf
    overlay_pdf = bytes(pdf.output())
    overlay_page = PdfReader(fdata=overlay_pdf).pages[0]
    PageMerge(writer.pagearray[index]).add(overlay_page).render()


writer = PdfWriter(f"{CUR_DIR}/ParadisPerdu_PresentationPourJoueurs.pdf")
_addpages_from_ranges(writer, ((1, 2), (4, 6)))
with _add_to_page(writer, index=1) as pdf:
    pdf.rect(x=183, y=265.5, w=66, h=10, style="F")
    pdf.rect(x=185, y=379.5, w=100, h=10, style="F")
    pdf.rect(x=197, y=447, w=100, h=10, style="F")
writer.write()
