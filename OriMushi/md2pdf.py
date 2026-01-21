#!/usr/bin/env python3
# USAGE: ./md2pdf.py [--watch] [file.md]
import asyncio, logging, sys
from pathlib import Path
from random import randint
from shutil import copyfile
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import add_outline_items, md2html, md2pdf, set_metadata, start_watch_and_rebuild

copyfile(str(DIR / ".." / "cc-by-nc-sa.png"), str(DIR / "layout" / "cc-by-nc-sa.png"))

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF :
    SCENAR1_MD_FILEPATH := DIR / "scenarios" / "LesDisparusDuFestivalDuPrintemps.md",
    SCENAR2_MD_FILEPATH := DIR / "scenarios" / "IlFautProtegerBourgMistral.md",
    SCENAR3_MD_FILEPATH := DIR / "scenarios" / "LesFuneraillesDuDaimio.md",
    GUIDE_DU_MJ_MD_FILEPATH := DIR / "GuideDuMJ.md",
    MJ_RECAP_KOMUSOS_MD_FILEPATH := DIR / "MJ-Recap-Komusos.md",
    NOMS_JAP_MD_FILEPATH := DIR / "Noms-japonais.md",
    CHARACTER_CREATION_MD_FILEPATH := DIR / "CreationDePersonnage.md",
    RULES_MD_FILEPATH := DIR / "OriMushi.md",
)

METADATA = {
    RULES_MD_FILEPATH: {
        "title": "Ori Mushi",
        "lang": "fr",
        "keywords": ("jdr", "ttrpg", "hopepunk", "japon", "fantasy", "ghibli", "komusō", "mushi"),
        "description": "Un jeu de rôle hopepunk dans un univers de fantasy inspiré du japon médiéval, où les joueurs incarnent des komusō, ayant fait vœu d'aider la population, et où des créatures nommées mushis ont donné naissance à la magie.",
        "extra_outline": [
            "ⰀⰁⰂⰃⰄⰅⰆⰇⰈⰉⰊⰋⰌⰍⰎⰏⰐⰑⰒⰓⰔⰕⰖⰗⰘⰙⰚⰛⰜⰝⰞⰟⰠⰡⰢⰣⰤⰥⰦⰧⰨⰩⰪⰫⰮ",  # Glagolitic => peut être converti en cyrillique
        ],
    },
    SCENAR1_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    SCENAR2_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    SCENAR3_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    GUIDE_DU_MJ_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    NOMS_JAP_MD_FILEPATH: { "lang": "fr", "bookmarks": False },  # TODO before publishing
    MJ_RECAP_KOMUSOS_MD_FILEPATH: { "lang": "fr", "bookmarks": False },  # TODO before publishing
    CHARACTER_CREATION_MD_FILEPATH: { "lang": "fr", "bookmarks": False },
}


def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None  # => rebuild all target PDFs
    if target_md_file is None and len(sys.argv) > 1 and sys.argv[-1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[-1])
    for md_src_file in SRC_FILES[2:]:
        metadata = {**METADATA[md_src_file]}
        bookmarks = metadata.pop("bookmarks", True)
        lang = metadata.pop("lang")
        extra_outline = metadata.pop("extra_outline", None)
        if not target_md_file or target_md_file == md_src_file:
            build_single_pdf(md_src_file, metadata, lang, extra_outline, bookmarks)
            if md_src_file.name == "OriMushi.md":
                (DIR / "index.html").rename("OriMushi.html")
            elif md_src_file.name == "CreationDePersonnage.md":
                (DIR / "index.html").rename("CreationDePersonnage.html")
    if not target_md_file:
        # This will be rendered at https://lucas-c.github.io/jdr/OriMushi/
        with open(DIR / "index.md", encoding="utf8") as md_file:
            md2html(DIR, md_file.read(), CSS_FILEPATH, lang="fr")

def build_single_pdf(md_filepath, metadata, lang, extra_outline, bookmarks):
    start = perf_counter()
    out_filepath = md_filepath.with_suffix(".pdf")
    with out_filepath.open("wb") as out_pdf_file:
        with open(md_filepath, encoding="utf8") as md_file:
            md_content = tmpl_subst(md_file.read())
        pdf = md2pdf(DIR, md_content, CSS_FILEPATH, lang=lang, metadata=metadata, bookmarks=bookmarks).getbuffer()
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
