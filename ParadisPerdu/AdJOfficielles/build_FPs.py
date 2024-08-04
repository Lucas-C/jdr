#!/usr/bin/env python
# INSTALL: pip install pypdf
# USAGE: ./build_FPs.py
import io, os
from contextlib import contextmanager
from fpdf import FPDF
from pypdf import PdfReader, PdfWriter

CUR_DIR = os.path.dirname(__file__)
SRC_PDF = f"{CUR_DIR}/ParadisPerdu_fichedepersos_Le-mot-de-passe-est-le-nom-de-la-drogue.pdf"

def build_fp(index, name):
    writer = PdfWriter()
    _from_pdf_page(writer, index)
    with _add_to_page(writer) as pdf:
        pdf.set_font("Helvetica", size=9)
        pdf.x, pdf.y = 160, 25
        pdf.multi_cell(w=80, h=3.666, text="""
Torrensen sera joué par Anna
Park sera joué par Mirko
Arora sera joué par Aurélien
Aberdeen sera joué par Michael
Sullivan sera joué par Matthieu""")
    out_filepath = f"{CUR_DIR}/ParadisPerdu_FP_{name}.pdf"
    writer.write(out_filepath)
    print(f"{out_filepath} generated")

def _from_pdf_page(writer, index):
    pages = PdfReader(SRC_PDF, password="Tedium").pages
    writer.add_page(pages[index])

@contextmanager
def _add_to_page(writer, index=0):
    pdf = FPDF(orientation="landscape")
    pdf.add_page()
    pdf.set_fill_color(255)  # white
    yield pdf
    overlay_pdf = io.BytesIO(pdf.output())
    overlay_page = PdfReader(overlay_pdf).pages[0]
    writer.pages[index].merge_page(page2=overlay_page)

build_fp(0, "Torrensen")
build_fp(1, "Park")
build_fp(2, "Aberdeen")
build_fp(3, "Arora")
build_fp(4, "Sullivan")
