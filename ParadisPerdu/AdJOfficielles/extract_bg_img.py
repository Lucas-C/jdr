#!/usr/bin/env python
import os, subprocess
from pypdf import PdfWriter

CUR_DIR = os.path.dirname(__file__)
SRC_PDF = f"{CUR_DIR}/ParadisPerdu_presentation.pdf"

i = 3
for page in (2, 6):
    writer = PdfWriter()
    writer.append(SRC_PDF, pages=(page, page + 1))
    writer.remove_text()
    tmp_pdf_filepath = f"{CUR_DIR}/tmp.pdf"
    writer.write(tmp_pdf_filepath)

    out_jpg_filepath = f"{CUR_DIR}/ParadisPerdu_presentation_bg{i}.jpg"
    subprocess.run(["convert", "-density", "300", tmp_pdf_filepath, "-flatten", out_jpg_filepath], check=True)
    os.remove(tmp_pdf_filepath)
    i += 1
