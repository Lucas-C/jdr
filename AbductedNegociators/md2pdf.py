#!/usr/bin/env python3
# USAGE: [FAST=1] ./md2pdf.py [--watch] [file.md]
import asyncio, logging, os, sys
from math import cos, pi, sin, sqrt
from pathlib import Path
from random import random
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import add_to_every_page_dynamic, copy_files, export_img, markdown2pdf, md2html, set_metadata, start_watch_and_rebuild
copy_files(DIR, "font:Candara")

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    EN_MD_FILEPATH := DIR / "AbductedNegociators.md",
    FR_MD_FILEPATH := DIR / "Abductes.md",
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/CriticalFondation/
    README_MD_FILEPATH := DIR / "README.md",
)

METADATA = {
    FR_MD_FILEPATH: {
        "lang": "fr",
        "title": "Abductés",
        "keywords": ("jdr", "jeu-de-rôle", "roleplay", "enlèvement", "science-fiction", "négociation", "minuteur", "alien", "cartes"),
        "description": "Un jeu de rôle centré sur le roleplay et employant des cartes",
    },
    EN_MD_FILEPATH: {
        "lang": "en",
        "title": "Abducted Negociators",
        "keywords": ("tabletop-roleplaying-game", "ttrpg", "roleplay", "abduction", "alien", "science-fiction", "negotiation", "timed", "cards"),
        "description": "A tabletop roleplaying game based on roleplay and some cards",
    },
    README_MD_FILEPATH: { "lang": "fr", "pdf": False },
}

def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None  # => rebuild all target PDFs
    if target_md_file is None and len(sys.argv) > 1 and sys.argv[-1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[-1])
    for md_src_file in SRC_FILES[2:]:
        metadata = {**METADATA[md_src_file]}
        lang = metadata.pop("lang")
        if target_md_file is None or target_md_file == md_src_file:
            if metadata.pop("pdf", None) is False:
                with open(md_src_file, encoding="utf8") as md_file:
                    md2html(DIR, md_file.read(), CSS_FILEPATH, lang=lang, metadata=metadata)
            else:
                build_single_pdf(md_src_file, metadata, lang)

def build_single_pdf(md_filepath, metadata, lang):
    out_filepath = md_filepath.with_suffix(".pdf")
    prefix = metadata.pop("prefix", None)
    if prefix:
        out_filepath = out_filepath.with_name(prefix + out_filepath.name)
    pdf = markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang, metadata=metadata).getbuffer()
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(pdf)
    start = perf_counter()
    set_metadata(out_filepath, **metadata, lang=lang)
    metadata_duration = perf_counter() - start
    if "FAST" in os.environ:
        pages_bg_duration = 0
        cards_duration = 0
    else:
        start = perf_counter()
        add_page_number_backgrounds(out_filepath)
        pages_bg_duration = perf_counter() - start
        cards_duration = export_img(out_filepath, (
            dict(page=8, suffix="-PersonalityCards", crop=(125, 610, 2355, 2220)),
        ))
    print(f"{out_filepath} has been rebuilt: metadata={metadata_duration:.1f}s pages_bg={pages_bg_duration:.1f}s cards={cards_duration:.1f}s")


def add_page_number_backgrounds(pdf_filepath):
    """
    Note: it is also possible to render a simple circle / image
    as background for page numbers using just CSS position: fixed
    """
    # Position / size on page:
    x0 = 99
    y0 = 278
    w = h = 12
    # Parameters:
    circle_radius = 4
    count = 10  # particles
    min_size = .2  # for particles
    max_size = .8  # for particles
    edge_width = .13
    no_edges_radius = 2  # circular zone where edges are not allowed
    edge_probability = .5  # among edges not crossing the no-edges-circular-zone
    # Dependent constants:
    center_x = x0 + w / 2
    center_y = y0 + h / 2
    half_diagonal = sqrt(w*w + h*h) / 2
    for i, pdf in enumerate(add_to_every_page_dynamic(pdf_filepath)):
        # Rendering particles:
        pdf.set_fill_color(0)  # black
        particles = []
        angle = 0
        while len(particles) < count:
            angle += random() * pi
            radius = circle_radius + random() * (half_diagonal - circle_radius)
            x = center_x + radius * cos(angle)
            y = center_y + radius * sin(angle)
            if x < x0 + max_size or x > x0 + w - max_size or y < y0 + max_size or y > y0 + h - max_size:
                continue
            size = min_size + random() * (max_size - min_size)
            pdf.circle(x, y, size, style="F")
            particles.append((x, y))
        # Drawing edges:
        pdf.set_line_width(edge_width)
        pdf.set_draw_color(0)  # black
        for i, part1 in enumerate(particles):
            for part2 in particles[i + 1:]:
                edge_cross_center = is_line_intersecting(*part1, *part2, center_x, center_y, r=no_edges_radius)
                if not edge_cross_center and random() < edge_probability:
                    pdf.line(*part1, *part2)
        # Draw central circle:
        pdf.set_line_width(.2)
        pdf.circle(center_x, center_y, circle_radius, style="D")


def is_line_intersecting(ax, ay, bx, by, cx, cy, r):
    "Recipe from: https://math.stackexchange.com/a/275537"
    ax -= cx
    ay -= cy
    bx -= cx
    by -= cy
    a = (bx - ax)**2 + (by - ay)**2
    b = 2 * (ax * (bx - ax) + ay * (by - ay))
    c = ax**2 + ay**2 - r**2
    det = b**2 - 4 * a * c
    if det <= 0:
        return False
    t1 = (-b - sqrt(det)) / (2 * a)
    t2 = (-b + sqrt(det)) / (2 * a)
    return 0 < t1 < 1 and 0 < t2 < 1


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
