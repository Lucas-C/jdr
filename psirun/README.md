## Psi*Run Unknown Armies
Une idée à développer : les joueurs incarnent des Avatars, et quelque chose s'est passé qui les a rendu amnésiques et leur fait perdre leurs pouvoirs progressivement : ils courent contre la montre pour trouver une solution !

Système : on lance toujours 4 dés, +1d si emploi d'un Pouvoir, qu'on répartit entre ces **Risques** :
* **Objectif** : idem que Psi*Run
* **Flashback** : idem que Psi*Run, mais : 1-2-3. on retire autant de jetons TEMPS.
  Souvenir de leur passé humain ou de leur Archétype ?
  -> octroie un jeton RELANCE, permettant de relancer une fois tout ou partie des dés.
* **Environnement** :
    5-6. Décrivez quelque chose en lien avec vos domaines dans le Lieu actuel ou un Lieu proche.
    4. Introduisez un nouveau PNJ, ou comment un PNJ vous aide. Les joueurs ont la parole.
    2-3. Un PNJ vous met des bâtons dans les roues. Retirez un jeton TEMPS. Le MJ a la parole.
    1. Un danger immédiat apparaît sur votre Lieu. Le MJ a la parole.
* **Pouvoir** : idem que Psi*Run, mais :
    1-2. perte de pouvoir -> l'Avatar perd totalement l'usage d'un Pouvoir qu'il a déjà employé.
    Si choix de ce risque alors qu'on a déjà perdu un pouvoir -> on devient **Simple mortel** (condition) : vous ne pouvez plus employer de **Pouvoir**; ajoutez alors à chaque jet le Risque **Blessure**.
* **Blessure** : uniquement pour les simples mortels
    5-6. OK
    3-4. si vous êtes déjà blessé, vous obtenez une blessure grave. Si vous avez déjà une blessure grave, vous mourrez. Sinon, vous êtes blessé -> dé piégé.
    Un joueur peut éviter une blessure en tombant **inconscient**. Avec un minimum d'assistance de ses camarades, l'Avatar reprendra conscience dans le prochain lieu de la Piste où il sera emmené.
    Se soigner nécessite du temps, et les Avatars n'en ont pas, ou de la magie.
    1-2. si vous êtes déjà blessé, vous mourrez. Sinon, vous êtes gravement blessé.

Pas de risque **Poursuite** / **Capture** / **Disparition**.

On configure un chronomètre pour sonner toutes les 20min : retirez alors un jeton TEMPS.
S'il n'y a plus de jetons TEMPS, on remplace le Risque **Flashback** par le Risque **Final** :
    6. Décrivez comment un passage est révêlé vers un lieu antérieur de la Piste.
       Si vous venez d'employer un Pouvoir, vous pouvez choisir d'ascendre et de devenir un Archétype. Les autres joueurs décrivent ce qu'il se passe.
    5. Vous recouvrez des bribes de mémoire sur ce qu'il s'est passé avant votre amnésie. Vous ne décrivez pas la scène, mais vous pouvez en faire part à vos camarades par la voix de votre personnage, en inventant les éléménts que vous souhaitez. Condition : je me souviens.
    3-4. Si vous êtes un Avatar, RAS. Si vous êtes un simple mortel, une opportunité de fuire et de sauver votre peau se présente : si vous la saisissez, décrivez comment. Condition obtenue : adios.
    1-2. L'un des Avatars est blessé. Décrivez qui et comment.

Prévoir des feuilles distintces : Avatar / Simple Mortel + "overlay" Final masquant le risque Flashback.
Prévoirs des jetons pour représenter les différentes conditions : blessé / blessure grave / perte de pouvoir / Archétype / inconscient / mort / je me souviens / adios.

Ajouter à la phase de création un choix d'Archétype & domaines.
Orienter les **Questions** sur ces thématiques :
* les pouvoirs de l'Avatar
* ses forces & faiblesses
* le passé immédiat & lointain : comment êtes-vous devenu Avatar ?

Setting :
* prévoir un Avatar PNJ soigneur
* détailler quelques lieux & PNJs


Autre idée issue de l'article [Otherkind Dice by Vincent Baker](https://lumpley.games/2022/03/14/otherkind-dice/) :

> [Champions] descending into a sorcerous dungeon, which has been spilling malignancy out into the world!

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
