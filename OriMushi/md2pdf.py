#!/usr/bin/env python3
import asyncio, logging, sys
from math import cos, pi, sin, sqrt
from pathlib import Path
from random import random
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

MD_FILEPATH = DIR / "OriMushi.md"
CSS_FILEPATH = DIR / "style.css"
OUT_FILEPATH = DIR / "OriMushi.pdf"
METADATA = dict(
    title="Ori Mushi",
    lang="fr",
    keywords=("jdr", "ttrpg", "japon", "fantasy", "naruto", "ghibli", "okami", "avatar"),
    description="Un jeu de rôle minimaliste inspiré où l'on joue dans un univers de fantasy inspiré du japon médiéval.",
)


def build_pdf():
    start = perf_counter()
    with OUT_FILEPATH.open("wb") as out_pdf_file:
        pdf = markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH, lang="fr", metadata=METADATA).getbuffer()
        out_pdf_file.write(pdf)
    set_metadata(OUT_FILEPATH, **METADATA)
    print(f"{OUT_FILEPATH} has been rebuilt in {perf_counter() - start:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        SRC_FILES = (__file__, MD_FILEPATH, CSS_FILEPATH)
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
