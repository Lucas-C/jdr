#!/usr/bin/env python3
# USAGE: ./md2pdf.py [--watch] [file.md]
import asyncio, logging, sys
from pathlib import Path
from shutil import copyfile
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, md2html, set_metadata, start_watch_and_rebuild
copyfile(str(DIR / ".." / "cc-by-nc-sa.png"), str(DIR / "imgs" / "cc-by-nc-sa.png"))

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/CriticalFondation/
    DIAGRAM_MD_FILEPATH   := DIR / "Diagramme.md",
    CARDS_MD_FILEPATH   := DIR / "Cartes.md",
    S1_NOTES_MD_FILEPATH  := DIR / "NotesEpisodes.md",
    HIGHTENSION_MD_FILEPATH  := DIR / "HauteTension-Notes.md",
    README_MD_FILEPATH := DIR / "README.md",
)

METADATA = {
    DIAGRAM_MD_FILEPATH: {
        "lang": "fr",
        "title": "Critical Fondation - Saison 1 - Diagramme et ajouts scénaristiques",
        "keywords": ("jdr", "Critical-Fondation", "jeu-de-rôle", "aide-de-jeu", "diagramme"),
        "description": "Un diagramme reliant les principaux éléments de l'intrigue de la saison 1 du jeu de rôle Critical Fondation, et quelques suggestions d'ajouts au scénario",
    },
    CARDS_MD_FILEPATH: {
        "lang": "fr",
        "prefix": "CriticalFondation-Saison1-",
        "title": "Critical Fondation - Saison 1 - Cartes additionnelles",
        "keywords": ("jdr", "Critical-Fondation", "jeu-de-rôle", "aide-de-jeu", "cartes"),
        "description": "Quelques cartes de jeu supplémentaires pour la saison 1 du jeu de rôle Critical Fondation",
    },
    S1_NOTES_MD_FILEPATH: {
        "lang": "fr",
        "prefix": "CriticalFondation-Saison1-",
        "title": "Critical Fondation - Saison 1 - Notes de MJ",
        "keywords": ("jdr", "Critical-Fondation", "jeu-de-rôle", "aide-de-jeu"),
        "description": "Quelques notes de préparation comme MJ, épisode par épisode, de la saison 1 du jeu de rôle Critical Fondation",
    },
    README_MD_FILEPATH: { "lang": "fr", "pdf": False },  # TODO before publishing
    HIGHTENSION_MD_FILEPATH: { "lang": "fr", "pdf": False },  # TODO before publishing
}

def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None  # => rebuild all target PDFs
    if target_md_file is None and len(sys.argv) > 1 and sys.argv[-1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[-1])
        print(f"{target_md_file=} from sys.argv")
    for md_src_file in SRC_FILES[2:]:
        metadata = METADATA[md_src_file]
        lang = metadata.pop("lang")
        if target_md_file is None or target_md_file == md_src_file:
            if metadata.pop("pdf", None) is False:
                with open(md_src_file, encoding="utf8") as md_file:
                    md2html(DIR, md_file.read(), CSS_FILEPATH, lang=lang, metadata=metadata)
            else:
                build_single_pdf(md_src_file, metadata, lang)

def build_single_pdf(md_filepath, metadata, lang):
    start = perf_counter()
    out_filepath = md_filepath.with_suffix(".pdf")
    prefix = metadata.pop("prefix", None)
    if prefix:
        out_filepath = out_filepath.with_name(prefix + out_filepath.name)
    with out_filepath.open("wb") as out_pdf_file:
        pdf = markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang, metadata=metadata).getbuffer()
        out_pdf_file.write(pdf)
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
