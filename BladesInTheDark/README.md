* [BitD - Interrogatoires (itch.io)](https://lucas-c.itch.io/blades-in-the-dark-interrogatoires) - Une aide de jeu pour faire jouer des interrogatoires - [(English version)](https://lucas-c.itch.io/blades-in-the-dark-interrogation)
* [Les bases de la chasse au Léviathan](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-LesBasesDeLaChasseAuLeviathan.pdf) - Traduction d'un aide de jeu en 2 pages
* [Deep Cuts - Nouvelles règles](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-DeepCuts-NouvellesRegles.pdf) - Traduction de 3 pages de l'excellente extension de John Harper, [Deeps Cuts @itch.io](https://johnharper.itch.io/deep-cuts)
* [Campagne de JdR Blades In The Dark @chezsoi.org](https://chezsoi.org/lucas/blog/pages/jdr-blades-in-the-dark.html)

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
