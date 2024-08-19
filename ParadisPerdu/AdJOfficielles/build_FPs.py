#!/usr/bin/env python
# USAGE: ./build_FPs.py
import os, sys
from pypdf import PdfReader, PdfWriter

CUR_DIR = os.path.dirname(__file__)
sys.path.append(f"{CUR_DIR}/../..")  # make pdf_utils.py importable
from pdf_utils import add_to_page

SRC_PDF = f"{CUR_DIR}/ParadisPerdu_fichedepersos_Le-mot-de-passe-est-le-nom-de-la-drogue.pdf"

def build_fp(index, name):
    writer = PdfWriter()
    _from_pdf_page(writer, index)
    with add_to_page(writer.pages[0]) as pdf:
        pdf.set_fill_color(255)  # white
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

build_fp(0, "Torrensen")
build_fp(1, "Park")
build_fp(2, "Aberdeen")
build_fp(3, "Arora")
build_fp(4, "Sullivan")
