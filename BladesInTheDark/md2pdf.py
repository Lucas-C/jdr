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

CSS_FILEPATH = DIR / "style.css"
DEMON_MD_FILEPATH = DIR / "BitD-DemonSheet.md"
INT_EN_MD_FILEPATH = DIR / "BitD-Interrogation.md"
INT_FR_MD_FILEPATH = DIR / "BitD-Interrogatoires.md"

DEMON_METADATA = {}  # TODO before publishing
INT_FR_METADATA = {
    "title": "Blades in the Dark - Interrogatoires",
    "keywords": ("jdr", "ttrpg", "blades in the dark", "roleplay", "aide de jeu", "interrogatoire"),
    "description": "Cette aide de jeu propose de développer les scènes d'interrogatoire du jeu de rôle Blades in the Dark, pour en faire des moments cruciaux, où les PJs sont mis sous pression par les Inspecteurs, où ils ont beaucoup à perdre, et où la situation se résoudra par des moments de roleplay mémorables.",
}
INT_EN_METADATA = {
    "title": "Blades in the Dark - Interrogation",
    "keywords": ("ttrpg", "blades in the dark", "roleplay", "module", "interrogation"),
    "description": "This game module develops the interrogation scenes of the tabletop roleplaying game Blades in the Dark, to make them crucial moments, where the PCs are put under pressure by the Inspectors, where they have a lot to lose, and where the situation will be resolved by memorable roleplay moments.",
}

def build_pdf():
    md_filepaths = ()
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF
    build_single_pdf(DEMON_MD_FILEPATH,  DEMON_METADATA,  lang="fr"); md_filepaths += DEMON_MD_FILEPATH,
    build_single_pdf(INT_FR_MD_FILEPATH, INT_FR_METADATA, lang="fr"); md_filepaths += INT_FR_MD_FILEPATH,
    build_single_pdf(INT_EN_MD_FILEPATH, INT_EN_METADATA, lang="en"); md_filepaths += INT_EN_MD_FILEPATH,
    return md_filepaths

def build_single_pdf(md_filepath, metadata, lang):
    start = perf_counter()
    out_filepath = md_filepath.with_suffix(".pdf")
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang).getbuffer())
    set_metadata(out_filepath, **metadata)
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    SRC_FILES = (__file__, CSS_FILEPATH)
    SRC_FILES += build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
