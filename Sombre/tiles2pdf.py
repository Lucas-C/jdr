#!/usr/bin/env python3
from pathlib import Path
from fpdf import FPDF

DIR = Path(__file__).parent

def add_tiles(img1, img2, scale):  # scale: mm / pixel
    _, _, img1_info = pdf.preload_image(DIR / "tiles" / img1)
    img1_width_mm = img1_info.width * scale
    img1_height_mm = img1_info.height * scale
    assert img1_width_mm < pdf.epw / 2, f"{img1_width_mm} >= {pdf.epw/2}"
    x = pdf.w/2 - img1_width_mm
    pdf.image(DIR / "tiles" / img1, x=x, y=pdf.y, w=img1_width_mm, keep_aspect_ratio=True)
    _, _, img2_info = pdf.preload_image(DIR / "tiles" / img2)
    img2_width_mm = img2_info.width * scale
    img2_height_mm = img2_info.height * scale
    assert img2_width_mm < pdf.epw / 2, f"{img2_width_mm} >= {pdf.epw/2}"
    x = pdf.w/2
    pdf.y += (img1_height_mm - img2_height_mm) / 2
    pdf.image(DIR / "tiles" / img2, x=x, y=pdf.y, w=img2_width_mm, keep_aspect_ratio=True)
    pdf.y += max(img1_height_mm, img2_height_mm)

pdf = FPDF()
pdf.t_margin *= 2

pdf.add_page()
add_tiles("Laboratory-Office-1.jpg", "Laboratory-Office-2.jpg", scale=.2)
pdf.y += 20
add_tiles("Laboratory-WC-1.jpg", "Laboratory-WC-2.jpg", scale=.2)
pdf.line(x1=pdf.w/2, y1=0, x2=pdf.w/2, y2=pdf.h)

pdf.add_page()
pdf.y += 35
add_tiles("Laboratory-SpecimensBench-1-short.jpg", "Laboratory-SpecimensBench-2-short.jpg", scale=.12)
pdf.line(x1=pdf.w/2, y1=0, x2=pdf.w/2, y2=pdf.h)

pdf.add_page()
add_tiles("Laboratory-Garage-1.jpg", "Laboratory-Garage-2.jpg", scale=.1)
pdf.line(x1=pdf.w/2, y1=0, x2=pdf.w/2, y2=pdf.h)

pdf.output(DIR / "Sombre-WIP.pdf")
