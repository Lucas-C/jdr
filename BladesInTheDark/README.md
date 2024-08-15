[BitD - Interrogatoires (itch.io)](https://lucas-c.itch.io/blades-in-the-dark-interrogatoires)

# How to build PDFs

    pip install -r ../requirements.txt
    ./md2pdf.py

And to build a `BitD-DemonSheet-2pages.pdf` file with 2 `BitD-DemonSheet.pdf` side-by-side:

    pdfly cat BitD-DemonSheet.pdf BitD-DemonSheet.pdf -o BitD-DemonSheet-2pages.pdf
    $opt/pdfrw/examples/subset_booklets.py BitD-DemonSheet-2pages.pdf
    mv booklet.BitD-DemonSheet-2pages.pdf BitD-DemonSheet-2pages.pdf

<!-- Printing required to: pdf2img2pdf.sh BitD-DemonSheet-2pages.pdf --landscape -->

Originally translated from French to English using [translate-shell](https://github.com/soimort/translate-shell):

    trans -s français -to english file://BitD-Interrogatoires.md >BitD-Questioning.md
