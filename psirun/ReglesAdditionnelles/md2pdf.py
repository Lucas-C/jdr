#!/usr/bin/env python3
# USAGE: ./md2pdf.py [file.md]
import asyncio, logging, sys
from pathlib import Path
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".." / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/psirun/ReglesAdditionnelles/
    EN_MD_FILEPATH := DIR / "ExtraRules.md",
    FR_MD_FILEPATH := DIR / "README.md",
)

METADATA = {
    FR_MD_FILEPATH: dict(
        title="Psi*Run - Règles additionnelles",
        lang="fr",
        keywords=("jeu-de-rôle", "jdr", "psi*run", "variante", "règles"),
        description="Règles additionnelles pour le jeu de rôle Psi*Run",
        out_filepath=DIR / "PsiRun-ReglesAdditionnelles.pdf",
    ),
    EN_MD_FILEPATH: dict(
        title="Psi*Run - Extra rules",
        lang="en",
        keywords=("tabletop-roleplaying-game", "ttrpg", "psi*run", "variant", "rules"),
        description="Extra rules for the Psi*Run tabletop role-playing game",
        out_filepath=DIR / "PsiRun-ExtraRules.pdf",
    ),
}


def build_pdf(target_md_file=None):
    if len(sys.argv) > 1 and sys.argv[1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[1])
    for md_src_file in SRC_FILES[2:]:
        metadata = METADATA[md_src_file]
        out_filepath = metadata.pop("out_filepath")
        lang = metadata.pop("lang")
        if target_md_file is None or target_md_file == md_src_file:
            build_single_pdf(md_src_file, out_filepath, metadata, lang)

def build_single_pdf(md_filepath, out_filepath, metadata, lang):
    start = perf_counter()
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang).getbuffer())
    set_metadata(out_filepath, **metadata, lang=lang)
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
