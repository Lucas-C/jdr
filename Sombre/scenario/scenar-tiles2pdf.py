#!/usr/bin/env python3
# Script Dependencies:
#    fpdf2
#    livereload
#    xreload
import asyncio, logging, sys
from pathlib import Path
from traceback import print_exc

from fpdf import FPDF
from fpdf.enums import Align
from livereload.watcher import get_watcher_class
from xreload import xreload


DIR = Path(__file__).parent
SCALE = .12  # scale: mm / pixel


def add_side_by_side(pdf, img1, img2=None, shadow=False):
    img1_width_mm, img1_height_mm = add_tile(pdf, img1, halign=Align.L)
    assert img1_width_mm < pdf.epw / 2, f"{img_width_mm} >= {pdf.epw/2}"
    if img2:
        img2_width_mm, img2_height_mm = add_tile(pdf, img2, halign=Align.R, valign_height=img1_height_mm)
        assert img2_width_mm < pdf.epw / 2, f"{img_width_mm} >= {pdf.epw/2}"
        vert_shift_mm = max(img1_height_mm, img2_height_mm)
    else:
        vert_shift_mm = img1_height_mm
        if shadow:
            x = halign2x(Align.R, pdf, img1_width_mm)
            pdf.rect(x=x, y=pdf.y, w=img1_width_mm, h=img1_height_mm)
    pdf.y += vert_shift_mm
    pdf.line(x1=pdf.w/2, y1=0, x2=pdf.w/2, y2=pdf.h)


def add_top_bottom(pdf, img1, shadow=False):
    img1_width_mm, img1_height_mm = add_tile(pdf, img1, halign=Align.C)
    pdf.y += img1_height_mm
    pdf.line(x1=0, y1=pdf.y, x2=pdf.w, y2=pdf.y)
    if shadow:
        x = halign2x(Align.C, pdf, img1_width_mm)
        pdf.rect(x=x, y=pdf.y, w=img1_width_mm, h=img1_height_mm)


def add_tile(pdf, img_filename, halign, valign_height=None):
    _, _, img_info = pdf.preload_image(DIR / "tiles" / img_filename)
    img_width_mm = img_info.width * SCALE
    img_height_mm = img_info.height * SCALE
    if valign_height:
        pdf.y += (valign_height - img_height_mm) / 2
    x = halign2x(halign, pdf, img_width_mm)
    pdf.image(DIR / "tiles" / img_filename, x=x, y=pdf.y, w=img_width_mm, keep_aspect_ratio=True)
    return img_width_mm, img_height_mm


def halign2x(halign, pdf, img_width_mm):
    if halign == Align.L:
        return pdf.w/2 - img_width_mm
    if halign == Align.C:
        return pdf.w/2 - img_width_mm / 2
    if halign == Align.R:
        return pdf.w/2
    raise ValueError(f"Invalid halign: {halign}")


def build_pdf():
    pdf = FPDF()
    pdf.t_margin *= 2

    pdf.add_page()
    add_side_by_side(pdf, "Laboratory-Corridor-1.jpg", "Laboratory-Corridor-2.jpg")
    pdf.y += 15
    add_side_by_side(pdf, "Laboratory-Garage-1.jpg", "Laboratory-Garage-2.jpg")

    pdf.add_page()
    add_side_by_side(pdf, "Laboratory-Office-1.jpg", "Laboratory-Office-2.jpg")
    pdf.y += 20
    add_side_by_side(pdf, "Laboratory-WC-1.jpg", "Laboratory-WC-2.jpg")
    pdf.y += 20
    add_side_by_side(pdf, "Laboratory-Lab.jpg", shadow=True)

    pdf.add_page()
    add_side_by_side(pdf, "Laboratory-SpecimensBench-1-short.jpg", "Laboratory-SpecimensBench-2-short.jpg")
    pdf.y += 15
    add_side_by_side(pdf, "Laboratory-Closet.jpg", shadow=True)

    pdf.add_page()
    pdf.y += 20
    add_side_by_side(pdf, "Laboratory-ControlRoom-1.jpg", shadow=True)
    pdf.y += 30
    add_side_by_side(pdf, "Laboratory-ControlRoom-2.jpg", shadow=True)

    pdf.add_page()
    pdf.y += 20
    add_top_bottom(pdf, "Laboratory-StorageRoom.jpg", shadow=True)

    out_filepath = "Sombre-WIP.pdf"
    pdf.output(DIR / out_filepath)
    print(f"{out_filepath} has been rebuilt")


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
        asyncio.run(start_watch_and_rebuild())
