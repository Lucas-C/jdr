#!/usr/bin/env python3
import asyncio, sys
from pathlib import Path
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

MD_FILEPATH = DIR / "AmnesicFantasy.md"
CSS_FILEPATH = DIR / "style.css"
OUT_FILEPATH = DIR / "AmnesicFantasy.pdf"


def build_pdf(target_md_file=None):
    start = perf_counter()
    with OUT_FILEPATH.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH, lang="fr").getbuffer())
    set_metadata(OUT_FILEPATH,
        title="Amnesic Fantasy",
        lang="fr",
        keywords=("jdr", "ttrpg", "escape-game", "roleplay"),
        description="TODO",
    )
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
