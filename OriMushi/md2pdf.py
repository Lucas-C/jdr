#!/usr/bin/env python3
import asyncio, logging, sys
from math import cos, pi, sin, sqrt
from pathlib import Path
from random import random
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

CSS_FILEPATH = DIR / "style.css"
RULES_MD_FILEPATH = DIR / "OriMushi.md"
RULES_OUT_FILEPATH = DIR / "OriMushi.pdf"
SCENAR1_MD_FILEPATH = DIR / "LesDisparusDuFestivalDuPrintemps.md"
SCENAR1_OUT_FILEPATH = DIR / "LesDisparusDuFestivalDuPrintemps.pdf"
SCENAR2_MD_FILEPATH = DIR / "LaSepultureDuDaimio.md"
SCENAR2_OUT_FILEPATH = DIR / "LaSepultureDuDaimio.pdf"
METADATA = dict(
    title="Ori Mushi",
    lang="fr",
    keywords=("jdr", "ttrpg", "japon", "fantasy", "naruto", "ghibli", "okami", "avatar"),
    description="Un jeu de rôle minimaliste inspiré où l'on joue dans un univers de fantasy inspiré du japon médiéval.",
)


def build_pdf():
    # Uncomment one of the lines below to only --watch/re-build a single PDF:
    build_single_pdf(SCENAR1_MD_FILEPATH, SCENAR1_OUT_FILEPATH)
    build_single_pdf(SCENAR2_MD_FILEPATH, SCENAR2_OUT_FILEPATH)
    build_single_pdf(RULES_MD_FILEPATH, RULES_OUT_FILEPATH)

def build_single_pdf(md_filepath, out_filepath):
    start = perf_counter()
    with out_filepath.open("wb") as out_pdf_file:
        pdf = markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang="fr", metadata=METADATA).getbuffer()
        out_pdf_file.write(pdf)
    set_metadata(out_filepath, **METADATA)
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        SRC_FILES = (__file__, CSS_FILEPATH, RULES_MD_FILEPATH, SCENAR1_MD_FILEPATH, SCENAR2_MD_FILEPATH)
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
