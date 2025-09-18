#!/usr/bin/env python3
# USAGE: ./md2pdf.py [file.md]
import asyncio, logging, sys
from pathlib import Path
from shutil import copyfile
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import markdown2pdf, set_metadata, start_watch_and_rebuild
copyfile(str(DIR / ".." / "cc-by-nc-sa.png"), str(DIR / "img" / "cc-by-nc-sa.png"))

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF :
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/BladesInTheDark/
    DEMON_MD_FILEPATH   := DIR / "BitD-DemonSheet.md",
    RITUELS_MD_FILEPATH := DIR / "BitD-Rituels.md",
    BdlCaL_MD_FILEPATH  := DIR / "BitD-LesBasesDeLaChasseAuLeviathan.md",
    REGLES_MD_FILEPATH  := DIR / "BitD-DeepCuts-NouvellesRegles.md",
    PCsQS_MD_FILEPATH   := DIR / "BitD-PCsQuickSummary.md",
    INT_EN_MD_FILEPATH  := DIR / "BitD-Interrogation.md",
    INT_FR_MD_FILEPATH  := DIR / "BitD-Interrogatoires.md",
)

METADATA = {
    DEMON_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    RITUELS_MD_FILEPATH: { "lang": "fr" },  # TODO before publishing
    INT_FR_MD_FILEPATH: {
        "title": "Blades in the Dark - Interrogatoires",
        "lang": "fr",
        "keywords": ("jdr", "ttrpg", "Blades-in-the-Dark", "roleplay", "aide-de-jeu", "interrogatoire"),
        "description": "Cette aide de jeu propose de développer les scènes d'interrogatoire du jeu de rôle Blades in the Dark, pour en faire des moments cruciaux, où les PJs sont mis sous pression par les Inspecteurs, où ils ont beaucoup à perdre, et où la situation se résoudra par des moments de roleplay mémorables.",
    },
    INT_EN_MD_FILEPATH: {
        "title": "Blades in the Dark - Interrogation",
        "lang": "en",
        "keywords": ("ttrpg", "Blades-in-the-Dark", "roleplay", "module", "interrogation"),
        "description": "This game module develops the interrogation scenes of the tabletop roleplaying game Blades in the Dark, to make them crucial moments, where the PCs are put under pressure by the Inspectors, where they have a lot to lose, and where the situation will be resolved by memorable roleplay moments.",
    },
    BdlCaL_MD_FILEPATH: {
        "title": "Blades in the Dark - Les bases de la chasse au Léviathan",
        "lang": "fr",
        "keywords": ("jdr", "ttrpg", "Blades-in-the-Dark", "aide-de-jeu", "Léviathan"),
        "description": "Une description de comment se déroule la chasse au Léviathan dans l'univers de Blades in the Dark.",
    },
    REGLES_MD_FILEPATH: {
        "title": "Blades in the Dark - Nouvelles règles issues de Deep Cuts",
        "lang": "fr",
        "keywords": ("jdr", "ttrpg", "Blades-in-the-Dark", "aide-de-jeu", "règles"),
        "description": "Traduction de 3 pages de l'excellente extension pour Blades in the Dark de John Harper, Deeps Cuts.",
    },
    PCsQS_MD_FILEPATH: {
        "title": "Blades in the Dark - PCs Quick Summary table",
        "lang": "en",
        "keywords": ("jdr", "ttrpg", "Blades-in-the-Dark", "aide-de-jeu", "table", "characters"),
        "description": "A simple table to keep track of the main characteristics of the Player Characters in Blades in the Dark",
    },
}

def build_pdf(target_md_file=None):
    if len(sys.argv) > 1 and sys.argv[1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[1])
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
