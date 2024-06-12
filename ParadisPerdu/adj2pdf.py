#!/usr/bin/env python3
import asyncio, logging, sys
from pathlib import Path
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

# Avoid some useless verbose logs:
logging.getLogger("fontTools.subset").level = logging.WARN
logging.getLogger("fontTools.ttLib.tables.O_S_2f_2").level = logging.ERROR

MD_FILEPATH = DIR / "ModulesDeSecours.md"
CSS_FILEPATH = DIR / "style.css"
OUT_FILEPATH = DIR / "ParadisPerdu-ModulesDeSecours.pdf"


def build_pdf():
    start = perf_counter()
    with OUT_FILEPATH.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH, lang="fr").getbuffer())
    set_metadata(OUT_FILEPATH,
        title="Paradis Perdu - Modules de secours",
        keywords=("jdr", "ttrpg", "aide de jeu", "sci-fi"),
        description="Une aide de jeu composée d'un ensemble de modules optionnels, pour ajouter des rebondissements supplémentaires au scénario original de Yno.",
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
