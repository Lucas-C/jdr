#!/usr/bin/env python3
import asyncio, logging, sys
from pathlib import Path
from time import perf_counter

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".." / ".."))  # make pdf_utils.py importable
from pdf_utils import add_pdf_annotations, add_to_every_page_dynamic, markdown2pdf, set_metadata, start_watch_and_rebuild

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    # The last one listed below will be rendered at https://lucas-c.github.io/jdr/PsiRun/Implacables/
    EN_MD_FILEPATH := DIR / "TheRestless.md",
    FR_MD_FILEPATH := DIR / "Implacables.md",
)

# A propos des annotations :
# * pour ce jeu, elles représentent les réflexions de Mad Jack, défunt
# * elles ne seront pas imprimées, et ne doivent donc pas contenir d'informations essentielles
# * mieux vaut les placer dans les marges latérales, car selon si Acrobat/Chrome/Firefox/Sumatra est employé, la position verticale d'une annotation Text change beaucoup ! (Acrobat & Firefox placent l'icône de l'annotation plus bas)
FR_ANNOTATIONS = {
    0: {
        "text_annotations": (
            dict(x=191, y=165, name="COMMENT",
                 text="Ah c'est pas vrai... Je me suis fait sauter le caisson, vraiment ?"),
            dict(x=12, y=182, name="COMMENT",
                 text="Leur perte de mémoire ne suffira pas à racheter les crimes de ces enfoirés."),
            dict(x=190, y=245, name="COMMENT",
                 text="Ce gros bâtard de Doggy, qui fait respecter l'ordre des riches comme un bon super-toutou..."),
            dict(x=12, y=260, name="COMMENT",
                 text="Ahahah j'imagine leurs tronches lorsqu'ils découvriront plus tard les collants en latex qu'ils portaient :D"),
        ),
    },
    1: {
        "text_annotations": (
            dict(x=191, y=62, name="COMMENT",
                 text="Ah bah oui merde, j'ai crevé. Au moins je leur ai bien mis dans l'os !"),
            dict(x=12, y=146, name="COMMENT",
                 text="Madison est réglo. J'espère que sa voix sera entendue dans les médias pour dénonces les Implacables."),
            dict(x=12, y=213, name="COMMENT",
                 text="Je n'ai jamais pu y pénétrer, seule la présence de Doggy déclenche l'ouverture de ce bunker."),
            dict(x=12, y=240, name="COMMENT",
                 text="L'hypocrisie de la morale rigoriste de MegaScout est vraiment risible, surtout vu ses hobbys..."),
            dict(x=191, y=220, name="COMMENT",
                 text="J'espère que Thorgal ne se laissera pas emporter par la colère pour me venger... Tel que je le connais, il voudra faire juger les Implacables par leurs victimes, puis appliquera la sentence lui-même."),
        ),
    },
    2: {
        "text_annotations": (
            dict(x=190, y=40, name="COMMENT",
                 text="Ah mes chers freaks vengeurs ! Ces corrompus d'Implausibles vont trembler devant votre juste colère !"),
            dict(x=12, y=272, name="COMMENT",
                 text="Tu es intelligent, et intègre. Ne te laisse pas submerger par la rage. La justice doit triompher, et je ne veux pas que tu meures."),
        ),
        "free_text_annotations": (  # easter egg in Acrobat / always visible in web viewers
            dict(x=132, y=46, w=28, h=28, text="", color=(1, 1, 1)),
        ),
    },
    3: {
        "text_annotations": (
            dict(x=190, y=136, name="COMMENT",
                 text="Quelle enfumade ! Avec un PDG dans la nature et aussi amnésique qu'un vinyl rayé, Vault Tech va finir par se retourner contre les Implacables..."),
            dict(x=12, y=168, name="COMMENT",
                 text="On va bien rire lorsque leurs portraits seront diffusés sur tous les écrans de la ville..."),
            dict(x=190, y=192, name="HELP",
                 text="Et est-ce que justice sera faite ?"),
        ),
    },
}

EN_ANNOTATIONS = {
    0: (
        "Oh, really? I blew my box? Damn!",
        "Their amnesia is not enough punishment for these bastards to atone for their crimes!",
        "That big bastard, enforcing the order of the rich like a good super-doggie...",
        "I love imagining their faces when they discover the photos where they were latex tights :D",
    ),
    1: (
        "Oh yeah, shit, that's true, I died. At least I got them right in the bone!",
        "Madison is legit. I hope his voice will be heard in the media to denounce the Restless.",
        "I have never been able to enter it, only Doggy's presence triggers the opening of this bunker.",
        "The hypocrisy of MegaScout's strict morality is truly laughable, especially given his hobbies...",
        "I hope Thorgal won't get carried away by anger to avenge me... As I know him, he will want to have the Restless judged by their victims, and then carry out the sentence himself.",
    ),
    2: (
        "Ah my dear vengeful freaks! These corrupt Restless will tremble before your just anger!",
        "You are intelligent and honest. Don't let yourself be overwhelmed by rage. Justice must triumph, and I don't want you to die like me.",
    ),
    3: (
        "What a smoke! With a CEO in the wild and as amnesiac as a scratched vinyl, Vault Tech will end up turning against the Relentless...",
        "We're going to have a good laugh when their portraits are broadcast on all the screens in town...",
        "And will justice be done?",
    ),
}
for page, fr_annot_dict in FR_ANNOTATIONS.items():
    fr_annot_dict["title"] = "MJ :"
    en_text_annots = EN_ANNOTATIONS[page]
    en_annots = EN_ANNOTATIONS[page] = {"title": "GM:"}
    en_annots["text_annotations"] = tuple({**annot, "text": text} for annot, text in zip(fr_annot_dict["text_annotations"], en_text_annots))
    if "free_text_annotations" in fr_annot_dict:
        en_annots["free_text_annotations"] = tuple(dict(annot) for annot in fr_annot_dict["free_text_annotations"])


METADATA = {
    FR_MD_FILEPATH: {
        "title": "Psi*Run - Implacables",
        "lang": "fr",
        "out_filename": "PsiRun-Implacables.pdf",
        "annotations": FR_ANNOTATIONS,
        "keywords": ("jeu-de-rôle", "jdr", "psi*run", "The-Boys"),
        "description": "Setting pour Psi*Run inspiré de The Boys",
    },
    EN_MD_FILEPATH: {
        "title": "Psi*Run - The Restless",
        "lang": "en",
        "out_filename": "PsiRun-TheRestless.pdf",
        "annotations": EN_ANNOTATIONS,
        "keywords": ("tabletop-roleplaying-game", "ttrpg", "psi*run", "The-Boys"),
        "description": "Setting for Psi*Run inspired by The Boys",
    },
}


def build_pdf(target_md_file=None):
    if target_md_file and not target_md_file.name.endswith(".md"):
        target_md_file = None
    if len(sys.argv) > 1 and sys.argv[1].endswith(".md"):
        target_md_file = Path(DIR / sys.argv[1])
    for md_src_file in SRC_FILES[2:]:
        metadata = dict(**METADATA[md_src_file])
        lang = metadata.pop("lang")
        out_filepath = DIR / metadata.pop("out_filename")
        annotations = metadata.pop("annotations")
        if target_md_file is None or target_md_file == md_src_file:
            build_single_pdf(md_src_file, out_filepath, annotations, metadata, lang)

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
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
