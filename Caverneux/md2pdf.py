#!/usr/bin/env python3
# USAGE: ./md2pdf.py [--watch]
import asyncio, logging, sys
from pathlib import Path
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, md2html, start_watch_and_rebuild

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    EN_MD_FILEPATH := DIR / "Caverneux.md",
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/CriticalFondation/
    README_MD_FILEPATH := DIR / "README.md",
)

def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None  # => rebuild all target PDFs
    if target_md_file is None and len(sys.argv) > 1 and sys.argv[-1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[-1])
    for md_src_file in SRC_FILES[2:]:
        if target_md_file is None or target_md_file == md_src_file:
            if md_src_file.name == "README.md":
                with open(md_src_file, encoding="utf8") as md_file:
                    md2html(DIR, md_file.read(), CSS_FILEPATH, lang="fr")
            else:
                build_single_pdf(md_src_file)

def build_single_pdf(md_filepath):
    out_filepath = md_filepath.with_suffix(".pdf")
    pdf = markdown2pdf(DIR, md_filepath, CSS_FILEPATH)
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(pdf)
    start = perf_counter()
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
