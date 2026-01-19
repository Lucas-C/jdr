#!/usr/bin/env python3
# Generate: https://lucas-c.github.io/jdr/all-fonts.pdf
# USAGE: ./gen_pdf_with_all_fonts.py $(git ls-files | grep '\..tf$')
import logging, sys
from pathlib import Path

logging.getLogger("fontTools.ttLib.ttFont").level = logging.INFO

DIR = Path(__file__).parent
sys.path.append(str(DIR))  # make pdf_utils.py importable

from pdf_utils import html2pdf

CSS_FILEPATH = DIR / "style.css"
HTML_FILEPATH = DIR / "all-fonts.html"
PDF_FILEPATH = DIR / "all-fonts.pdf"

def main():
    if len(sys.argv) <= 1:
        raise RuntimeError("Some font files should be passed as arguments")
    css, html = "", ""
    for font_filepath in sys.argv[1:]:
        font_filepath = Path(font_filepath)
        css += f'@font-face {{ font-family: "{font_filepath.name}"; src: url("{font_filepath}"); }}\n'
        html += f'<p style="font-family: \'{font_filepath.name}\'">{font_filepath}</p>'
    with CSS_FILEPATH.open("w", encoding="utf8") as css_file:
        css_file.write(css)
    html = f"""<!doctype html>
    <html lang="en">
        <head>
            <meta charset="utf-8">
            <title>All fonts</title>
            <link rel="stylesheet" href="{CSS_FILEPATH.name}">
        </head>
        <body>
        {html}
        <br>
        <p>Check also : <a href="https://chezsoi.org/lucas/blog/pages/images-libres-de-droits.html#fonts">Images sous licences libres > Fonts</a></p>
        </body>
    </html>"""
    with HTML_FILEPATH.open("w", encoding="utf8") as html_file:
        html_file.write(html)
    bytesio = html2pdf(DIR, html, css_filepath=CSS_FILEPATH)
    with PDF_FILEPATH.open("wb") as pdf_file:
        pdf_file.write(bytesio.getbuffer())
    print(f"{PDF_FILEPATH} generated")

if __name__ == "__main__":
    main()
