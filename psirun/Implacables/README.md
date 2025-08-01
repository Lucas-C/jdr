* Version française : [Implacables (itch.io)](https://lucas-c.itch.io/psirun-implacables)
* English version: [The Restless (itch.io)](https://lucas-c.itch.io/psirun-the-restless)

## Notes
* Version française : _Mad Jack_ / _Mankind Justice_ / _Maître du Jeu_
* English version: _Gary Maniac_ / _Guild of Mentalists_ / _Game Master_

## Build the PDFs

    ./md2pdf.py --watch

## Generate preview images

    mkdir -p preview
    for i in {0..3}; do convert -density 300 PsiRun-Implacables.pdf[$i] -flatten preview/PsiRun-Implacables-page-$i.png; done
    for i in {0..3}; do convert -density 300 PsiRun-TheRestless.pdf[$i] -flatten preview/PsiRun-TheRestless-page-$i.png; done
    cd ../ReglesAdditionnelles/
    mkdir -p preview
    for i in {0..1}; do convert -density 300 PsiRun-ReglesAdditionnelles.pdf[$i] -flatten preview/PsiRun-ReglesAdditionnelles-page-$i.png; done
    for i in {0..1}; do convert -density 300 PsiRun-ExtraRules.pdf[$i] -flatten preview/PsiRun-ExtraRules-page-$i.png; done
