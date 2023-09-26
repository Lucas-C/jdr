#!/usr/bin/env python3
# Script Dependencies:
#    fpdf2
from pathlib import Path
from fpdf import FPDF

DIR = Path(__file__).parent

pdf = FPDF(orientation="landscape")
pdf.b_margin = pdf.t_margin = 12
pdf.add_page()
pdf.image(DIR / "FullPlan.jpg", h=pdf.eph, w=pdf.epw, keep_aspect_ratio=True)
pdf.output(DIR / "FullPlan.pdf")
