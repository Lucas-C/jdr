#!/usr/bin/env python3
import asyncio, logging, sys
from math import cos, pi, sin, sqrt
from pathlib import Path
from random import random
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import add_to_every_page_dynamic, markdown2pdf, set_metadata, start_watch_and_rebuild

# Avoid some useless verbose logs:
logging.getLogger("fontTools.subset").level = logging.WARN
logging.getLogger("fontTools.ttLib.tables.O_S_2f_2").level = logging.ERROR

MD_FILEPATH = DIR / "ModulesDeSecours.md"
CSS_FILEPATH = DIR / "style.css"
DIAGRAM_FILEPATHS = (DIR / "scenario1.svg", DIR / "scenario2.svg")
OUT_FILEPATH = DIR / "ParadisPerdu-ModulesDeSecours.pdf"


def build_pdf():
    start = perf_counter()
    with OUT_FILEPATH.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH, lang="fr").getbuffer())
    add_page_number_backgrounds(OUT_FILEPATH)
    set_metadata(OUT_FILEPATH,
        title="Paradis Perdu - Modules de secours",
        keywords=("jdr", "ttrpg", "aide de jeu", "sci-fi"),
        description="Une aide de jeu composée d'un ensemble de modules optionnels, pour ajouter des rebondissements supplémentaires au scénario original de Yno.",
    )
    print(f"{OUT_FILEPATH} has been rebuilt in {perf_counter() - start:.1f}s")


def add_page_number_backgrounds(pdf_filepath):
    """
    Note: the git history contains an example of rendering just a circle
    as background for page numbers using CSS position: fixed
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
        if i == 0:  # skipping 1st page
            continue
        def circle(x, y, r, style):
            # Workaround while pending for a fix for fpdf2 issue...
            pdf.circle(x-r, y-r, 2*r, style)
        # Debug render bounding box:
        #   pdf.set_draw_color(255, 0, 0)
        #   pdf.rect(x0, y0, w, h, style="D")
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
            circle(x, y, size, style="F")
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
        pdf.set_draw_color(30, 60, 143)
        circle(center_x, center_y, circle_radius, style="D")
        pdf.set_line_width(.5)
        pdf.set_draw_color(77, 93, 182)
        circle(center_x, center_y, circle_radius - .3, style="D")
        pdf.set_line_width(.4)
        pdf.set_draw_color(118, 129, 222)
        circle(center_x, center_y, circle_radius - .7, style="D")


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
        SRC_FILES = (__file__, MD_FILEPATH, CSS_FILEPATH) + DIAGRAM_FILEPATHS
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
