<!--
Voies :
* le Poète-Sorcier a une VISION de sa propre mort dans l'avenir -> se réalisera-t-elle ?
* principes de conceptions :
    + PROGRESSION : ~3 critères, dont un en lien avec celui d'une autre Voie
    + TRIGGERS :
        pour chaque palier, le PJ doit être AUTONOME pour l'un, l'autre dépend des aventures proposées par le MJ
        sur les 4 de la feuille, un doit être en commun avec une autre Voie
    + le 2e PALIER offre un CHOIX de spécialisation
      (OU: permet au joueur de se créer SA PROPRE TECHNIQUE, avec SON PROPRE SOUS-SYSTEME au choix parmi 3)

Article blog : ambitions de game design, Codex Mushi, Vocables, ...
    + edit GameLoop.jpg & JetsDeDes.png du précédent post

Villes:
* https://www.pathfinder-fr.org/Wiki/Pathfinder-RPG.Villes.ashx
* https://ptgptb.fr/urbanisme

Classification mushis :
* https://www.steamgalaxy.com/design-your-own-game/
* https://mushishi.fandom.com/wiki/Category:Mushi

Next:
* définir quelques éléments de comportement des Colosses & mushis : ils se nourrissent ?
* détailler/revoir Oris/XPs ?
* rédiger section Santé / blessures / mort
* rédiger apprentissage nouveaux Versets : ☑ ☑ ☑ 3 usages réussis => acquis comme Verset +1d6
* nouvel agencement FPs : cf. OriMushi-CombinaisonFPs.jpg
* employer jinja2 pour définir des templates de PNJ :
    + ses Objectifs
    + son Attitude + guide de Roleplay
    + en cas d'alliance avec les PJs : comment il peut les aider / ce qu'il peut leur fournir
    + en cas de conflit avec les PJs...
    + liens avec autres PNJS
* Codex Mushi : inclure des zones de dessin

Gameplay:
+ prévoir que le système (changement de règles...) & les FPs des joueurs (éléments rayés / agraffés / collés...) évoluent au fur et à mesure des parties - Exemples / idées :
    * les règles MENTENT : la transformation en Oni est plus rapide que prévue !
        -> et provoque un changement de FP !
    * les feuilles de Voie initiales sont REMPLACÉES suite à un événement "BIG BANG"

Twists:
+ les PJs mettent la main sur un recueil de haïkus, celui que les joueurs ont composé !
  -> c'est un des objectifs de l'Artiste-Conteur pour passer au palier 3
+ une fois 5 ou 6 Colosses placés sur la carte, il est aisé d'imaginer un symbole à partir de ces points.
  Le MJ peut alors employer ce symbole dans une enigme...

Lore:
* https://fr.wikipedia.org/wiki/Clou_de_fondation
* donner un rôle aux SINGES ? (présents sur maps ForestShrineFestival & WizardPrison)

À lire : Mener des parties de jeu de rôle -> Fiches-de-synthese-A4.pdf
* [x] Créer un scénario, page 31
* [ ] Enseigner un jeu, page 93
* [ ] Incarner des PNJ, page 125
* [ ] Dompter la linéarité, page 159
* [ ] Partager la narration, page 381

Mise en page :
- trouver un symbole pour les Oris
- Ajouter de jolis ornements en header/footer de pages
    Chinese landscape painting: https://github.com/LingDong-/shan-shui-inf
    https://github.com/watabou/CompassOS
    https://github.com/emmiegit/canji : procedural kanji generator (Python)
    and/or https://github.com/AdrianMargel/glyphs
    https://github.com/CiaccoDavide/Alchemy-Circles-Generator
    or https://github.com/AdrianMargel/alchemy-circles
    or https://game-dev-goose.itch.io/magic-circle-generator ($20)
- Expliquer en détail le fonctionnement des cases à cocher de la FP / les étapes de la créa de PJ
- formatter les règles (jets + tables) en une seule page A4
- SpellCheck
- Illustrations.pdf : add section titles + more images of equipments & places
- Remplacer Odachi par typo / font plus adaptée / lisible pour dyslexiques ?
- Ajouter des boutons dans les scénarios pour lire des morceaux de musique ?

Com'
* transformer https://lucas-c.github.io/jdr/OriMushi/ en un "hub" promouvant un kit de découvert et la version papier
* exposer une 2e page web référencée dans le livre, avec tous les liens vers les ressources PDFs du jeu
* https://www.reddit.com/r/Mushishi

Refs for illus hand-drawn-asian-style-tattoo-illustration*.jpg :
<a href="https://www.freepik.com/free-vector/hand-drawn-asian-style-tattoo-illustration_79302251.htm#fromView=keyword&page=1&position=19&uuid=8d653419-e11f-4883-a72c-8510e20dab2e&query=Japanese+Retro">Image by pikisuperstar on Freepik</a>

Illustrations not free:
* https://www.deviantart.com/niloadoptables/art/open-Ai-Adoptable-5366-1139413431 - girl - 8$
* https://www.instagram.com/maruti_bitamin

Contacter Gulix pour review / partie test ?
-->

# Ori Mushi

::::: rules
<img class="size10" alt="" src="cc-imgs/japan_flag_cool_wallpaper_by_Ir_IA_cc-by-nc_noBg.jpg">

<br>

Un jeu de rôle _hopepunk_ dans un univers de _fantasy_ inspiré du japon médiéval,
où les joueurs incarnent des komusō, ayant fait vœu d'aider la population,
et où des créatures nommées _mushis_ ont donné naissance à la magie.

**Inspirations**: Mushishi, Shadow of the Colossus, Avatar le maître de l'air, Naruto, Princesse Mononoké, le Voyage de Chihiro, Zelda, Ori & the Blind Forest...

::: web-only
- Version PDF de ces règles: [OriMushi.pdf _(19 pages, 4,4 Mo)_](OriMushi.pdf)
:::

- Feuille de komusō : [FeuillePersonnage.pdf](OriMushi-FeuillePersonnage.pdf)
- Aides de jeu :
    + [OriMushi-VoiesDesPersonnages.pdf](character-sheets/OriMushi-VoiesDesPersonnages.pdf)
    + [VoeuxDesKomuso.pdf](layout/OriMushi-VoeuxDesKomuso.pdf)
    + [GameLoop.jpg](layout/GameLoop.jpg)
    + [Illustrations.pdf _(16 pages, 40 Mo)_](OriMushi-illustrations.pdf)
- Feuille de komusō pour partie de 30min : [FeuillePersonnageExpress.pdf](character-sheets/OriMushi-FeuillePersonnageExpress.pdf)
- Articles sur mon blog à propos de ce jeu : [tag ori-mushi @ chezsoi.org](https://chezsoi.org/lucas/blog/tag/ori-mushi.html)

::: page-break
:::

### Sommaire

<br>
<ul class="toc" data-tags="h2"></ul>

::: page-break
:::

## Les terres connues
Le monde d'Ori Mushi est une forme de **Japon médiéval avec des éléments fantastiques** :
* la **magie** existe, elle opère par la parole, et est enseignée à travers différents **Vocables**.
L'énergie magique provient du **Mana**, provenant des **mushis**, des créatures élémentaires invisibles...
* tout individu possède un potentiel maveillant enfoui, un **Oni**, qui peut s'éveiller, le dévorer et le transformer en **démon**.
* les **komusō** sont un ordre respecté dans toutes les terres connues.

Les terres connues comportent encore de nombreuses traces des **Temps Antiques**,
une ère dont les légendes sont encore très présentes dans les esprits,
inspirée des mythes greco-romains et égyptiens.

## Histoire
#### Les temps antiques
Il y a environ mille ans : <!-- Inspi : Dark Souls opening https://www.youtube.com/watch?v=e0l73vAlEBQ -->
* les **dragons** veillent sur le monde et guident les empereurs.
* cette époque voit les plus grandes merveilles être conçues :
la **Cité aux Mille Pages**, une véritable ville-bibliothèque; le **Théâtre des Cieux** de l'artisan-ingénieur **Vitruve**, immense et mobile; la **Tour de l'Infini**...
* la **Sculpteuse** conçoit initiallement les **Colosses** pour qu'ils déclament à travers les terres connues les Versets du **Poète Endeuillé**.
* fondation de l'ordre des **komusō**.
#### La Guerre de l'Oubli
Il y a environ un siècle :
* une armée de **Onis**, des démons, ravage les terres connues, menés par l'empereur fou, **Enkidu**.
Ils massacrent les dragons, ainsi que tout un peuple : le **peuple éteint**.
Les grandes merveilles disparaissent.
* les premiers **Poètes-Sorciers** maîtrisent la magie du **Verbe**, et transmettent leurs Vocables pour lutter contre les Onis.
* les **Onis** sont finalement vaincus. Certains disent grâce à un enfant, **Gilga**, qui commandait aux Colosses. D'autres racontent qu'ils ont été enchaînés dans les cœurs des hommes.
#### Récemment
Ces dernières années :
* **Hisaishi Inoue**, capitaine en chef des bateliers.
* **Oma la Cueilleuse de Mots**, une Poètesse-Sorcière, a été élue par les forestiers pour remplacer le précédent empereur des Basses Plaines. Elle siège au conseil des sages de la ville de Nippur.
* l'**Empereur des Hauts Plateaux** est mort, de tristesse à ce qu'on raconte, sans descendance. 

## Géographie & peuples
Ces lieux & régions sont des points de repère essentiels dans les terres connues :
* les **Basses Plaines** : région de vallées verdoyantes et de nombreuses rivières. Deux peuples y cohabitent : les **forestiers**, qui mènent une vie sédentaire rurale; et les **bateliers**, nomades dont les escadres de chars à voile se déplacent aussi bien dans les plaines herbeuses que sur la mer.
* les **Hauts Plateaux** : région montagneuse, découpée en de multiples provinces. L'**Église de la Connaissance** y est très influente, promouvant un progrès scientifique et industriel.
* **Uruk** est la plus grand ville des Hauts Plateaux, capitale du Pays de la Mer. D'immenses industries s'y sont installées le long de ses immenses falaises.
* **Bilgamesh** est un Colosse encore actif, un géant humanoïde qui arpente les Basses Plaines. Une épreuve de courage des bateliers est de l'escalader.
* de nombreux **temples** et **monastères** parsèment les terres connues. Parfois très anciens, ils ont été érigés pour vénérer des divinités shintoïstes. La plupart sont aujourd'hui devenus des lieux dédiés aux Sciences, où diverses écoles de **Moines-Scientifiques** s'isolent pour approfondir leurs théories, dans des domaines aussi variés que l'astronomie, la botanique, la philosophie, les mathématiques... La majorité sont affiliés à l'Église de la Connaissance, mais pas toutes.

<img class="full-width" alt="" src="cc-imgs/vecteezy_japanese-style-link-art-border-frame_cc-by.jpg">

Les terres connues ne sont volontairement **pas** décrites en détails afin de :
* vous permettre, MJ & joueurs, de les détailler par petites touches, au fur et à mesure de vos parties.
* d'inclure toutes les références que vous souhaitez à des univers de fiction existants, qu'il s'agisse de lieux, de personnages, d'organisations...

{{ rand_plant() }}

::: page-break
:::

## Mushis
Un **mushi** est un organisme vivant **invisible** aux yeux des humains.
Il en existe de différentes espèces, et ils tissent des liens essentiels avec les autres êtres vivants, de manière **symbiotique** : tantôt sources de nourriture, tantôt protecteurs de plantes et d'animaux.

Les mushis ne semblent pas doués de conscience.
Ils ne sont ni mauvais ni bienveillants, mais contribuent
à l'équilibre des environnements naturels où l'homme est absent.

Bien qu'invisibles, leurs morphologies sont tantôt semblables à des plantes, à des insectes, à de petits oiseaux, ou à des champignons.

Les mushis produisent naturellement du **Mana**, l'énergie permettant la magie.
La plupart réagissent à **la musique**, aux métaux **argentés**, et à **la lune** :
certains se reproduisent en émettant des **spores** durant les nuits de pleine lune.
où ils convergent et se réunissent en masse à certains endroits mystérieux.
On appelle cela un **banquet des mushis**.

<br>

_Mot-clefs : invisible, étrange, nature, symbiose, fragile, paisible, surnaturel_

<br>
<img class="size20" alt="Mushi" src="cc-imgs/a-handbook-of-cryptogamic-botany-1889-page-415.jpg">

### Codex mushi
Les joueurs dans le groupe qui jouent des Mushishis se voient remettre une feuille de **Codex mushi vierge**.
S'il y a deux Mushishis, chacun reçoit un Codex vide, et les joueurs se répartissent les six familles entre eux, afin de se spécialiser chacun dans trois d'entre elles.
Si le groupe ne comporte aucun Mushishi, alors la tenue du codex est à la charge de l'ensemble des joueurs.

Le MJ dispose également du **Codex mushi complet**,
contenant les détails de tous les mushis connus.
Le MJ est également libre d'en imaginer d'autres.
Les Mushishis en inventent eux-même de nouveaux à la seconde phase de leur Voie.

<img class="size6" alt="Mushi insecte" src="cc-imgs/kage_no_mushi_by_the_fake_dexter_cc-by-nc-greyscale.jpg">


## Onis
Dans les terres connues, tout individu possède un démon intérieur, un **Oni**.
Ce Oni se nourrit de colère, de frustration, de peurs.

Chez la plupart des gens, ce Oni reste en sommeil et ne se développe jamais.

À l'inverse, certains individus choisissent de nourrir ce Oni,
pour obtenir en échange une grande puissance.
Cette voie mène néanmoins à une transformation en un véritable **démon**.

<br>

<img class="size14 float-left" alt="Réveil d'Oni" src="cc-imgs/demon_blood_by_amigos21_cc-by.jpg">

_Mot-clefs : enragé, hurlement, bestial, monstre, terrifiant, agressif, sidérant, danger_

::: page-break
:::

## Colosses
<!-- Également nommés **dogū** -->
Ce sont de gigantesques et mystérieux géants de pierre, en partie scultpés.
Certains sont endormis, d'autres errent, répétant des gestes ou des trajets dont le sens s'est perdu à travers les âges...

Peu de choses sont connues sur ces statues géantes.
Ils réagissent à la **musique**, en général en l'écoutant,
et parfois en répondant par un chant plaintif.

Les Colosses inertes, que plus rien n'anime, semblent être un lieu de prédilection des mushis.

Certains bas-reliefs de temples antiques, ou sur les Colosses eux-mêmes,
mentionnent leur lien avec un énigmatique **Poète Endeuillé**.

<img class="size25" alt="Élémentaire de pierre" src="cc-imgs/DnD_Stone_Elemental-LadyOfHats-cc0.png">

<!-- SOTC Colossus reveals:
1. https://youtu.be/U8rn9BZXaKY?t=885
2. https://youtu.be/U8rn9BZXaKY?t=1185
3. https://youtu.be/U8rn9BZXaKY?t=1438
4. https://youtu.be/U8rn9BZXaKY?t=1716
5. https://youtu.be/U8rn9BZXaKY?t=2005
-->

De nombreuses légendes circulent à leur sujet.
Certains disent en avoir vu s'affronter.
D'autres racontent avoir vu un Colosse entretenir un jardin de fleurs.

_Mot-clefs : gigantesque, lent, inarrêtable, massif, antique, minéral, lourd, tremblement, errance_

::: page-break
:::

## L'Église de la Connaissance
Cette influente institution promeut **le progrès scientifique et industriel**.

Cette organisation partage certaines caractéristiques d'une religion :
* le progrès technologique est **sacralisé**, mis en exergue comme la salut de l'humanité, et ses partisans exhortent à avoir **foi** en la Science et la grande Révolution Industrielle qui se déploie.
* la spiritualité et la magie sont **bannies** comme des absurdités barbares. Les **livres** qui y font référence sont **brûlés**.
* il n'y a pas de texte sacré, mais les **écrits scientifiques** sont portés aux nues, et célébrés comme les trésors les plus précieux de l'humanité.
Cette instution constitue un réseau très bien organisé :
* différents **lieux** lui sont dédiés, en ville comme dans des lieux reculés : **temples et monastères** qui sont autant d'instituts de recherche, mais aussi **usines de production** et carrières d'extraction de ressources
* une **hierarchie de scientifiques** dirige cette église : **barons et capitaines de l'industrie**, **doyens d'université**, **ingénieurs en chef**...
* l'église encourage les **bonnes œuvres**, et structure plusieurs initiatives de bienfaisance sociale : aumône, aide alimentaire aux plus démunis, hébergement d'urgence, médecine gratuite, etc.

L'Église de la Connaissance a de nombreux détracteurs, qui lui reprochent notamment
sa censure proche d'une **Inquisition**;
la réalisation d'**expérimentations sur les défavorisés** qui bénéficient de ses bonnes œuvres;
la **destruction d'environnements et la pollution** qu'entraînent les industries intensives qu'elle promeut.

Aujourd'hui, l'église est très influente dans les provinces des Hauts Plateaux,
et de plus en plus également dans les villes des Basses Plaines.

_Mot-clefs : dogme, rigueur, usines, mécanique, productivisme, steampunk_

::: page-break
:::

## Vocables
Les Vocables sont des languages mystiques ancestraux permettant de maîtriser différentes formes de magie, correspondant aux familles de mushis.

Voici les principaux Vocables connus :

::: same-size-2-cols

**Gravité** : intensifier ou supprimer la gravité dans une zone proche. | **Mimétisme** : agir sur les reflets, dupliquer un objet...
-|-
**Perceptif** : podifier les perceptions, se rendre imperceptible, avoir une odeur attirante, être effrayant à en hérisser le poil, etc. | **Plantes** : faire pousser des plantes (arbres, lianes, fleurs...) extrêmement vite, modifier un objet en bois...
**Sommeil** : l'induire ou empêcher de dormir, agir sur les rêves... | **Téléportation** : déplacement instantanné à courte distance de soi, d'un objet, d'un adversaire...

<img class="size10" alt="Cercle magique" src="cc-imgs/magic_circle_2_by_nnao_cc-by-nc-sa.jpg">

{{ rand_spiral() }}

:::

::: page-break
:::

## Les dragons
ToDo / À rédiger

## Le peuple éteint
{{ rand_creature_portrait() }}

<br><br><br>
<img class="size16" alt="" src="cc-imgs/kuma_by_hijodelopio_cc-by_BW.jpg">

::: page-break
:::

## Les joueurs incarnent des komuso
Avant que les joueurs ne créent leurs personnages,
informez-les de la nature de leur groupe :
il vont incarner des **komusō**.

Les personnages des joueurs viennent de conclure un apprentissage d'élite
(ou leur reconversion) dans un domaine, quel qu'il soit : artisan, savant, sorcier...

En échange de cette formation d'excellence qu'ils ont reçu,
ils ont accepté ensuite, pendant un an, d'assumer la fonction de komusō,
et pendant **un an** de former un groupe suivant les préceptes de cette charge :

<br>

* **Vœu d'Errance** : un komusō ne reste jamais plus de **trois nuits** dans un lieu, à moins d'une urgence vitale.
* **Vœu de Pauvreté** : un komusō ne conserve **jamais d'argent** pour lui. Il subsiste de la générosité des autres, qui leur offrent en général volontier le gîte et le couvert. Un komusō peut faire du troc.
* **Vœu d'Assistance** : un komusō accepte toujours d'**aider quelqu'un en difficulté**, de lui porter secours.
* **Vœu d'Impartialité** : un komusō se doit d'être **impartial** et **juste**. En cas de conflit, sans qu'ils ne possèdent la moindre autorité officielle, les komusō sont parfois sollicités comme juges impartiaux.
* **Vœu de Préserver la Vie** : un komusō ira jusqu'à **se battre pour une vie**. Il protège également **la nature**, animaux, plantes et autres créatures.

<img class="size20" alt="Vœux des komusō" src="layout/VoeuxDesKomuso.jpg">

En-dehors de ce code moral, les komusō sont d'origines très diverses.
Ils ont souvent des connaissances et des compétences très complémentaires au sein d'un groupe,
pouvant parfois même provoquer des tensions.

<br>
<img class="size10 float-left" alt="Daïmio" src="cc-imgs/Dakuan_by_daudiomultimedia_cc-by-nc_BW.jpg">

Ils doivent tous respect et obéissance à un **daïmio**,
qui a sélectionné les membres du groupe des komusō, et à qui ils rendent compte.
Il peut parfois leur demander d'accomplir certains missions spécifiques.
Pour les personnages des joueurs, son nom est **Mokabé**.

<br>

Au terme de leur mission de komusō, l'appréciation finale du daïmio sera cruciale pour la poursuite de carrière des komusō dans leur activité.

<br>

Les Vœux des komusō sont sources de points d'expériences :
un joueur sauvant une vie en danger ou épargnant un adversaire meutrier gagne **+1 Ori**.

::: page-break
:::

## Créer son komuso
Chaque joueur :
* choisit une **Motivation**
* choisit une **Voie**
* choisit et coche **3 compétences**
* choisit un Artefact
* choisit une mauvaise habitude : _section en cours de rédaction..._
* débute à 0 dans les jauge d'Ori & Oni
* (selon Voie) débute avec 3 Mana : il remplit 5 cases de la jauge correspondante
* (si Poète-Sorcier) débute avec un Vocable et un Verset maîtrisé

::: page-break
:::

### Motivation
Pourquoi es-tu devenu komusō ?

Coche l'une des options proposées sur ta feuille de personnage,
puis détaille ton histoire en quelques phrases au dos.

::: borderless with-headings text-small left-align-col-1 left-align-col-2
Motivation | Vœu personnel | Gain d'Ori
-|-
Aider mon prochain | Vœu d'assistance | Lorsque vous sauvez ou changez positivement & significativement la vie de quelqu'un
Devenir daïmyo | Vœu d'impartialité | Lorsque vous contribuez significativement à ce que justice soit faite
Devenir un maître | Vœu d'excellence | Lorsque vous surpassez un maître ou remportez une compétition
Expier mes erreurs | Vœu de réparation | Lorsque vous résolvez un conflit / réparez un dysfonctionnement majeur
Humilité | Vœu de discrétion | Lorsque résolvez une situation sans attendre de reconnaissance et sans qu'aucun PNJ n'ait connaissance de vos actions
Voyager | Vœu d'exploration | À chaque découverte d'un lieu oublié ou secret
:::

À chaque motivation est associé un vœu personnel **suggéré** : vous êtes libre d'en choisir un autre.
Le **vœu personnel** est l'un des 5 vœux des komusō, ou un 6<sup>e</sup> vœu qui lui est propre,
qui guide votre personnage dans sa vie.

::: page-break
:::

### Voies
::: same-size-2-cols

_cf._ [OriMushi-VoiesDesPersonnages.pdf](character-sheets/OriMushi-VoiesDesPersonnages.pdf)

#### Maître-Artisan
Je veux maîtriser toutes les formats d'artisanat, pour construire les objets les plus beaux et utiles,
et leur insuffler un peu d'âme.

Matériaux : n'importe quel _loot_ dont le komusō justifie la pertinence, pour de l'artisanat ou de l'alchimie,
mais **JAMAIS** 2x le même.

<!-- Mystère/objectif "fil rouge" : découvrir l'origine des Colosses, réveiller un -->

#### Artiste-Conteur
Je raconte de manière captivante les plus incroyables histoires.
Je sais un captiver un public avec jonglage, tours de passe-passe, ombres chinoises, etc.

<!-- Mystère/objectif "fil rouge" : découvrir la véritable histoire du Poète Endeuillé / sa tombe / des Colosses -->

#### Mushishi
J'étudie et m'efforce d'apaiser mushis et Colosses.

Les mushis étant invisibles, chaque Mushishi a sa propre manière de les détecter : grâce à des lunettes spéciales, en fermant les yeux et en se basant sur son odorat, ou bien en les caressant délicatement, etc.
Au joueur de déterminer comment son komusō perçoit les mushis, et de l'indique sur sa feuille de Voie.

Un Mushishi peut employer sa compétence **Percevoir les mushis** pour détecter leur présence dans un lieu.
Il effectue alors un jet de dé, et selon le résultat le MJ lui indique s'il perçoit ou non des mushis à proximité. Un résultat « mais » peut signifier que le Mushishi perçoit autre chose, qu'il pense détecter un mushi mais qu'il se trompe, etc.

Un Mushishi peut employer sa compétence **Connaissance des mushis** pour tenter d'identifer un mushi, lorsqu'il a détecté la présence de l'un d'eux.
Il effectue alors un jet de dé, et le meilleur dé obtenu indique le nombre de caractéristiques que le MJ lui indique concernant ce mushi.

<!-- Mystère/objectif "fil rouge" : ? TODO -->

#### Poète-Sorcier
Je maîtrise l'art du Verbe, et les Vocables magiques.

<!-- Mystère/objectif "fil rouge" : découvrir la véritable histoire du Poète Endeuillé / sa tombe -->
:::

::: page-break
:::

### Artefacts
Les artefacts sont des objets spéciaux uniques, magiques ou d'excellente facture,
et leur possesseur les manipule avec virtuosité.
Deux PJs ne peuvent pas avoir le même. 

<br>

**Bâton télescopique** : peut être employé tout autant comme une arme, que comme un moyen de prendre de la hauteur | **Grappin téléscopique** : comme dans Zelda ou Batman | **Arc à flèches soniques** : propulse des flèches éthérées, illimitées et aux multiples propriétés : elles peuvent sonner l'alarme, assourdir, trancher en deux de petits objets, etc. 
-|-
**Amulette de feu** : produit d'intenses flammes | **Gant de bourrasque** : projette de l'air | **Cape d'invisibilité** : permet de camoufler une seule personne, ne supprime pas le son
**Instrument de musique** : dont la sonorité appaise toute créature | **Grande plume volante** | **Masque** permettant de changer de visage
**Guide d'identification de mushis** | **Lunettes à mushis** | **Katana tranche-tout**

::: page-break
:::

### Liens entre komuso
Au terme de cette étape de la création des komusō,
chaque personnage aura créé **deux liens** avec d'autres membres du groupe.

Cette étape se déroule sous forme d'une « chaîne » entre joueurs :
* un premier joueur lance un dé pour déterminer avec quel autre komusō du groupe son personnage aura un lien.
Il propose ensuite au joueur partenaire une nature de lien dans la table suivante.
Si le joueur décline, il doit proposer un autre lien.
Lorsque les deux joueurs sont d'accord, la ligne correspondante est cochée dans la table, et ils répondent ensemble aux questions selon le _modus operanti_ décrit dans la section suivante.
* c'est ensuite au tour du joueur du komusō qui vient d'être tiré au hasard.
Ce joueur effectue lui aussi un jet de dé pour sélectionner un autre personnage du groupe, à l'exception de celui du premier joueur.
Il choisit ensuite la nature de ce lien dans la table suivante parmi les options non encore sélectionnées, coche la ligne correspondante, et les deux joueurs répondent aux questions.
* le joueur qui vient d'être tiré au hasard effectue lui aussi un jet de dé pour sélectionner un autre personnage du groupe, à l'exception de ceux des premier et second joueurs.
* et ainsi de suite jusqu'au dernier joueur, dont le komuso aura automatiquement un lien avec celui du premier joueur

Pour chaque **lien**, trois questions sont posées.
Le joueur qui n'a pas choisit la nature du lien commence à répondre à l'une des question.
Puis son partenaire répond à une second question.
La parole revient enfin au joueur initial pour la question restante.

<!-- Les objectifs :
* créer du lien entre PJs
* initier du worldbuilding collectif, sachant que les joueurs n'ont encore quasi aucune refs
-->

::: borderless with-headings text-small reduced-vertical-margin large-col-3
☑ | Nature du lien | Questions
-|-
▢ | Originaires du même lieu | <ul><li>Était-ce dans les Basses ou Hautes Plaines ? Un village forestier, un quartier de ville, une escadre de bateliers ?</li><li>Qu'avez-vous partagé en ce lieu, qui vous a marqué ?</li><li>En quoi ce lieu a-t-il changé aujourd'hui ?</li></ul>
▢ | Élèves du même maître | <ul><li>Quel est son nom et son domaine d'expertise ?</li><li>Est-il décédé ou toujours vivant ?</li><li>Êtes-vous en compétition, ou coopérez-vous pour transmettre son enseignement ?</li></ul>
▢ | Ancêtre commun ayant participé à la Guerre de l'Oubli | <ul><li>Quel était son nom et sa profession ?</li><li>Comment at-il/elle participé à la guerre ?</li><li>Que vous a-t-il/elle légué ?</li></ul>
▢ | Voyagez ensemble depuis longtemps | <ul><li>Quelle sale habitude insupporte ton compagnon ?</li><li>Quel est l'endroit le plus mémorable visité ensemble ?</li><li>À quelle occasion lui as-tu déjà sauvé la vie ?</li></ul>
▢ | Assisté à un banquet de mushis ensemble | <ul><li>Happé dans le _flow_ des mushis, comment as-tu réagi ?</li><li>Tu as versé du sang, pourquoi ?</li><li>Tu t'es reveillé près de ton camarade : où ça ?</li></ul>
▢ | Victimes du même Oni | <ul><li>Qui était ce Oni avant de devenir un démon ?</li><li>L'un de vous l'a affronté, comment ?</li><li>Cela s'est fini dans les larmes, pourquoi ?</li></ul>
▢ | Relation d'amour | <ul><li>De quel forme d'amour s'agit-il ?</li><li>Qui la ressent pour qui ?</li><li>Comment vivez-vous cet amour au quotidien ?</li></ul>
▢ | Motivations proches | <ul><li>Quel objectif avez-vous en commun ?</li><li>Sur quoi n'êtes-vous pas en accord ?</li><li>Êtes-vous en compétition, ou coopérez-vous ?</li></ul>
▢ | Parentalité | <ul><li>Quel est votre lien de parentalité ?</li><li>Quel souvenir d'enfance partagez-vous ?</li><li>Quel lien avec votre famille conservez-vous avec vous ?</li></ul>
▢ | Lien secret | **Surprise !** Le MJ vous expliquera votre lien en apparté.
:::

<!-- Autres idées : Ont jeté les armes (À quelle bataille avez-vous tous deux participés ?) -->

::: page-break
:::

#### Lien secret
Le MJ prend en apparté les deux joueurs,
et leur révêle que l'un des komusō est un **mushi clone** de l'autre !

Depuis le clonage, les deux personnages ont probablement adopté des signes distinctifs,
les rendant légèrement dissemblables l'un de l'autre.
Ou bien peut-être prétendent-ils être jumeaux.
Mais ils disposaient en tout cas d'un corps et de souvenirs identiques au moment où le mushi est né.

Depuis, le mushi clone a entièrement est devenu une personne à part entière.
Il est complètement indépendant de son modèle et en tous points humain.

Répondez à ces questions :
* quel personnage est "l'original" ? Ou bien l'ignorez-vous ?
* il y a combien de temps le clone est-il né ?
* pourquoi avez-vous décidé de voyager ensemble ?

::: page-break
:::

## Jets de dés
1d6 minimum, **+1d6** par compétence et artefact applicables.
Selon le meilleur résultat obtenu aux dés :

<img class="size10 float-right" alt="Chibi Ninja" src="cc-imgs/Epic-Chibi-Ninja_by_dmr12890_cc-by-nc-sa.jpg">

* ⚅ / ⚄ : c'est réussi !
* ⚃ : c'est réussi **mais**...
* ⚂ : c'est raté **mais**...
* ⚁ / ⚀ : c'est raté

De plus :
* si deux ⚅ sont obtenus : c'est une **réussite épique** ! <!--, **le joueur décrit la scène** -->
* si deux ⚀ sont obtenus : c'est un **échec critique**
* sur un ⚂ ou ⚃, le MJ peut également proposer un **dilemme** :
  le joueur se voit proposer un choix cornélien entre deux options exclusives.
  Son personnage peut par exemple obtenir quelque chose au prix d'un sacrifice,
  ou bien se rabattre sur une réussite partielle.
* actions **difficiles** : lorsque le personnage d'un joueur tente d'accomplir une véritable prouesse, une action à la limite de ses capacités, le MJ peut alors indiquer qu'au moins **deux dés de valeur** ⚃, ⚄ ou ⚅ sont nécessaires pour réussir l'action.
* actions **en opposition**, comme par exemple un affrontement : un jet est effectué par personnage : **celui obtenant le plus de** ⚅ l'emporte. En cas d'égalité, on considère les ⚄, puis les ⚃. Si l'égalité persiste, aucun personnage ne prend l'avantage.
* actions **conjointes** : un personnage assistant un autre à réaliser une action lui octroie **un dé bonus**, si cette aide est jugée pertinente par le MJ.

<br class="web-only">

::: page-break
:::

### Règles d'emploi des Vocables
Employer un Vocable nécessite **1 point de Mana** canalisé, et un jet de dé.
Un personnage maîtrisant un Vocable, peut tenter n'importe quelle Versets propre à cette famille de magie.
Il est aussi possible de devenir expert d'un **Verset** en particulier, et de gagner ainsi **+1 dé** au lancer lorsqu'on l'emploie.

Certains artefacts rares peuvent également conférer **+1 dé** au lancer pour un Vocable spécifique.

<br>
<img class="size16 float-left" alt="Zuko" src="cc-imgs/zuko_fanart_by_codethecod_cc-by_greyscale.jpg">

<img class="size16 float-right" alt="Character perfoming magic" src="cc-imgs/the_new_avatar_allegedly_by_bananascholar_cc-by_greyscale.png">

<img class="size25" alt="Kyoshi Earthbender" src="cc-imgs/kyoshi_earthbender_lineart_by_aedo_sama_cc-by-nc-sa.jpg">

## Canaliser son Oni
Un komusō peur canaliser son Oni pendant un bref moment,
en réveillant la rage en lui
et ainsi offrir une pulsion d'énergie et de focus à son porteur.

Sur sa feuille de personnage, un joueur peut cocher une case libre de sa **jauge de Oni**.
Le nombre de cases cochées de cette jauge défini son **niveau de Oni**.

En faisant ainsi, pendant quelques minutes son personnage est plongé dans une rage concentrée.
Durant cette période, le joueur dispose d'autant de jetons de « rage Oni » que son niveau de Oni.
Le joueur peut dépenser ses jetons avant ou après un jet de dé demandé par le MJ,
pour obtenir immédiatement une **réussite critique**.

Lorsqu'il dépense un jeton « rage Oni »,
le joueur doit lancer un dé :
si le résultat est strictement inférieur à son niveau de Oni,
il entre en rage berserk.

::: page-break
:::

### Devenir berserk
Un komusō entrant en rage berserk passe sous le contrôle du MJ.

Un joueur peut choisir de **consommer 1 Ori** pour éviter cette transformation.

Le comportement du berserk est défini en consultant le résultat du jet de dé ayant transforé le komusō en berserk dans la table suivante :

::: borderless right-align-col-1 with-headings

Dé | Attitude
-|-
⚀⚁ | Le berserk s'attaque au PJ le plus proche.
⚂ | Le berserk s'attaque au PNJ le plus proche.
⚃ | Le berserk s'enfuit.
⚄⚅ | Le berserk s'attaque à un adversaire. S'il n'y en pas, relancé le dé.

:::

<br>
<img class="size20" alt="Shen Blood Moon" src="cc-imgs/league_of_legends_shen_blood_moon_by_spellshuei_cc-by.jpg">

::: page-break
:::

### Devenir un démon
Lorsqu'un personnage atteint le rang 5 d'Oni, des traits démoniaques commencent à apparaître sur son corps.
Lorsqu'il atteint le rang 6, encore plus de traits apparaissent.
Lancez un dé au rang 5 puis deux dés au rang 6 : ⚀: des oreilles pointues ; ⚁: des griffes ; ⚂: une machoire carnassière ; ⚃: la peau rouge; ⚄: des écailles; ⚅: des cornes.

Lorsqu'un personnage ayant un rang Oni 6 coche la dernière case de sa jauge,
il joue sa dernière scène puis devient un démon, joué comme un PNJ par le MJ.

<br>
<img class="size20" alt="Kappa" src="cc-imgs/Kappa_Koopa_by_weremagnus_cc-by.jpg">

::: page-break
:::


## Santé
_Section en cours de rédaction..._

<br>
<img class="full-width" alt="Old japanese village" src="cc-imgs/openclipart-old-japanese-village.svg">

::: page-break
:::


## Boucle de jeu
Dans Ori Mushi, le jeu alterne entre trois phases :

<img alt="Game loop" src="layout/GameLoop.jpg" class="size25">

### Jeu libre
Durant cette phase de jeu, chaque joueur incarne son komusō,
et est totalement libre de ses actions et paroles.
C'est le mode de jeu « classique » de la plupart des jeux de rôle.

L'un des vœux des komusō étant l'**itinérance**, ils voyagent sans cesse de lieu en lieu.
**À chaque fois que les komusō migrent d'un lieu** pour se rendre dans un autre,
passez ensuite successivement aux phases de jeu suivante :
1. [Répartition des Oris & progression](#oris-progression)
1. [Mystika](#mystika), où les joueurs rêvélent et détaillent **les secrets des terres connues**
1. [Autour du feu](#autour-du-feu), un moment de _roleplay_ entre komusō pour les joueurs

::: page-break
:::

## Oris & progression
Les Oris représentent la sagesse, l'élan de bonté, la force intérieure que n'importe qui peut développer.

La progression en Oris d'un komusō représente son gain d'expérience
acquise en réalisant des actions en alignement avec son code moral,
au fur et à mesures de ses aventures.

::: borderless right-align-col-1 with-headings

Situation | Progression par aventure
-|-
Échec critique ⚀⚀ | +1 Ori
Suivre activement les Vœux des komusō | +1 Ori
Suivre sa Progression de Voie | +1 Ori
Compléter la carte | +1 Ori

En dehors de l'échec critique, tous les gains d'Oris se font en fin de session de jeu,
lorsque les komusō reprennent leur voyage.

:::

::: page-break
:::

## Mystika
Durant cette phase narrative, les joueurs vont définir collectivement les détails qui entourent certains **secrets** de l'univers d'Ori Mushi.

Cette phase a lieu lorsque les komusō profitent des moments de repo de leur voyage
pour déchiffrer des **bas-reliefs antiques** qu'ils ont recopié durant leurs aventures,
ou pour lire des **livres interdits** qu'ils ont récolté.

L'examen de ces reliques est le rôle de l'**Artiste-Conteur** du groupe.
S'il n'y en aucun parmi les joueurs, alors le suivi des secrets découverts
est géré **globalement par le groupe** : découpez simplement la zone _Secrets_
d'une feuille d'Artiste-Conteur, et confiez-la aux joueurs.
S'il y a deux Artiste-Conteurs parmi les joueurs, alors laissez-les se mettre d'accord
pour que l'un se charge des bas-reliefs antiques et l'autre des livres interdits.

### Révélation d'un secret
Une fois par voyage entre deux aventures, un Artiste-Conteur peut profiter des temps de repo
pour déchiffrer un **bas-relief antiques** qu'il a recopié, ou un **livre interdit**.

Au terme de cet examen littéraire, il **découvre un secret** sur terres connues.
Pour déterminer lequel, le joueur lance un dé,
puis le MJ se reporte à la ligne correspondant au résultat dans la table ci-dessous.

Chaque secret déjà découvert par les komusō, et donc déjà coché dans la table,
est ignoré, et le secret en-dessous pris en compte à la place.
Et ainsi de suite **jusqu'à obtenir un secret non encore rêvélé**.
Le MJ le coche alors, et inscrit sur un morceau de papier la nature du secret,
qu'il transmet ensuite à l'Artiste-Conteur.

Le MJ est libre de cocher au préalable dans la table les secrets qu'il ne souhaite pas introduire dans la partie, afin qu'ils ne soient jamais rêvélés ainsi.

::: borderless text-small with-headings
☑ | Secret | Narration partagée
-|-
▢ | Le chant plaintif des Colosses est constitué de Versets du Poète Endeuillé, dont les effets sont magiques | **Question-Réponses** : Bilgamesh emploie le Vocable des Plantes, quel est exactement l'impact de ses Versets ?
▢ | Le peuple éteint n'a pas totalement disparu. Ses derniers membres se sont réfugiés dans une **vallée secrète**. | **Question-Réponses** : la relique que vous avez déchiffré indique comment y accéder, quel est ce moyen ?
▢ | Chaque Colosse est alimenté par une **sphère de Vitruve**, un dispotif mécano-magique alimenté par un **œuf de dragon**. Il est possible de leur donner des instructions en connaissant leur **nom secret**. | 
▢ | Dès l'œuf, les dragons ont un **nom secret**. Tant que celui-ci n'est pas oublié, ils sont immortels. | **Question-Réponses** : lors de la guerre de l'Oubli, comment fut oublié le nom de Watatsumi, dragon des mers ?
▢ | ❔ Les Onis sont en réalité affectés par une 7e famille de mushis parasites | 
▢ | ❔ Les dragons forment une 7e famille de mushis, et ils ne sont pas tous morts | 
▢ | xxx | 
▢ | xxx | 
▢ | xxx | 
:::

<!--
Ces secrets doivent "accompagner" la campagne principale.
Idéalement, alterner l'objet de ces secret: les Temps Antiques / la Guerre de l'Oubli / etc.
? Est-ce que d6 est vraiment UTILE ? Est-ce que rêvéler les secrets un à un ne serait pas plus simple pour écrire la campagne ?
-->

### Narration partagée
Cette colonne de la table des secrets indique **comment** se déroulera cette phase.
Il existe plusieurs formats, détaillés dans les sections suivantes :
* Question-Réponses
* Haïkus
* Artefact
* Journal de bord

Une bande son calme, poétique, envoutante est idéale pour cette phase.
Suggestions : [Mushishi](https://www.youtube.com/watch?v=brsJ19kclwc),
[Ori and the Blind Forest](https://www.youtube.com/watch?v=OvpnMT-iqCM).

L'Artiste-Conteur prend en note sur sa feuille de Voie du secret rêvélé.
Il aussi encouragé à prendre note, au dos de sa feuille de Voie,
des détails inventés collectivement durant cette phase.
Il pourra s'en inspirer pour de futures représentations de spectacles !

::: callout
Gardez en têtes ces grands principes durant la phase Mystika :
<!-- Ces principes valent aussi pour la phase de création de liens entre PJs -->
* durant ces phases de narration partagée, **vous êtes libres de créer n'importe quel élément de l'univers** : lieux, personnages, événements...
* employez la technique du **« oui et »** : ne rentrez jamais en contradiction avec les éléments apportés par les autres joueurs, mais rebondissez dessus et étoffez-les.
* tout n'a pas à être **cohérent** : les reliques découvertes par les komusō relatent des histoires, pas forcément la Vérite. Elles peuvent même parfois se contredire.
* cette phase doit rester relativement **courte**, idéalement environ une demi-heure : c'est au MJ de l'animer et de s'assurer qu'elle ne traîne pas en longueur
:::

### Format : question-réponses
À chacune de ces phases, un joueur sera l'Arbitre.
L'Artiste-Conteur est le premier à endosser ce rôle,
puis il sera assumé par tous les joueurs à tour de rôle au fil des phases suivantes de Questions-Réponses.
L'Artiste-Conteur est responsable de consigner qui a déjà été Arbitre,
et à qui revient ce rôle à chaque fois.

Les phases de Questions-Réponses se déroulent ainsi :
* le MJ énonce la question posée
* à tour de rôle, chaque joueur propose une réponse, sauf l'Arbitre
* enfin, l'Arbitre choisit la réponse qu'il préfère, ou un mélange de réponses

### Format : haïkus
Dans ce format, vous allez décrire une succession de **scènes** et d'ambiances,
formant un poème ou une balade, qui se transmet souvent accompagné de musique.
Le lien entre ces scènes ne sera pas explicité, et c'est à chacun de se forger une idée de ce qui les relier à travers le temps et l'espace.
Chaque scène est un haïku, une strophe du poème.

Le MJ peut choisir de participer ou non à cette phase.

**Déroulé** : à tour de rôle, chaque joueur énonce une phrase décrivant une **scène** ou une ambiance, pour former une succession de haïkus.
* n'importe quel joueur inspiré énonce la première phrase du premier haïku. Il est alors chargé d'inscrire toute la strophe sur la Feuille des Haïkus.
* en tournant dans les sens des aiguilles d'une montre, chaque joueur annonce une phrase à son tour.
* après un temps de réflexion, un joueur peut passer son tour.
* si possibe, la troisième phrase doit clôturer chaque haïku, puis la quatrième débuter un nouveau haïku, et ainsi de suite.
* ne respectez pas strictement les règles de composition des haïku : une strophe peut contenir 4 ou 5 phrases, le nombre de syllabes importe peu, une césure (_kireji_) à la fin est bienvenue mais pas nécessaire, etc.
* **le poème est fini** lorsque tous les joueurs sont satisfaits du poème, et que plus personne n'est inspiré pour débuter de nouveau haïku.

<!-- TODO : ajout exemples -->

### Format : artefact
Le MJ participe à cette phase comme les autres joueurs.

Le joueur qui a placé son dé sur cette table choisit un artefact
en possession d'un komusō du groupe, ou mentionné précédemment durant une partie.
Il désigne ensuite un joueur en lui passant son dé.

**Déroulé** :
* chaque joueur doit décrire une brève scène ou l'artefact était impliqué.
* le premier joueur doit décrire l'origine de l'objet, comment il a été conçu.
* la description doit s'attacher à décrire une scène préciser, sans nécessaire donner d'explications.
* les autres joueurs peuvent ensuite faire des commentaires, et poser des questions sur des détails de la scène.
* enfin, le joueur qui a décrit la scène transmet le dé un autre joueur, pour qu'il narre une autre scène impliquant l'artefact, située chronologiquement plus tard dans la vie de l'objet.
* une fois que tous les joueurs ont décrit au moins une scène, n'importe quel joueur qui reçoit le dé peut décider d'arrêt cette phase de narration.

::: page-break
:::

## Autour du feu
<img class="size8" alt="Feu de camp" src="cc-imgs/campfire_lit-cc0.svg">

Durant cette phase, les joueurs incarnent leurs komusō, au terme d'une journée de voyage,
alors qu'ils se retrouvent traditionnellement autour d'un feu de camp.
Si une phase Mystika vient d'avoir lieu,
alors cette scène commence alors que leurs personnages viennent de découvir
**un secret des terres connues**.

Il s'agit d'une séquence d'un quart d'heure axée sur le _roleplay_, où les joueurs sont encouragés à :
* partager avec les autres komusō ce que leur personnage a **ressenti** durant leur dernière étape
* revenir sur ce que certains de **leurs camarades ont fait**
* discuter de **leur mission** : est-ce qu'il l'accomplissent correctement ? Est-ce qu'ils l'envisagent tous de la même manière ?
* évoquer les **rêves et ambitions** de chacun
* émettre des hypothèses sur les **grands mystères** des terres connues : Colosses, mushis, légendes...

Durant cette phase, le MJ peut participer durant les "blancs" de la discussion pour décrire l'environnement autour des komusō, la lumière, les bruits, le vent...
Il est aussi encouragé à diffuser une musique d'ambiance adaptée :
* [Campfire Ambience with music - 1 Hour](https://www.youtube.com/watch?v=8tWmmhhJEjw)
* [Campfire Stories | TTRPG Ambience Music | 1 Hour](https://www.youtube.com/watch?v=bxaPsiNFY8E)
* [Campfire at Night - TTRPG relaxed BG Music - 1 Hour](https://www.youtube.com/watch?v=nSYpUGP7RRc)

::: page-break
:::

### La carte des terres connues
Au fur et à mesure de leur pérégrinations, les komusō tracent une **carte des terres connues**.
Au terme de la phase Mystika, les joueurs complètent cette carte :
* ils peuvent y ajouter des **lieux**, issus de leur dernier voyage où du Mystika
* ils peuvent y dessiner ou mentionner des **personnages** ou des **points d'intérêt** notables

Cette carte mentionne les lieux notables traversés par le groupe,
et éventuellement des éléments sur le relief, les cours d'eau,
l'environnement en général et les bâtiments découverts en chemin.

En tant que MJ, lors de votre première partie, vous pouvez au choix :
* donner une **feuille A4 vierge** à vos joueurs
* fournir un **fond de carte** de votre univers favori, ou dessinée par vos soins

La carte doit comporter une **rose des vents** indiquant les directions cardinales : Nord, Sud, Est, Ouest.
Elle doit aussi comporter **les signatures des komusō**, qui attestent de sa validité.

À chaque fin de partie, un joueur du groupe se dévoue pour compléter la carte.
Le PJ de ce joueur gagne **+1 Ori** s'il inclut au moins un tout petit **dessin** d'une plante, d'une créature ou d'un personnage qu'ils ont rencontré.

<br><br>
<img class="size10" alt="Un parchemin de carte" src="cc-imgs/pirate_map_1_by_thestockwarehouse_cc-by_greyscale.png">

::: page-break
:::


## PNJs
### Hisaishi Inoue
Capitaine en chef des bateliers
### Oma la Cueilleuse de Mots
Une Poètesse-Sorcière, élue par les forestiers pour diriger le conseil des sages de Nippur.
Vit au Moulin Des Cigognes
### Bilgamesh
Colosse encore actif, géant humanoïde arpentant les Basses Plaines.
### Gilga
La légende raconte qu'il commandait aux Colosses et qu'il aurait vaincu les Onis.


## Griddish
<https://www.reddit.com/r/neography/comments/a9yd0d/i_made_a_griddy_cipher_where_letters_smush/>

::: borderless
A | B | C | D | E | F | G | H | I | J | K | L | M
-|-
~~A~~ | ~~B~~ | ~~C~~ | ~~D~~ | ~~E~~ | ~~F~~ | ~~G~~ | ~~H~~ | ~~I~~ | ~~J~~ | ~~K~~ | ~~L~~ | ~~M~~
N | O | P | Q | R | S | T | U | V | W | X | Y | Z
~~N~~ | ~~O~~ | ~~P~~ | ~~Q~~ | ~~R~~ | ~~S~~ | ~~T~~ | ~~U~~ | ~~V~~ | ~~W~~ | ~~X~~ | ~~Y~~ | ~~Z~~
:::
<br>

lepoeteendeuille : ~~lepoeteendeuille~~

LEPOETEENDEUILLE : ~~LEPOETEENDEUILLE~~

Dans le jeu, cet alphabet est celui des Temps Antiques.

L'idée est d'employer ce script sur les feuilles de personnage pour y dissimuler des secrets que les joueurs décrouvriront durant la partie.

::: page-break
:::

## Version Express
Cette version du jeu est destinée à des parties très courtes, d'une heure environ.
Inspiré du [scénario de Kalwrynn pour initier au jeu de rôle intitulé "Mener en 30min"](http://www.lulu.com/fr/fr/shop/kalwrynn/mener-en-30mn/ebook/product-24254652.html),
ce mode de jeu se veut volontairement très simple et épuré,
pour offrir aux joueurs en une heure un aperçu du jeu.

### Création de personnage en 5min
1. Choisissez votre apparence et **un artefact** (arme, objet magique...) parmi les illustrations,
ou inventez-les ! Les artefacts sont des objets magiques ou que leur possesseur maîtrise avec virtuosité.

2. Inscrivez sur votre feuille de personnage son **nom**, son **activité** et cochez **3 compétences**.

L'**inventaire** de départ des personnages est complètement libre :
il s'agit de tous les objets qu'ils souhaiteraient transporter sur eux.
Ces objets n'étant pas _spéciaux_, ils n'octroient pas de dé supplémentaires lors des jets.## Éléments clefs à établir en début de partie
- « L'histoire se déroule dans un japon médiéval imaginaire. Il existe de la magie et des monstres. »
- Le meneur de jeu demandera des jets aux joueurs pour les actions risquées de leurs personnages.
- Les joueurs se connaissent déjà et voyagent ensemble, et c'est d'ailleurs leur objectif commun : explorer les terres connues... et inconnues !
Ils ont déjà traversé de nombreuses contrées et aidé bien des gens.

<br>

## Scène 0 - Course poursuite !
Bien que cela rallonge légèrement la durée de la partie, je trouve très judicieuse l'idée de Kalwrynn de commencer _in media res_.

Je vous suggère donc de commencer la partie en décrivant rapidement un joli décor de chemin de terre sinuant
parmi les champs et les herbes folles, par une paisible après-midi printanière, au pied d'une montagne...
Où les personnages des joueurs descendent le chemin en pente à perdre haleine,
poursuivis par un troll-kappa dont ils ont piétinés le jardin par mégarde !
Cette créature, sorte de taupe humanoïde avec un bec, est fâchée et pas du tout disposée à discuter !

Décrivez aux joueurs les environs pour leurs donner quelques idées d’échappatoire :
l'orée de la forêt de bambous, la descente un peu raide vers un lac, les hautes herbes balayées par le vent...

Au terme de cette scène, les joueurs doivent rejoindre le village, par le chemin ou le lac,
quitte à faire une ellipse ou à indiquer qu'il s'agit de l'étape suivante de leur voyage,
où on leur a vanté une recette locale de poisson frit...

::: page-break
:::

<br>
<img class="size10 float-right" alt="Bambou" src="cc-imgs/bamboo-cc0.svg">


## Ressources

<br>

### Illustrations
S'inspirant de [Sventovia](http://legrumph.org/Terrier/?Jeux-de-role/Sventovia) du Grümph,
nous vous encourageons à imprimer des images au préalable, pour faciliter l'immersion des joueurs.

Vous trouverez dans ce PDF de multiples illustrations pour les komusō, les PNJs,
ainsi que différents lieux, créatures & artefacts
[OriMushi-illustrations.pdf](OriMushi-illustrations.pdf).

Voici également quelques illustrateurs inspirants :
* [liquidcoco](https://www.artstation.com/liquidcoco)

### Ambiance musicale
Quelques suggestions de bande sons originales :
[Okami](https://www.youtube.com/watch?v=JAfXYXwykFI),
[Princess Mononoke](https://www.youtube.com/watch?v=LKI9aczEL3g),
[Furyo / Merry Christmas Mr. Lawrence](https://www.youtube.com/playlist?list=PLBTmKkw_sSw0garpOiQ0W6deqEXd_zfaj),
[Journey](https://www.youtube.com/watch?v=M3hFN8UrBPw),
[Creatures of Ava](https://www.youtube.com/watch?v=FMFb5eY3Wc4)
--> à insérer comme suggestion pour chaque phase

[Beautiful Piano -Poems of the Moon - Japanese Fantasy Inspired BGM](https://www.youtube.com/watch?v=Zu_pBbCwovA)

[Blue Turtle YouTube playlists](https://www.youtube.com/@BlueTurtle/videos)

Bande son YouTube : [Ori Mushi](https://www.youtube.com/playlist?list=PLLgE-ga3W_kbktCFQcCk_AIr3UqNLBRGI)

### Cartes de lieux
Si vous aimez avoir un support visuel pour vos parties, voici quelques belles cartes qui peuvent parfaitement servir de support à une partie d'Ori Mushi :

* [Sanctuaire de la forêt - Czepeku](https://www.czepeku.com/fr/store/product/forest-shrine-festival)
* [Monastère des cerisiers en fleurs - Czepeku](https://www.reddit.com/r/dndmaps/comments/mo9udv/cherry_blossom_monastery_21x49/) - [scene illustration @ Patreon](https://www.patreon.com/posts/zen-monastery-109669515)
* [Warforged Titan Scrapyard - Czepeku](https://www.czepeku.com/fr/store/product/warforged-titan-scrapyard) - [scene illustration](https://www.czepeku.com/fr/store/product/warforged-titan-scrapyard-scene)
* [Cache du Oni - Ferme de riz - Czepeku](https://www.reddit.com/r/battlemaps/comments/q3dkqc/oni_hideout_spring_23x36/)
* [Bains japonais - Czepeku](https://www.czepeku.com/store/product/steamy-japanese-bathhouse) - [scene illustration @ Patreon](https://www.patreon.com/posts/90005505)
* [Wizard Prison - Czepeku](https://www.czepeku.com/fantasy/maps/wizard-prison-part-1) - [scene illustration @ Patreon](https://www.patreon.com/posts/90005505)
* [Celestial Gate - Czepeku](https://www.czepeku.com/fantasy/maps/celestial-gate/spring) - [video scene](https://www.patreon.com/posts/celestial-gate-79276610) - Spring version
* [Mountaintop Observatory - Czepeku](https://www.czepeku.com/fantasy/maps/mountaintop-observatory/hot-spring-monkey)

::: page-break
:::

## Illustrations sélectionnées - non encore placées
<img class="size6" alt="Yin Yang symbol" src="cc-imgs/freesvg-decorative-ying-yang-sign.svg">

<br>
<img class="size20" alt="Samurai" src="cc-imgs/quick_samurai_sketch_by_hidanbasher_cc-by_greyscale.jpg">

<br>
<img class="size10" alt="A Noh demon" src="cc-imgs/Noh_Demon_by_weremagnus_cc-by_greyscale.jpg">

<br>
<img class="size10" alt="Moon and clouds" src="cc-imgs/moon-and-clouds.jpg">

<br>
<img class="size10" alt="" src="unused-cc-imgs/HUNTING-Familiar-Wolf_by_kindya-island_cc-by-nc_greyscale.jpg">

<br>
<img class="size20" alt="" src="unused-cc-imgs/Misplaced_by_willinvadesearth_cc-by_BW.jpg">

<br>
<img alt="" src="unused-cc-imgs/nature_waterfall_2_by_mholtsmeier_cc-by.jpg">

<br>
<img class="size20" alt="" src="unused-cc-imgs/haptera-de-taille-considerable-fig-751-cc0.jpg">

<br>
<img class="size20" alt="" src="unused-cc-imgs/pistils-de-glyceria-cc0.jpg">

<br>
<img class="size10" alt="" src="cc-imgs/Gold-Demon-by-marikbentusi-cc-by-nc-cropped-greyscale.png">

<br>
<img class="size20" alt="" src="cc-imgs/Black-n-Gold-Stuff-by-marikbentusi-cc-by-nc-cropped-greyscale.png">

_**Images searches**_: Creative Commons via Google, avec filtres "il y a moins d'un mois" + Licences Creative Commons :
* [DeviantArt: artwork|"concept art"|illustration|character](https://www.google.com/search?tbm=isch&tbs=qdr:m,sur:cl&q=site%3Adeviantart.com+-Derivatives+-NoDerivatives+-%22User+profile%22+-Explore+-%22AI+tools%22+%28artwork%7C%22concept+art%22%7Cillustration%7Ccharacter%29)
* [DeviantArt: manga](https://www.google.com/search?tbm=isch&tbs=qdr:m,sur:cl&q=site%3Adeviantart.com+-Derivatives+-NoDerivatives+-%22User+profile%22+-Explore+-%22AI+tools%22+manga)

::: page-break
:::

## Glossaire

JdR
: jeu de rôle

MJ
: Meneur ou Meneuse de Jeu

PJ
: Personnage d'une Joueuse ou d'un Joueur

One-shot
: courte partie de JdR isolée, sans qu'il ne soit prévu de suite

Campagne
: ensemble de parties de JdR se suivant pour former une continuité, où l'on retrouve les même personnages dans le même univers

Hopepunk
: un sous-genre des littératures de l'imaginaire, conçu à l'opposé des dystopies amorales ou violentes, où la bonté est un acte politique et de rébellion, et les personnages ne se résignent pas face à un univers hostile. [Page Wikipedia](https://fr.wikipedia.org/wiki/Hopepunk). Voici quelques œuvres que j'estime appartenir à ce genre et que je recommande : les BDs _Lightfall_, _Mouse Guard_, _Nimona_, _SAGA_; les films Nausicaä & Princesse Mononoké; la série _Firefly_; les jeux vidéos _Brothers - A Tale of Two Sons_ & _Journey_.

::: page-break
:::

## Ambitions de _game design_
::: callout
* un JdR où les combats sont rares, et **jamais nécessaires**
* un format de courte campagne (~ 10 parties) où les personnages et l'univers **évolueront significativement**, avec plusieurs mystères rêvélés
* intégrer aux feuilles des personnages des **mécaniques incitant à les faire évoluer narrativement**, avec des éléments **uniques pour chaque archétype**
* créer un jeu **_light_ en terme de contenu textuel** décrivant l'univers, et intégrer à la place des phases de **_storytelling_ narrativiste**. N'inclure **aucun élément de _lore_** "inutile" (~ _fusil de Tchekhov_)
:::

## Toutes les idées qui n'ont pas pu aboutir dans cette version

### Atlas des joueurs
Un atlas de 4-6 pages est remis aux joueurs en début de campagne.
Cet atlas détaille brièvement l'histoire et la géographie des terres connues.
Des annotations manuscrites mentionnent quelques mystères,
et des petits encarts de réponse permettent aux joueurs d'y consigner leurs découvertes.

### Site web
* partage de haïkus, avec mise en page jolie (proc-gen) de ces textes
* partage de personnages
* partage de lieux sur carte partagée (mentionner `#hashtag` dédié pour les partager sur réseaux sociaux)
    + tool: <https://github.com/Azgaar/Fantasy-Map-Generator>
    -> fine-tune & disable useless features: <https://github.com/Azgaar/Fantasy-Map-Generator/wiki/Quick-Start-Tutorial#performance-tips>
    alt tool: <https://github.com/davmillar/DavesMapper>
    + 1 carte commune publique
    + lien avec le jeu ?
        -> avoir acheté le jeu permet d'avoir un compte sur la carte partagée
    + collaboration model: all users with an account can edit the map
    -> add a server-storage based provider, with some auth: <https://github.com/Azgaar/Fantasy-Map-Generator/blob/master/modules/io/cloud.js>
    => needs a system to avoid concurrent edits
    => open GitHub issue to suggest feature?

::: page-break
:::

## Licence, sources & remerciements

<a class="float-left" rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img alt="Creative Commons License Attribution-NonCommercial-ShareAlike 4.0 Unported" src="layout/cc-by-nc-sa.png">
</a>

_Ori Mushi_ a été conçu par [Lucas Cimon](https://chezsoi.org/lucas/blog/), il est placé sous license <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0</a>.

Ce jeu est diffusé à prix libre.
Si vous souhaitez me soutenir, vous pouvez me faire un don sur [lucas-c.itch.io](https://lucas-c.itch.io).
Les fichiers sources ayant permis de générer ce PDF sont disponibles [sur GitHub](https://github.com/Lucas-C/jdr/tree/master/OriMushi).
Cette version est la v0.4.

Je serais ravi d'avoir vos retours si vous jouez à ce jeu !
Racontez-moi comment s'est passée votre partie via un commentaire [lucas-c.itch.io](https://lucas-c.itch.io) ou sur [mon blog](https://chezsoi.org/lucas/blog/tag/ori-mushi.html).

Merci enfin aux développeurs des [logiciels libres](https://fr.wikipedia.org/wiki/Free/Libre_Open_Source_Software) employés pour réaliser ce jeu : [le navigateur Firefox](https://www.mozilla.org/fr/firefox/), [le logiciel de dessin Gimp](https://www.gimp.org/), [l'éditeur de texte Notepad++](https://notepad-plus-plus.org/), [le lecteur de PDF Sumatra PDF](https://www.sumatrapdfreader.org), [le language de programmation Python](https://www.python.org/), les bibliothèques de code [mistletoe](https://pypi.org/project/mistletoe/) & [weasyprint](https://weasyprint.org/), le logiciel d'agrandissement d'image [nunif/waifu2x](https://www.waifu2x.net/).

<img class="size8 float-right" alt="Ombrelle en papier" src="cc-imgs/piratebay-asian_paper_umbrella.jpg">
<br>

::: thanks
Polices : [Ink Free](https://www.dafontfree.co/ink-free-font/)
& [Odachi](https://www.behance.net/gallery/59783897/Odachi-Free-Brush-Font)
& [Xangda Shiny](https://www.fontspace.com/starinkbrush/xangda-shiny).

Illustrations employées :

<!-- TODO: add icons & plants-by-LeviGilbert-cc-by -->

- [Epic Chibi Ninja par dmr12890](https://www.deviantart.com/dmr12890/art/Epic-Chibi-Ninja-129862000) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [Kyoshi Earthbender Lineart par Aedo Sama](https://www.deviantart.com/aedo-sama/art/Kyoshi-Earthbender-Lineart-215736017) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [magic circle 2 par NNao](https://www.deviantart.com/nnao/art/magic-circle-2-216221240) - [CC BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/)
- [Kappa koopa](https://www.deviantart.com/weremagnus/art/Kappa-koopa-53098269) & [Noh Demon par weremagnus](https://www.deviantart.com/weremagnus/art/Noh-Demon-39665536) - [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/)
- [HUNTING - Familiar Wolf par Kindya-Island](https://www.deviantart.com/kindya-island/art/HUNTING-Familiar-Wolf-982938883) - [CC BY-NC 3.0](https://creativecommons.org/licenses/by-nc/3.0/)
- [Nature waterfall 2 par MHoltsmeier](https://www.deviantart.com/mholtsmeier/art/Nature-waterfall-2-963933789) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Zuko fanart par CodeTheCod](https://www.deviantart.com/codethecod/art/Zuko-fanart-902243721) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [League of Legends - Shen / Blood Moon par Spellshuei](https://www.deviantart.com/spellshuei/art/League-of-Legends-Shen-Blood-Moon-296075743) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Demon blood par aMiGoS21](https://www.deviantart.com/amigos21/art/Demon-blood-1179573979) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Quick samurai sketch par hidanbasher](https://www.deviantart.com/hidanbasher/art/Quick-samurai-sketch-566443259) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [Pirate Map 1 par TheStockWarehouse](https://www.deviantart.com/thestockwarehouse/art/Pirate-Map-1-845443862) - [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)
- [DnD Stone Elemental par Lady of Hats](https://commons.wikimedia.org/wiki/File:DnD_Stone_Elemental.png) - [CC0](https://creativecommons.org/publicdomain/zero/1.0/deed.en)
- [Japanese Style Link Art Border Frame](https://www.vecteezy.com/png/32163325-japanese-style-link-art-border-frame-ai-generative) @vecteezy.com
- [parapluie-écran-chinois](https://pixabay.com/fr/photos/parapluie-%C3%A9cran-chinois-chine-japon-898076/) @pixabay.com
- [Decorative Ying Yang sign](https://freesvg.org/vector-clip-art-of-decorative-ying-yang-sign) @freesvg.org - domaine public
- [Image from _"A handbook of cryptogamic botany"_ (1889)](https://www.flickr.com/photos/internetarchivebookimages/20102877173/) - domaine public
:::
:::::

<!--
Partie du 2/01/2025 avec 3 jeunes, à la Possonière, avec Donatien :
* Sunraku (Marwann) : Mushishi - Jutsu
* Aether (Leyline) : Apothicaire - Jutsu
* Sasukeden (Aïden) : Ronin - Jutsu

Partie du 1/03/2025 avec Aurelien, Elliot, Laure, Matt & Olivier

Partie du 5/04/2025 Au WEJ avec Olivier, Naïg, Flo, Timothé (?) & ? (ami Naïg IUT)
* l'énigme avec le Mushi / labyrinthe sous le temple est trop frustrante
* intégrer les singes & la gravure à l'intrigue ?
* changer l'échelle de difficulté : 1-2 = râté; 3 = non mais...; 4 = oui mais...; 5-6 = réussi
* mieux vaut privilégier des prétirés pour les one-shot :
    là les joueurs étaient frustrés d'avoir des compétences qui leur soient inutiles
-->
