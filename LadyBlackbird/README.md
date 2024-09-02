## Extraction & personnalisation des feuilles de personnage
Au format A4 :

    ./extract_FPs.py

Pour générer `Lady-BlackBird-FPs-2pages.pdf` avec 2 `Lady-BlackBird-FPs.pdf` côte à côte,
avec [pdfly](https://github.com/py-pdf/pdfly) & [pdfrw](https://github.com/pmaupin/pdfrw) :

    pdfly cat Lady-BlackBird-FPs.pdf Lady-BlackBird-FPs.pdf -o Lady-BlackBird-FPs-2pages.pdf
    $opt/pdfrw/examples/subset_booklets.py Lady-BlackBird-FPs-2pages.pdf
    mv booklet.Lady-BlackBird-FPs-2pages.pdf Lady-BlackBird-FPs-2pages.pdf
