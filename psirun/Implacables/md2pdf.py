#!/usr/bin/env python3
import asyncio, sys
from pathlib import Path
from time import perf_counter

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".." / ".."))  # make pdf_utils.py importable
from pdf_utils import add_pdf_annotations, add_to_every_page_dynamic, markdown2pdf, set_metadata, start_watch_and_rebuild

CSS_FILEPATH = DIR / "style.css"

FR_MD_FILEPATH = DIR / "README.md"
FR_OUT_FILEPATH = DIR / "PsiRun-Implacables.pdf"
FR_METADATA = dict(
    title="Psi*Run - Implacables",
    keywords=("jeu-de-rôle", "jdr", "psi*run", "The-Boys"),
    description="Setting pour Psi*Run inspiré de The Boys",
)
# A propos des annotations :
# * pour ce jeu, elles représentent les réflexions de Mad Jack, défunt
# * elles ne seront pas imprimées, et ne doivent donc pas contenir d'informations essentielles
# * mieux vaut les placer dans les marges latérales, car selon si Acrobat/Chrome/Firefox/Sumatra est employé, la position verticale d'une annotation Text change beaucoup ! (Acrobat & Firefox placent l'icône de l'annotation plus bas)
FR_ANNOTATIONS = {
    0: {
        "text_annotations": (
            dict(title="MJ :", x=191, y=165, name="COMMENT",
                 text="Ah c'est pas vrai... Je me suis fait sauter le caisson, vraiment ?"),
            dict(title="MJ :", x=12, y=182, name="COMMENT",
                 text="Leur perte de mémoire ne suffira pas à racheter les crimes de ces enfoirés."),
            dict(title="MJ :", x=180, y=238, name="COMMENT",
                 text="Ce gros bâtard de Doggy, qui fait respecter l'ordre des riches comme un bon super-toutou..."),
            dict(title="MJ :", x=12, y=260, name="COMMENT",
                 text="Ahahah j'imagine leurs tronches lorsqu'ils découvriront plus tard les collants en latex qu'ils portaient :D"),
        ),
    },
    1: {
        "text_annotations": (
            dict(title="MJ :", x=191, y=62, name="COMMENT",
                 text="Ah bah oui merde, j'ai crevé. Au moins je leur ai bien mis dans l'os !"),
            dict(title="MJ :", x=12, y=146, name="COMMENT",
                 text="Madison est réglo. J'espère que sa voix sera entendue dans les médias pour dénonces les Implacables."),
            dict(title="MJ :", x=12, y=205, name="COMMENT",
                 text="Je n'ai jamais pu y pénétrer, seule la présence de Doggy déclenche l'ouverture de ce bunker."),
            dict(title="MJ :", x=12, y=233, name="COMMENT",
                 text="L'hypocrisie de la morale rigoriste de MegaScout est vraiment risible, surtout vu ses hobbys..."),
            dict(title="MJ :", x=191, y=220, name="COMMENT",
                 text="J'espère que Thorgal ne se laissera pas emporter par la colère pour me venger... Tel que je le connais, il voudra faire juger les Implacables par leurs victimes, puis appliquera la sentence lui-même."),
        ),
        "free_text_annotations": (  # easter egg in Acrobat / always visible in web viewers
            dict(x=128, y=239, w=40, h=43, text="", color=(1, 1, 1)),
        ),
    },
    2: {
        "text_annotations": (
            dict(title="MJ :", x=185, y=40, name="COMMENT",
                 text="Ah mes chers freaks vengeurs ! Ces corrompus d'Implausibles vont trembler devant votre juste colère !"),
            dict(title="MJ :", x=12, y=272, name="COMMENT",
                 text="Tu es intelligent, et intègre. Ne te laisse pas submerger par la rage. La justice doit triompher, et je ne veux pas que tu meures."),
        ),
    },
    3: {
        "text_annotations": (
            dict(title="MJ :", x=190, y=136, name="COMMENT",
                 text="Quelle enfumade ! Avec un PDG dans la nature et aussi amnésique qu'un vinyl rayé, Vault Tech va finir par se retourner contre les Implacables..."),
            dict(title="MJ :", x=12, y=168, name="COMMENT",
                 text="On va bien rire lorsque leurs portraits seront diffusés sur tous les écrans de la ville..."),
            dict(title="MJ :", x=190, y=192, name="HELP",
                 text="Et est-ce que justice sera faite ?"),
        ),
    },
}

EN_MD_FILEPATH = DIR / "TheRestless.md"
EN_OUT_FILEPATH = DIR / "PsiRun-TheRestless.pdf"
EN_METADATA = dict(
    title="Psi*Run - The Restless",
    keywords=("tabletop-roleplaying-game", "ttrpg", "psi*run", "The-Boys"),
    description="Setting for Psi*Run inspired by The Boys",
)

EN_ANNOTATIONS = {
    0: (
        "Ah that's not true... I blew my box, really?",
        "Their loss of memory will not be enough to atone for the crimes of these bastards." "That big bastard Doggy, who enforces the order of the rich like a good super-doggie...",
        "Ahahah I can imagine their faces when they later discovered the latex tights they were wearing :D",
    ),
    1: (
        "Ah well yes shit, I had a flat tire. At least I got them right in the bone!",
        "Madison is legit. I hope his voice will be heard in the media to denounce the Implacables.",
        "I have never been able to enter it, only Doggy's presence triggers the opening of this bunker.",
        "The hypocrisy of MegaScout's strict morality is truly laughable, especially given his hobbies...",
        "I hope that Thorgal will not let himself be carried away by anger to avenge me... As I know him, he will want to have the Implacables judged by their victims, then will carry out the sentence himself.",
    ),
    2: (
        "Ah my dear vengeful freaks! These corrupt Implausibles will tremble before your just anger!",
        "You are intelligent and honest. Don't let yourself be overwhelmed by rage. Justice must triumph, and I don't want you to die.",
    ),
    3: (
        "What a smoke! With a CEO in the wild and as amnesiac as a scratched vinyl, Vault Tech will end up turning against the Relentless...",
        "We're going to have a good laugh when their portraits are broadcast on all the screens in town...",
        "And will justice be done?",
    ),
}
for page, fr_annot_dict in FR_ANNOTATIONS.items():
    en_text_annots = EN_ANNOTATIONS[page]
    en_annots = EN_ANNOTATIONS[page] = {}
    en_annots["text_annotations"] = tuple({**annot, "text": text} for annot, text in zip(fr_annot_dict["text_annotations"], en_text_annots))
    if "free_text_annotations" in fr_annot_dict:
        en_annots["free_text_annotations"] = tuple(dict(annot) for annot in fr_annot_dict["free_text_annotations"])


# Waiting for fpdf2.8.2 :
for annot_dict in list(FR_ANNOTATIONS.values()) + list(EN_ANNOTATIONS.values()):
    for name, annots in annot_dict.items():
        for annot in annots:
            if name == "text_annotations":
                del annot["title"]
            if name == "free_text_annotations":
                del annot["color"]


def build_pdf():
    md_filepaths = ()
    # Uncomment one of those lines if you only want to --watch/re-build a single PDF
    build_single_pdf(EN_MD_FILEPATH, EN_OUT_FILEPATH, EN_ANNOTATIONS, EN_METADATA, lang="en"); md_filepaths += EN_MD_FILEPATH,
    build_single_pdf(FR_MD_FILEPATH, FR_OUT_FILEPATH, FR_ANNOTATIONS, FR_METADATA, lang="fr"); md_filepaths += FR_MD_FILEPATH,
    return md_filepaths

def build_single_pdf(md_filepath, out_filepath, annotations, metadata, lang):
    start = perf_counter()
    with out_filepath.open("wb") as out_pdf_file:
        out_pdf_file.write(markdown2pdf(DIR, md_filepath, CSS_FILEPATH, lang=lang).getbuffer())
    add_pdf_annotations(out_filepath, annotations)
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
