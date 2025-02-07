#!/usr/bin/env python3
import asyncio, logging, sys
from pathlib import Path
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF :
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/OriMushi/
    SCENAR1_MD_FILEPATH := DIR / "LesDisparusDuFestivalDuPrintemps.md",
    SCENAR2_MD_FILEPATH := DIR / "LaSepultureDuDaimio.md",
    RULES_MD_FILEPATH := DIR / "OriMushi.md",
)

METADATA = {
    RULES_MD_FILEPATH: {
        "title": "Ori Mushi",
        "lang": "fr",
        "keywords": ("jdr", "ttrpg", "japon", "fantasy", "naruto", "ghibli", "okami", "avatar"),
        "description": "Un jeu de rôle minimaliste inspiré où l'on joue dans un univers de fantasy inspiré du japon médiéval.",
    },
    SCENAR1_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    SCENAR2_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
}


def build_pdf():
    target_md_file = (DIR / sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].endswith(".md") else None
    for md_src_file in SRC_FILES[2:]:
        metadata = METADATA[md_src_file]
        lang = metadata.pop("lang")
        if target_md_file is None or target_md_file == md_src_file:
            build_single_pdf(md_src_file, metadata, lang)

def build_single_pdf(md_filepath, metadata, lang):
    start = perf_counter()
    out_filepath = md_filepath.with_suffix(".pdf")
    with out_filepath.open("wb") as out_pdf_file:
        pdf = markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang, metadata=metadata).getbuffer()
        out_pdf_file.write(pdf)
    set_metadata(out_filepath, **metadata)
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
