#!/usr/bin/env python
# USAGE: ./build_FPs.py
import os, sys
from pypdf import PdfReader, PdfWriter

CUR_DIR = os.path.dirname(__file__)
sys.path.append(f"{CUR_DIR}/..")  # make pdf_utils.py importable
from pdf_utils import add_to_page

SRC_PDF = f"{CUR_DIR}/LBB_CHAP1_L_indomptable_bleue_du_Firmament.pdf"

PC_NAMES = (
    "Natasha Syri (Lady Blackbird)",
    "Naomi Bishop",
    "Cyrus Vance",
    "Kale Arkam",
    "Snargle",
)

writer = PdfWriter()
writer.append(PdfReader(SRC_PDF), pages=(2, 7))
for i in range(5):
    with add_to_page(writer.pages[i]) as pdf:
        pdf.add_font(fname="fonts/Coelacanth.otf")
        pdf.set_font("Coelacanth", size=11)
        pdf.x, pdf.y = 114, 110
        pdf.multi_cell(w=84, h=8, text="\n".join(
            f"_____________  joue {name}" for j, name in enumerate(PC_NAMES) if i != j)
        )
out_filepath = f"{CUR_DIR}/Lady-BlackBird-FPs.pdf"
writer.write(out_filepath)
print(f"{out_filepath} generated")
