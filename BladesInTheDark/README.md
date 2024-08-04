# Génération des PDFs

    ./md2pdf.py
    pdfly cat BitD-DemonSheet.pdf BitD-DemonSheet.pdf -o BitD-DemonSheet-2pages.pdf
    $opt/pdfrw/examples/subset_booklets.py BitD-DemonSheet-2pages.pdf
    mv booklet.BitD-DemonSheet-2pages.pdf BitD-DemonSheet-2pages.pdf

<!-- Printing required to: pdf2img2pdf.sh BitD-DemonSheet-2pages.pdf --landscape -->
