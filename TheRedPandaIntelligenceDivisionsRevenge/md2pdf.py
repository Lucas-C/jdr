#!/usr/bin/env python3
# USAGE: ./md2pdf.py [--watch]
import asyncio, logging, os, sys
from pathlib import Path
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import copy_files, export_img, markdown2pdf, md2html, set_metadata, start_watch_and_rebuild
copy_files(DIR, "font:GunnyRewritten")

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    MD_FILEPATH := DIR / "LaVengeanceDesPandasRouxDeLEspace.md"
)

METADATA = {
    MD_FILEPATH: {
        "lang": "fr",
        "title": "La Vengeance des Pandas Roux de l'Espace",
        "keywords": ("jdr", "jeu-de-rôle"),
        "description": "Vous êtes une unité spéciale de Pandas roux ninjas de l’espace ! Vous avez été enlevés sur Terre. Vous êtes très en colère, et vraiment, vraiment badass !!",
    }
}

def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None  # => rebuild all target PDFs
    if target_md_file is None and len(sys.argv) > 1 and sys.argv[-1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[-1])
    for md_src_file in SRC_FILES[2:]:
        metadata = {**METADATA[md_src_file]}
        lang = metadata.pop("lang")
        if target_md_file is None or target_md_file == md_src_file:
            if metadata.pop("pdf", None) is False:
                with open(md_src_file, encoding="utf8") as md_file:
                    md2html(DIR, md_file.read(), CSS_FILEPATH, lang=lang, metadata=metadata)
            else:
                build_single_pdf(md_src_file, metadata, lang)

def build_single_pdf(md_filepath, metadata, lang):
    out_filepath = md_filepath.with_suffix(".pdf")
    prefix = metadata.pop("prefix", None)
    if prefix:
        out_filepath = out_filepath.with_name(prefix + out_filepath.name)
    pdf = markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang, metadata=metadata).getbuffer()
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(pdf)
    start = perf_counter()
    set_metadata(out_filepath, **metadata, lang=lang)
    metadata_duration = perf_counter() - start
    print(f"{out_filepath} has been rebuilt: metadata={metadata_duration:.1f}s")


# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
