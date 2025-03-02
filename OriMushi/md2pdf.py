#!/usr/bin/env python3
import asyncio, logging, sys
from pathlib import Path
from random import randint
from shutil import copyfile
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import add_outline_items, md2pdf, set_metadata, start_watch_and_rebuild
copyfile(str(DIR / ".." / "cc-by-nc-sa.png"), str(DIR / "layout" / "cc-by-nc-sa.png"))

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF :
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/OriMushi/
    SCENAR1_MD_FILEPATH := DIR / "scenarios" / "LesDisparusDuFestivalDuPrintemps.md",
    SCENAR2_MD_FILEPATH := DIR / "scenarios" / "LaSepultureDuDaimio.md",
    RULES_MD_FILEPATH := DIR / "OriMushi.md",
)

METADATA = {
    RULES_MD_FILEPATH: {
        "title": "Ori Mushi",
        "lang": "fr",
        "keywords": ("jdr", "ttrpg", "japon", "fantasy", "naruto", "ghibli", "okami", "avatar"),
        "description": "Un jeu de rôle minimaliste inspiré où l'on joue dans un univers de fantasy inspiré du japon médiéval.",
        "extra_outline": [
            "ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰟⰠⰡⰢⰣⰤⰥⰦⰧⰨⰩⰪⰫⰮ",  # Glagolitic
        ],
    },
    SCENAR1_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    SCENAR2_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
}


def build_pdf():
    target_md_file = (DIR / sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].endswith(".md") else None
    for md_src_file in SRC_FILES[2:]:
        metadata = {**METADATA[md_src_file]}
        lang = metadata.pop("lang")
        extra_outline = metadata.pop("extra_outline", None)
        if target_md_file is None or target_md_file == md_src_file:
            build_single_pdf(md_src_file, metadata, lang, extra_outline)

def build_single_pdf(md_filepath, metadata, lang, extra_outline):
    start = perf_counter()
    out_filepath = md_filepath.with_suffix(".pdf")
    with out_filepath.open("wb") as out_pdf_file:
        with open(md_filepath, encoding="utf8") as md_file:
            md_content = tmpl_subst(md_file.read())
        pdf = md2pdf(DIR, md_content, CSS_FILEPATH, lang=lang, metadata=metadata).getbuffer()
        out_pdf_file.write(pdf)
    set_metadata(out_filepath, **metadata)
    if extra_outline:
        add_outline_items(out_filepath, extra_outline)
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")

def tmpl_subst(md_content):
    # No need for jinja2 for now:
    return md_content.replace("{{ rand_img() }}", f'<img class="size20" alt="" src="cc-imgs/freepik-hand-drawn-asian-style-tattoo-illustration-0{randint(1, 6)}.jpg">')


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
