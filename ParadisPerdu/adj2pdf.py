#!/usr/bin/env python3
# Script Dependencies:
#    livereload
#    mistletoe
#    weasyprint
#    xreload
import asyncio, logging, sys
from pathlib import Path

DIR = Path(__file__).parent

logging.getLogger("fontTools.subset").level = logging.WARN  # avoid useless verbose logging
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, start_watch_and_rebuild

MD_FILEPATH = DIR / "TerraNova-LieuxEmblematiques.md"
CSS_FILEPATH = DIR / "style.css"
OUT_FILEPATH = DIR / "ParadisPerdu-LieuxEmblematiques.pdf"


def build_pdf():
    with OUT_FILEPATH.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH).getbuffer())
    print(f"{OUT_FILEPATH} has been rebuilt")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        SRC_FILES = (__file__, MD_FILEPATH, CSS_FILEPATH)
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
