#!/usr/bin/env python3
# USAGE: ./md2pdf.py [--watch] [file.md]
import asyncio, logging, sys
from pathlib import Path
from random import randint
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO  # avoid useless verbose logging

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import add_outline_items, md2pdf, set_metadata, start_watch_and_rebuild

SCENARII_MD_FILEPATHS = (DIR / "scenarios").glob("*.md")
SRC_FILES = [
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    *SCENARII_MD_FILEPATHS,
    CAMPAGN_MD_FILEPATH := DIR / "Campagne.md",
    GUIDE_DU_MJ_MD_FILEPATH := DIR / "GuideDuMJ.md",
    LIENS_ENTRE_PJS_MD_FILEPATH := DIR / "TableDesLiensEntrePersonnages.md",
    MJ_RECAP_KOMUSOS_MD_FILEPATH := DIR / "MJ-Recap-Komusos.md",
    NOMS_JAP_MD_FILEPATH := DIR / "Noms-japonais.md",
    CHARACTER_CREATION_MD_FILEPATH := DIR / "CreationDePersonnage.md",
    RULES_MD_FILEPATH := DIR / "OriMushi.md",
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/OriMushi/
    PITCH_MD_FILEPATH := DIR / "index.md",
]
if "--offline" in sys.argv:
    del SRC_FILES[-1]  # index.md contains remotely-hosted <img>s

METADATA = {
    RULES_MD_FILEPATH: {
        "title": "Ori Mushi",
        "keywords": ("jdr", "ttrpg", "hopepunk", "japon", "fantasy", "ghibli", "isekai", "komusō", "mushi"),
        "description": "Un jeu de rôle hopepunk dans un univers de fantasy inspiré du japon médiéval, où les joueurs incarnent des komusō, ayant fait vœu d'aider la population, et où des créatures nommées mushis ont donné naissance à la magie.",
        "extra_outline": [
            "ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰟⰠⰡⰢⰣⰤⰥⰦⰧⰨⰩⰪⰫⰮ",  # Glagolitic => peut être converti en cyrillique
        ],
        "html_filename": "OriMushi.html"
    },
    NOMS_JAP_MD_FILEPATH: { "bookmarks": False },  # TODO before publishing
    MJ_RECAP_KOMUSOS_MD_FILEPATH: { "bookmarks": False },  # TODO before publishing
    CHARACTER_CREATION_MD_FILEPATH: { "bookmarks": False, "html_filename": "CreationDePersonnage.html" },  # TODO before publishing
    PITCH_MD_FILEPATH: { "bookmarks": False, "pdf_filename": "Pitch.pdf" },  # TODO before publishing
}


def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None  # => rebuild all target PDFs
    if target_md_file is None and len(sys.argv) > 1 and sys.argv[-1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[-1])
    for md_src_file in SRC_FILES[2:]:
        metadata = {**METADATA.get(md_src_file, {})}
        bookmarks = metadata.pop("bookmarks", True)
        extra_outline = metadata.pop("extra_outline", None)
        html_filename = metadata.pop("html_filename", None)
        pdf_filename = metadata.pop("pdf_filename", None)
        if not target_md_file or target_md_file == md_src_file:
            build_single_pdf(md_src_file, metadata, extra_outline, bookmarks, pdf_filename)
            if html_filename:
                print("Creation de", html_filename)
                (DIR / "index.html").rename(html_filename)

def build_single_pdf(md_filepath, metadata, extra_outline=None, bookmarks=False, pdf_filename=None):
    start = perf_counter()
    if pdf_filename:
        out_filepath = Path(pdf_filename)
    else:
        out_filepath = md_filepath.with_suffix(".pdf")
    with out_filepath.open("wb") as out_pdf_file:
        with open(md_filepath, encoding="utf8") as md_file:
            md_content = tmpl_subst(md_file.read())
        pdf = md2pdf(DIR, md_content, CSS_FILEPATH, lang="fr", metadata=metadata, bookmarks=bookmarks).getbuffer()
        out_pdf_file.write(pdf)
    set_metadata(out_filepath, **metadata)
    if extra_outline:
        add_outline_items(out_filepath, extra_outline)
    print(f"{out_filepath} has been rebuilt in {perf_counter() - start:.1f}s")

def tmpl_subst(md_content):
    # No need for jinja2 for now:
    md_content = md_content.replace("{{ rand_creature_portrait() }}", f'<img class="size20" alt="Peuple éteint" src="cc-imgs/freepik-hand-drawn-asian-style-tattoo-illustration/0{randint(1, 6)}.jpg">')
    md_content = md_content.replace("{{ rand_spiral() }}", f'<img class="size6" alt="Spirale" src="layout/spirals/spiral-{randint(1, 11):02}.jpg">')
    md_content = md_content.replace("{{ rand_plant() }}", f'<img class="size6" alt="Plante" src="cc-imgs/plants-by-LeviGilbert-cc-by/plant{randint(1, 17):02}.png">')
    return md_content


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
