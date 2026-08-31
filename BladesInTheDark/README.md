Aides de jeu pour _Blades in the Dark_ :

* [Interrogatoires (itch.io)](https://lucas-c.itch.io/blades-in-the-dark-interrogatoires) - Une aide de jeu pour faire jouer des interrogatoires - [(English version)](https://lucas-c.itch.io/blades-in-the-dark-interrogation)
* [Afflictions (PDF)](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-Afflictions.pdf) - Une aide de jeu pour octroyer des cartes handicapantes à vos joueurs
* [Rituels (PDF)](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-Rituels.pdf) - Quelques idées de rituels d'haruspice
* [Special Items (PDF)](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-SpecialItems.pdf) - Cartes à donner aux joueurs représentant quelques objets spéciaux
* [Feuille de Démon (PDF)](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-FeuilleDeDemon-2up.pdf) - Une aide de jeu pour documenter les démons rencontrés par les PJs, et notamment pour [le _playbook_ du Magicien](https://nebmia.itch.io/the-magician-playbook) - _English version_: [Demon sheet (PDF)](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-DemonSheet-2up.pdf)
* [PCs Quick Summary table](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-PCsQuickSummary.pdf) - A simple table to keep track of the main characteristics of the Player Characters in Blades in the Dark
* [Pouvoir de décorporation (PDF)](https://lucas-c.github.io/jdr/BladesInTheDark/BitD-PouvoirsEthnos.pdf) - Règle supllémentaire pour gérer un pouvoir obtenu par l'un des joueurs de ma campagne
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

<!-- Required for printing: pdf2img2pdf.sh BitD-DemonSheet-2pages.pdf -->

Originally translated from French to English using [translate-shell](https://github.com/soimort/translate-shell):

    trans -s français -to english file://BitD-Interrogatoires.md >BitD-Questioning.md
