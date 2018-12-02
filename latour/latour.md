<!--
- idées en vrac:
  * mécanique de jeu qui font qu'ils ne peuvent utiliser leurs caracs qu'une fois par étage,
    et "récupèrent" lorsqu'ils descendent d'un niveau, pour les forcer à varier les stratégies
  * idee système de combat: joueur decrit son action : **où** il frappe + **comment** + quel est son **objectif**
    la réussite du jet determine si cet objectif atteind ou non, et empêche une riposte en cas de critique (adversaire passe son tour -> combos)
- ajouter mention auteur + license + ressources
- proposer sur http://troplongpaslu.fr/proposer-un-jeu-de-role-court/ 
-->
# LA TOUR
Vous venez d'arriver au sommet de La Tour, l'immeuble de plusieurs dizaines d'étages le plus mal fâmé du pays.
Vous formez une équipe d'opérations spéciales aguérie, équipée pour l'assaut et entrainée au combat urbain.
Il va maintenant vous falloir descendre les étages jusqu'au rez-de-chaussé, en accomplissant votre mission en chemin...
::::: grid
:::: grid-item
d6 | POURQUOI ETES-VOUS ICI ?
---|-
1  | éliminer le mystérieux occupant du dernier étage
2  | effectuer une descente sur un cartel de la drogue
3  | libérer votre chef mafieux prisonnier
4  | 
5  | 
6  | vous ne vous souvenez pas
::::
:::: grid-item
d6 | COMMENT ETES-VOUS ARRIVE LA-HAUT ?
---|-
1  | en hélicoptère
2  | en parachute
3  | en rappel d'une autre tour
4  | via la nacelle d'un laveur de vitres
5  | l'ascenseur vous a monté jusqu'ici (malgré vous ?)
6  | vous ne vous souvenez pas
::::
:::: grid-item
d6 | PJ: QUEL EST TON SECRET ?
---|-
1  | vous avez un petit parachute !
2  | vous avez des explosifs !
3  | votre fiancée / fils est prisonnier dans la tour !
4  | vous avez un allié dans la tour ! De qui s'agit-il ?
5  | vous avez un pouvoir psi ! Définissez-le maintenant.
6  | vous êtes un ripoux ! Quel est votre véritable objectif ?
::::
::::grid-item
## La Tour
- #étages = **1d6** + #joueurs
- dessinez-la sur une feuille
- 
![La Tour](Fire_Ravaged_Part_-_Nandram_Market_-_Brabourne_Road_-_Kolkata.png)
::::
::::grid-item
## Ton perso
Répartis les valeurs de 1 à 4 parmis :
- commander
- close combat
- furtivité
- mitrailler

Choisis une compétence spéciale au choix:
::: no-bullets
- [ ] éliminer des adversaires à travers les cloisons
- [ ] intimider l'ennemi pour qu'il se rende
- [ ] éviter les balles
:::
![Fusil d'assaut](150311-Z-NI803-314.png)
::::
::::grid-item
## Combat
...
## Assaut de groupe
Lorsque tu progresses dans le bâtiment conjointement,
tu gagnes...
::::
::::grid-item
d6 | MJ: QU'Y A-T-IL A CET ETAGE ?
---|-
1  | il est vide
2  | que des civils
3  | 
4  | 
5  | 
6  | le QG des truands
::::
:::: grid-item
d6 | PJ: TU VEUX OUVRIR CETTE PORTE ?
---|-
1  | 
2  | 
3  | 
4  | 
5  | 
6  | 
::::
:::: grid-item
d6 | MJ: RETOURNEMENT DE SITUATION !
---|-
1  | 
2  | 
3  | 
4  | 
5  | 
6  | 
::::
:::::


<style>
@font-face {
  font-family: PhageRough;
  src: url('fonts/Phage Rough.otf') format('truetype');
}
@font-face {
  font-family: GabrieleL;
  src: url('fonts/gabriele-l.ttf') format('truetype');
}

body {
    font-family: "Courier New", Courier, monospace;
    font-size: .6rem;
    line-height: 1.6;
    color: #444;
    /* Making font rendering prettier: */
    text-rendering: optimizeLegibility !important;
}
h1 {
    font-family: PhageRough;
    font-size: 3rem;
    line-height: 1.2;
    text-align: center;
    display: block;
    margin: 0 auto;
}
section { max-width: 40rem; margin: 2rem auto; }
img { max-width: 100%; max-height: 30rem; display: block; margin: 0 auto; }
table { border-spacing: 0; border-collapse: collapse; table-layout: fixed; }
table, section section { font-size: .5rem; }
h2, thead { font-family: GabrieleL; font-size: 1em; }
td, th { padding: .2rem; }
td { border-top: 1px solid #ddd; }
tr > td:first-child, tr > th:first-child { font-weight: bold; }
ul { margin-left: -1.5rem; }

.grid { max-width: 80rem; margin: 0 auto; }
.grid-item { width: 30%; }
.no-bullets ul { list-style-type: none; margin-left: -2.5rem; }
</style>
<script src="imagesloaded.pkgd.min.js"></script>
<script src="packery.pkgd.min.js"></script>
<script>
var pckry = new Packery('.grid', {
  percentPosition: true,
  gutter: 20
});
imagesLoaded('img', () => pckry.layout());
</script>