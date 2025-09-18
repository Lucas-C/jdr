#!/usr/bin/env python3
import asyncio, logging, sys
from pathlib import Path
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    MD_FILEPATH := DIR / "README.md",
)

METADATA = {
    "title": "Girl Underground - Aides de jeu en français",
    "keywords": ("jeu-de-rôle", "jdr", "GirlUnderground", "alice-au-pays-des-merveilles"),
    "description": "Aides de jeu en français pour le jeu de rôle Girl Underground",
}


def build_pdf(target_md_file=None):
    start = perf_counter()
    out_filepath = DIR / "GirlUnderground-FR.pdf"
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH, lang="fr").getbuffer())
    set_metadata(out_filepath, **METADATA, lang="fr")
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
