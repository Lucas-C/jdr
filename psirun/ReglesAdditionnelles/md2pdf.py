#!/usr/bin/env python3
import asyncio, sys
from pathlib import Path
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".." / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

CSS_FILEPATH = DIR / "style.css"

FR_MD_FILEPATH = DIR / "README.md"
FR_OUT_FILEPATH = DIR / "PsiRun-ReglesAdditionnelles.pdf"
FR_METADATA = dict(
    title="Psi*Run - Règles additionnelles",
    keywords=("jeu-de-rôle", "jdr", "psi*run", "variante", "règles"),
    description="Règles additionnelles pour le jeu de rôle Psi*Run",
)

EN_MD_FILEPATH = DIR / "ExtraRules.md"
EN_OUT_FILEPATH = DIR / "PsiRun-ExtraRules.pdf"
EN_METADATA = dict(
    title="Psi*Run - Extra rules",
    keywords=("tabletop-roleplaying-game", "ttrpg", "psi*run", "variant", "rules"),
    description="Extra rules for the Psi*Run tabletop role-playing game",
)


def build_pdf():
    md_filepaths = ()
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF
    build_single_pdf(EN_MD_FILEPATH, EN_OUT_FILEPATH, EN_METADATA, lang="en"); md_filepaths += EN_MD_FILEPATH,
    build_single_pdf(FR_MD_FILEPATH, FR_OUT_FILEPATH, FR_METADATA, lang="fr"); md_filepaths += FR_MD_FILEPATH,
    return md_filepaths

def build_single_pdf(md_filepath, out_filepath, metadata, lang):
    start = perf_counter()
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang).getbuffer())
    set_metadata(out_filepath, **metadata, lang=lang)
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
