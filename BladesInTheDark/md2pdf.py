#!/usr/bin/env python3
import asyncio, logging, sys
from pathlib import Path

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

# Avoid some useless verbose logs:
logging.getLogger("fontTools.subset").level = logging.WARN
logging.getLogger("fontTools.ttLib.tables.O_S_2f_2").level = logging.ERROR

MD_FILEPATH = DIR / "BitD-Questioning.md"
CSS_FILEPATH = DIR / "style.css"
OUT_FILEPATH = DIR / "BitD-Questioning.pdf"


def build_pdf():
    with OUT_FILEPATH.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, MD_FILEPATH, CSS_FILEPATH).getbuffer())
    set_metadata(OUT_FILEPATH,
        title="Blades in the Dark - Interrogatoires",
        keywords=("jdr", "ttrpg", "blades in the dark", "roleplay", "aide de jeu"),
        description="Cette aide de jeu propose de développer les scènes d'interrogatoire du jeu de rôle Blades in the Dark, pour en faire des moments cruciaux, où les PJs sont mis sous pression par les Inspecteurs, où ils ont beaucoup à perdre, et où la situation se résoudra par des moments de roleplay mémorables.",
    )
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
