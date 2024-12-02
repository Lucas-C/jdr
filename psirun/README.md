## Règles additionnelles
_cf_. [./CustomRules/](./CustomRules/)

    $opt/pdfrw/examples/subset_booklets.py PsiRun-ReglesAdditionnelles.pdf && mv booklet.PsiRun-ReglesAdditionnelles.pdf PsiRun-ReglesAdditionnelles-onePage.pdf

## Setting - Implacables
_cf_. [./Implacables/](./Implacables)

    $opt/pdfrw/examples/subset_booklets.py PsiRun-Implacables.pdf && mv booklet.PsiRun-Implacables.pdf PsiRun-Implacables-onePage.pdf

<!--
With an inversion of pop(0)/pop() on line 58
When available, using pdly x2pdf --layout 2x1 would be nice: https://github.com/py-pdf/pdfly/issues/64
-->

Originally translated from French to English using [translate-shell](https://github.com/soimort/translate-shell):

    trans -s français -to english file://BitD-Interrogatoires.md >BitD-Questioning.md

## Setting - Le Manoir
- Version française : https://lucas-c.itch.io/psirun-le-manoir
- English version: https://lucas-c.itch.io/psirun-the-manor

## Compte-rendus de partie
- https://chezsoi.org/lucas/jdr/psirun/CR_2016-12-18.html
- https://chezsoi.org/lucas/jdr/psirun/CR_2017-12-27.html

    md2html CR_2016-12-18.md > CR_2016-12-18.html
    md2html CR_2017-12-27.md > CR_2017-12-27.html
    java -jar ditaa0_9.jar CR_2017-12-27_piste.txt

<!--
    for cr in CR_*.html; do echo $cr; tq img -a src < $cr; done > rsync.include
    rsync --files-from=rsync.include -rv . ct-lucas:/usr/share/nginx/html/lucas/jdr/psirun/
-->
