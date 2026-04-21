#!/usr/bin/env python3
import asyncio, logging, os, sys
from base64 import b64encode
from io import BytesIO
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, StrictUndefined
from qrcode import QRCode
from yaml import load as yaml_load, FullLoader

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR / ".."))  # make pdf_utils.py importable
from pdf_utils import copy_files, html2pdf, modify_html, start_watch_and_rebuild
copy_files(DIR, "font:Candara", imgs={
    "2200_le_jugement_des_dieux/img/cover.png": "2200-lJdD-cover.png",
    "2200_le_jugement_des_dieux/img/d11iblu-a1bec916-ba47-4975-8b6a-1db61470c40e-2.jpg": "2200-lJdD-god.jpg",
    "CyberPunk/big-title.jpg": "CyberPunk.jpg",
    "genius-loci/img/church.png": "genius-loci-church.png",
    "genius-loci/img/pub.png": "genius-loci-pub.png",
    "HavocBrigade/illustrations/Havoc-Brigade-cover.jpg": "HavocBrigade-cover.jpg",
    "HavocBrigade/illustrations/Goblins.png": "HavocBrigade-goblins.png",
    "RunDieRepeat/plasma_gauntlet_by_suldae_d4623vd.jpg": "RunDieRepeat-Invasion.jpg",
    "RunDieRepeat/labyrinthe.png": "RunDieRepeat-Labyrinthe.png",
    "RunDieRepeat/RunDieRepeat-with-goblin.jpg": "",
    "TheRedPandaIntelligenceDivisionsRevenge/cover.png": "LaVengeanceDesPandasRouxDeLEspace.png"
})

SRC_FILES = (
    __file__,
    CSS_FILEPATH := DIR / "style.css",
    JDR_TEMPLATE_FILEPATH := DIR / "jdr.html",
    YAML_FILEPATH := DIR / "jdr-courts.yaml",
)
METADATA = {
    "title": "Catalogue de jeux de rôles courts",
    "keywords": ("jdr", "jeu-de-rôle", "catalogue"),
    "description": "Un catalogue de jeux de rôle courts, à employer en bar à JdR de festival",
}
PDF_FILEPATH = DIR / "CatalogueJdrCourts.pdf"

def build_pdf(target_file=None):
    with (YAML_FILEPATH).open("rb") as yaml_file:
        jdr_courts = yaml_load(yaml_file, FullLoader)
    env = Environment(loader=FileSystemLoader(str(DIR)),
                      lstrip_blocks=True, trim_blocks=True,
                      undefined=StrictUndefined)
    template = env.get_template(JDR_TEMPLATE_FILEPATH.name)
    jdrs_html = ''
    for jdr in jdr_courts:
        qrcode_data_img = 'data:image/png;base64,' + base64_png_qrcode_img(jdr["url"])
        jdrs_html += template.render(jdr=jdr, qrcode_data_img=qrcode_data_img)
    html_doc = build_html_doc(jdrs_html)
    with open(DIR / "index.html", "w", encoding="utf8") as html_file:
        html_file.write(html_doc)
    pdf = html2pdf(DIR, html_doc, CSS_FILEPATH, lang="fr", metadata=METADATA).getbuffer()
    with PDF_FILEPATH.open("wb") as out_pdf_file:
        out_pdf_file.write(pdf)
    print(f"{PDF_FILEPATH.name} built")

def base64_png_qrcode_img(url):
    qr = QRCode()
    qr.add_data(url)
    img = qr.make_image(back_color="transparent")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return b64encode(buffer.getvalue()).decode('ascii')

def build_html_doc(jdrs_html):
    return modify_html(f"""<!doctype html>
    <html lang="fr">
      <head>
        <meta charset="utf-8">
        <title>{METADATA.get("title")}</title>
        <link rel="stylesheet" href="{CSS_FILEPATH.name}">
      </head>
      <body>
      <div class="page">
        <img class="intro" alt="Affiche du bar à JdRs" src="imgs/BarAJdRs.jpg">
        <h3>Licence</h3>
        <a class="float-left license" rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/deed.fr">
        <img alt="Creative Commons License Attribution 4.0 Unported" src="../cc-zero.svg">
        </a>
        <p>
          Ce catalogue a été mis en page par <a href="https://chezsoi.org/lucas/blog/">Lucas Cimon</a> en avril 2026
          pour le <a href="https://laubergedesreveurs.fr/festival-meujeuteries-et-merveilles/">festival M&amp;M</a>.
          <br>
          Il est placé dans le domaine public :
          <a rel="license" href="https://creativecommons.org/publicdomain/zero/1.0/deed.fr">CC0</a>.
          Le code source est sur GitHub : <a href="https://github.com/Lucas-C/jdr/tree/master/catalogue">Lucas-C/jdr</a>.
        </p>
        <h3>Sommaire</h3>
        <ul class="toc" data-tags="h2">
      </div>
      {jdrs_html}
      </body>
    </html>""")

# This conditional ensure that the code below
# does not get executed when calling xreload on this module:
if not __annotations__.get("XRELOADED"):
    build_pdf()
    # The --watch mode is very handy when using a PDF reader
    # that performs hot-reloading, like Sumatra PDF Reader:
    if "--watch" in sys.argv:
        asyncio.run(start_watch_and_rebuild(sys.modules[__name__], *SRC_FILES))
