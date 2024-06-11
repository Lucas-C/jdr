# Paradis Perdu
# Modules de secours

<!--br><br><br>
<img class="large" alt="" src="">
<br><br-->

Ceci est une aide de jeu pour [Paradis Perdu](https://www.misterfrankenstein.com/wordpress/?p=5388), un excellent jeu de rôle « Nuit Blanche » d'Anthony "Yno" Combrexelles.
Il se compose d'un ensemble de modules optionnels, que vous pourrez adopter pour ajouter des rebondissements supplémentaires au scénario original. Ces modules m'ont également beaucoup aidé en tant qu'Admin pour préparer ma partie, et compléter quelques points non détaillés dans le jeu de base.

### Sommaire

- [Plan de la station Terra Nova](#plan-de-la-station-terra-nova)
- [Terminaux CommLinks](#terminaux-commlinks)
- [PNJs](#pnjs)
- [Intro - Connivences](#intro-connivences)
- [Acte 1 - L'œil pour le détail](#acte-1-l-il-pour-le-d-tail)
- [Acte 2 - Big brother is watching you](#acte-2-big-brother-is-watching-you)
- [Acte 2 - Trolley dilemna au laboratoire](#acte-2-trolley-dilemna-au-laboratoire)

TODO : à compléter + vérifier que liens fonctionnent + intégrer sections du README.md


## Plan de la station Terra Nova

<img class="large" alt="Space station" src="img/SpaceStation.jpg" style="min-height: 890px">


### Déplacements
TODO - à rédiger : en substance, l'idée est de réaliser des micro-ellipses lorsque les PJs progressent à travers des étages où il ne se passe rien. + rappel table des **Rencontres** avec des androïdes page 63

À chaque fois que les PJs veulent se rendre d'un point A à un point B dans la station, indiquez le ou les itinéraires qu'ils peuvent envisager, ils en choisissent un, puis je leur indique la ou les situations qu'ils rencontrent en chemin


## Terminaux CommLinks
Ce module propose de mettre à disposition des joueurs un **terminal web**, diégétique à l'histoire car consultable par les PJs sur les CommLinks de la station. Il nécessite que vos joueurs aient des smartphones avec connexion à internet durant la partie.

> Le but de ce terminal est de contribuer à l'immersion des joueurs dans l'histoire, mais aussi d'ajouter quelques indices optionnels sur les événements du scénario.

Tout PJ peut accéder à ce terminal si on lui montre la manipulation à effectuer sur un CommLink, mais au début du scénario seuls **Arora** et **Sullivan** connaissent l'existence de cette fonctionnalité.

Découpez ces deux cartes, et remettez-les aux joueurs correspondants après l'**Intro**, lorsqu'ils découvrent les CommLinks :

<table><tr>
    <td>
        <b>Arora</b><br>
        Lorsque vous employez un CommLink, vous savez accéder à son terminal :
        <a href="https://chezsoi.org/lucas/jdr/ParadisPerdu/acte-1/">
            <img alt="" src="qrcode-terminal-acte-1.png">
        </a>
        Mot de passe <code>auditer</code> : <code>trustno1</code>
    </td>
    <td>
        <b>Sullivan</b><br>
        Lorsque vous employez un CommLink, vous savez accéder à son terminal :
        <a href="https://chezsoi.org/lucas/jdr/ParadisPerdu/acte-1/">
            <img alt="" src="qrcode-terminal-acte-1.png">
        </a>
    </td>
</tr></table>

> Les QR-codes ci-dessus sont les mêmes.
> En version PDF, vous pouvez cliquez dessus pour accéder au terminal dans votre navigateur web.

Voici un résumé des informations fournies par ce terminal :

* la commande `map` fournit la liste des niveaux de la stations, et indique la répartition des androïdes `Arnie`, `Cory` & `Miranda`.
* la commande `medic` permet de s'inscrire pour rendez-vous auprès du Dr Aberdeen, et de voir la liste des consultations prévues.
* la commande `port` liste les vaisseaux à quai dans le port spatial au niveau 9.
* la commande `staff` liste les personnes référentes de la station.
* la commande `audit`, uniquement accessible par Arora après s'être logué⸱e comme `auditer` via la commande `login`, indique que tout est opérationnel sauf l'une des antennes de communication spatiale. De plus, un message fantômatique est adressé à _Sanj_ par son amour décédé...
* **Daryl** a également envoyé un email énigmatique à toute la station. Le déchiffrer (c'est du [ROT13](https://fr.wikipedia.org/wiki/ROT13)) permet de comprendre qu'il faut ensuite taper dans le terminal une commande non référencée par `help`, mais qui existe sur les systèmes [Linux](https://fr.wikipedia.org/wiki/Linux) : `exit`, `hostname`, `man`, `ps`, `pwd`, `shutdown`, `sudo`, `touch`, `ping` ou `whoami` peuvent fonctionner. Daryl donne alors rendez-vous au niveau 3 au PJ qui aura résolu son jeu de piste.

À la fin de l'**acte 1**, la prise de contrôle de l'étage des Communications par Cory 3 affecte le terminal.
Pour refléter cela, découpez la carte ci-dessous, et remettez-la aux joueurs au début de l'**acte 2**, dès qu'ils accèderont à un terminal CommLink.
Ils devront désormais employer cette nouvelle version du terminal :

<table class="terminal-card"><tr>
    <td>
        ⚠️ ⚠️ ⚠️
        <br>Les communications de la station
        <br>sont impactées.
        <br>Voici le nouveau contenu du terminal CommLink web :
        <a href="https://chezsoi.org/lucas/jdr/ParadisPerdu/acte-2/">
            <img alt="" src="qrcode-terminal-acte-2.png">
        </a>
    </td>
</tr></table>

Cette seconde version du terminal comporte plusieurs changements :

* le niveau d'**oxygène** de la station a drastiquement réduit est en baisse constante.
* la commande `map` n'indique plus la position à jour des androïdes.
* les commandes `medic` & `port` ne fonctionnent plus.
* la commande `audit` indique de très importants **dysfonctionnements des systèmes**, notamment des communications avec Cepheus, des communications spatiales et du réseau des androïdes.
* de nouveaux emails ont été diffusés à tout la station, révélant la panique et les tragédies suite à l'attaque des androïdes. Notamment **Ellen Frost** qui demande de l'aide alors que la dépressurisation du niveau 9 est en cours. Il y a également un message crypté de **La Sécurité** informant de son intervention imminente.


## PNJs
En complément des informations données dans le scénario, cette section propose quelques éléments supplémentaires pour jouer les PNJs, en détaillant notamment leurs objectifs durant les actes 2 et 3, leur attitude face aux PJs, la manière la plus probable dont ils décèderont, et un conseil sur comment interprêter théâtralement chaque personnage. Je me suis inspirés pour ce dernier point de l'article [_Comment interpréter les traits distinctifs des PNJ_ de James Introcaso, traduit sur ptgptb.fr](https://ptgptb.fr/interpreter-les-traits-distinctifs-des-pnj).

Concernant les _morts probables_ : ces indications sont là pour vous encourager à décimer progressivement les PNJs au fur et à mesure du scénario, et ainsi maintenir la tension dramatique. N'hésitez pas pour autant à improviser et les faire décéder autrement !

### Brett Bettany
<img alt="Brett Bettany" src="img/hazmat_by_fernand0fc_bgw_buste_cc-by.jpg" class="pnj">

* n'apprécie pas les dockers & manœuvres, qu'il trouve méprisant envers les ouvriers, et en particulier Ellen Frost qu'il déteste.

* connait Watters et sa promotion du culte de l'Ascension. Il s'en méfie comme de la peste.

* a connaissance d'**une arme de contrebande (fusil à pompe) planquée au niveau 4**, dans un recycleur.

* durant les actes 2 & 3, peut fournir des **combinaisons spatiales**

* **Objectifs** : initialement paniqué, Brett se reprendra après la tuerie initiale, et aidera 1D6+2 ouvriers à se barricader dans un petit hangar au niveau 10. Ensuite&nbsp;:
    1. protéger les ouvriers, et s'armer pour se défendre
    2. trouver un vaisseau fonctionnel pour se tirer cette station
    3. fuir en embarquant un maximum d'ouvriers avec lui

* **Attitude** : coopératif avec les PJs si cela le rapproche de ses objectifs. En cas de situation critique pour lui ou des ouvriers, il n'hésitera pas à jeter les PJs en pâture à des ennemis pour leur échapper.

* **Roleplay** : posture très droite, presque rigide; parle de manière lente et posée, en prennant de profondes inspirations avant chaque nouvelle phrase.

* **Mort probable** : en prennant d'assaut le vaisseau de « La Sécurité ».

### Isaac Cameron
<img alt="Isaac Cameron" src="img/ElliotJolivet_Tensei_Inktober2017.jpg" class="pnj">

* à l'acte 1, en plus des activités mentionnées par le scénario (pages 51 & 52), il sera en train d'enquiller les verres d'alcool fort au **bar le Kapow, au niveau 8**, au début de l'acte 2.

* armé d'un **revolver**, il récupère le **taser** d'un marshal décédé et comprend vite qu'il est plus efficace contre les androïdes.

* la moitié du paiement lui a été viré sur un compte extraplanétaire, l'autre lui a été remis « en liquide  », via des liasses de **crédits planqués dans une bible**

* **Objectifs** :
    1. Survivre et fuir la station
    2. En profiter pour récupérer ce qui a de la valeur

* **Attitude** : combatif, il n'hésite pas à affronter les androïdes, sans prendre de risques inutiles; s'il croise les PJs, il sera méfiant mais pas belliqueux, et pourra les accompagner un temps. Il grommele ses soupçons concernant Watters : _« Quel salopard... Tout est parti en vrille après le deal, comme par hasard... »_

* **Roleplay** : vouté; crispé, mais essaie de paraître détendu; se tripote les doigts constamment, ou les tapote sur la table.

* **Mort probable** : blessé mortellement par « La Sécurité », il agonise dans un recoin

### Candy Davies
<img alt="Candy Davies" src="img/CandyDavies.jpg" class="pnj" style="max-height: 14.5rem">

* si les PJs remontent la piste des vendeurs de Tedium, ils entendront vite parler d'elle.

* elle reconnaîtra facilement avoir vendu du Tedium, mais sera réticente à balancer son fournisseur.

* ce qui peut la convaincre de révéler ce qu'elle sait : une grosse somme d'argent; qu'on lui rapporte des propos l'accusant de Jones ou Cotton; qu'on l'intimide sérieusement - jet de **S'imposer (+ Argumentation)**... La menace d'alerter « les flics » ne l'effrayera pas.

* si elle le peut, elle balancera seulement Jones, car Coton est une cliente qui paye bien et ne l'a jamais trahie. Et elle l'aime bien.

* **Attitude** : nubile et allumeuse, quel que soit le genre de son interlocuteur•rice; elle est volubile et colportera volontiers infos et commérages sur toutes les personnes connues de la station.

* **Roleplay** : voix suave; mache un chewing-gum; se tripote les cheveux; _« mon bichon »_; _« mon•a poulet•te »_; _« petit•e coquin•e »_, _« petit•e coquin•e »_, etc.

* **Mort probable** : au début de l'acte 2, tuée par un androïde sous les yeux des PJs

### Darcy Cotton
<img alt="Darcy Cotton" src="img/headshots_by_fernand0fc_girl_bw_cc-by.png" class="pnj">

* durant l'acte 1, comme mentionné dans le scénario (page 58), elle essaiera d'éloigner les soupçons d'elle concernant le Tedium. Face à des gélules, elle identifiera la substance, mais évoquera un vol récent dans les bureaux de Revolve, signalé à la sécurité, et que le secret industriel lui empêche d'en dire plus. Lui faire avouer la vérité nécessitera beaucoup de ruse, ou un jet réussi de **S'imposer (+ Argumenter)**.

* durant l'acte 2, elle sera initiallement **bloquée dans sa cabine, au niveau 6**, des androïdes l'empêchant d'en sortir. Elle tentera alors de joindre des survivant via CommLink, et elle justifiera si besoin de son utilité en évoquant son expertise en IA & communications à Revolve.

* une fois qu'elle aura l'occasion d'examiner un androïde, elle sera la 1ère PNJ à **comprendre que Cory 3 est à l'origine de la rébellion**, et qu'il commande aux androïdes depuis la salle réseau du niveau 1 (_cf._ [Terminaux CommLinks](#terminaux-commlinks)), et que..

* elle a accès depuis n'importe quel CommLink à toutes les caméras de sécurité en activité de la station. _(Admin : pratique pour introduire des rebondissements)_

* elle connaît bien Deware, et saura identifier les intentions de « La Sécurité » à leur arrivée. Elle mettra en garde les PJs, inquiète pour elle-même.

* **Objectifs** :
    1. Survivre : retrouver et suivre Jones lui semble initiallement le meilleur choix
    2. Comprendre ce qui est arrivé aux androïdes
    3. Étouffer cette affaire, et détruire le labo de Revolve

* **Attitude** : aucun remord à s'en sortir seule, mais elle sait qu'elle aura d'abord besoin d'alliés. Elle joue les pimbêches candides pour mieux leurer son monde, alors qu'elle a des nerfs d'acier. Elle a une arme à feu mais évitera de le montrer.

* **Roleplay** : joue les appeurées et fait preuve d'auto-dérision; rit à ses propres touches d'humour, et recherche la complicité de ses interlocuteurs; se masse constamment les épaules; lance parfois des regards perçants trahissant sa dureté.

* **Mort probable** : éventrée par une larve cosmique, après avoir trahi les PJs.

### Daryl Hamon
* Daryl se doute que Cotton traffique quelque chose de **louche**, à titre personnel, avec les médicaments qui lui sont administrés. Il se méfie d'elle.

* les compétences de Daryl en _hacking_ lui ont permi de s'introduire dans le réseau CommLink, où il a laissé un petit **message caché**, dans l'espoir que quelqu'un de futé remonte à lui afin de faire sa connaissance, _cf._ [Terminaux CommLinks](#terminaux-commlinks).

* ses compétences en informatique lui ont également permi d'avoir accès à distance aux capteurs de la station, et Daryl a détecté des échanges de **communications à quelques km** seulement de Terra Nova (le vaisseau de « La Sécurité »). Il pense qu'il s'agit peut-être d'une balise spaciale « pirate » et est curieux d'en savoir plus.

* au début de l'acte 2, la moitié des chercheurs du laboratoire iront se réfugier dans leurs cabines du niveau 6. L'autre moitié aura été **massacrée par des androïdes**, et leurs corps entassés dans dans le local informatique de manière gore, éclaboussant de sang et de tripes toute la pièce. Daryl de son côté a réussi à ramper jusqu'à une cachette, avec uniquement ses prothèses de bras, et les androïdes ne l'ont pas trouvé.

* le chaos ambiant sera pour lui une opportunité de quitter le laboratoire avec ses prothèses expérimentales des quatre membres qui lui manquent, _cf._ [Trolley dilemna](#acte-2-trolley-dilemna-au-laboratoire). Malheureusement celles-ci se mettront progressivement à **dysfonctionner** : jambe qui boîte, doigts bloqués, bras restant collé contre son corps... Sullivan pourra peut-être palier aux problèmes initiaux, mais les membres artificiels Daryl cesseront inéluctablement de fonctionner au terme de l'acte 2.

* s'il voit les cadavres des chercheurs de Revolve qui prennaient soin de lui, Daryl sera profondément **traumatisé**. Il restera mutique plusieurs dizaines de minutes, chancelant, mais acceptera de suivre les PJs d'un air ébété. _(Admin : trigger warning, ne jouez cette scène que si vous joueurs sont OK avec cela. Vous pouvez aussi choisir que Daryl soit traumatisé par une autre scène sanglante, plus tard)_

* **Objectifs** :
    1. s'émanciper et être autonome, parcourir la station avec ses prothèses
    2. contribuer à solutionner l'attaque des androïdes

* **Attitude** : Daryl est très jovial et empathique. Il engagera spontannément la conversation avec Sullivan, le questionnant sur son voyage jusqu'ici, ce qui l'a motivé à accepter de venir sur Terra Nova, ses loisirs... Il aura la même attitude bienveillante et curieuse lors de l'acte 2, et sera ravi de rencontrer les autres PJs, qu'il encouragera régulièrement : _« ne baissons pas les bras, on va s'en sortir ! »_, _« je suis sûr qu'en réfléchissant bien, on peut trouver une solution »_, _« vous nous avez sauvé tout à l'heure, j'ai confiance et je compte sur vous »_, etc.

* **Roleplay** : son ton est toujours enjoué; il ponctue ses phrases de touches d'humour et de courts rires sincères : _« je ne te serre pas la main mais le cœur y est ! Ahaha 😄 »_. S'il est traumatisé à la vue de cadavres, adoptez un _roleplay_ significativement différent pour traduire ce choc. Daryl ne rira plus, il sera plus cynique et déprimé, et pourra même céder à la rage face aux androïdes.

* **Mort probable** : tué par les androïdes, ou possédé par une larve cosmique, ne pouvant se débattre avec ses prothèses HS.

### Ellen Frost
<img alt="Ellen Frost" src="img/helmet_concepts_by_akol3850_x2_bw_flipped_cc-by-nc.png" class="pnj">

* persuadée que GEC a causé l'attaque des androïdes pour mater les ouvriers, suite à la révolte sur Cepheus

* sait qu'il peut y avoir du **matériel utile pour se défendre au niveau 2**, dans les bureaux de GEC.

* il y a **un émeteur-récepteur longue portée au niveau 7**, dans sa cabine, qui lui permettait de contacter en secret d'autres leaders syndicalistes de stations et colonies environnantes. Cela peut sembler un moyen pour appaler à l'aide, mais il faudra compter plus de 16h avant d'avoir une réponse.

* à l'acte 2 les PJs la croiseront avec 4 dockers rescapés, donc 2 avec exo-squelettes

* **Objectifs** : durant les premières heures après l'attaque, elle s'efforcera de sécuriser une zone de repli au niveau 9, bien que l'androïde du poste de garde, armé, s'avère difficile à neutraliser. Ensuite&nbsp;:
    1. sauver et rassembler un maximum de dockers et manœuvres
    2. s'armer, lutter contre les androïdes et reprendre la station
    3. envoyer un SOS avec son récepteur

* **Attitude** : elle sera ouverte à l'entraide avec des PJs combatifs ayant des objectifs compatibles. Elle provoquera des PJs trop passifs en les exortant à _« se sortir les doigts du trou noir »_. Prête à mettre sa vie propre vie en jeu.

* **Roleplay** : s'exprime en phrases courtes, hachées, mordantes. Emploi de l'argot et du jargon de docker. Inspiration possible&nbsp;: _Camina Drummer_ dans _The Expanse_.

* **Mort probable** : tuée au combat par un androïde en fin d'acte 2, ou durant d'acte 3.

### Jada Jones
<img alt="Jada Jones" src="img/JadaJones-aka-ZoeWashburne.jpg" class="pnj">

* si elle est interrogée concernant le Tedium, Jones évoquera avoir mené son enquete, mais pretendra qu'elle n'a pas encore abouti. Elle mentionnera seulement avoir établi un lien entre cette drogue et le milieu de la prostitution.

* à l'acte 2 les PJs la croiseront accompagnée de 2 autres marshals rescapés, dont un sévèrement blessé. Avec leurs « smart guns », ils constituent les humains les mieux armés de la station.

* **Objectifs** :
    1. Garder son calme
    2. Appeler les secours / protéger les civils / évacuer
    3. Garder son calme

* **Attitude** : tendue, elle n'hésitera pas à clamer _« c'est moi qui commande »_ si on s'oppose à elle. Son calme apparent dissimule en fait une terrible panique : traumatisée par la mort d'O'Neil, elle ne que faire comme marshal de substitution.

* **Roleplay** : voix exagérément ferme et fébrile ; elle coupe la parole mais ensuite ne finit pas ses phrases ; elle répète souvent les même phrases : _« Allez on bouge ! »_, _« C'est moi le marshal »_, _« Il faut appeler les secours »_, _« Allez on bouge ! »_...

* **Mort probable** : face aux androïdes au court de l'acte 2

### Léo·Léa Waschenski
* le joueur concerné décidera si c'est réciproque, mais il est intéressant pour le scénario que Léo·Léa ait **le béguin pour Torrensen**.

* durant l'acte 1, Léo·Léa pourra être aperçu·e écouter avec attention les prêches de Watters. Sensible à la verve du prêtre et à la perspective d'un au-delà radieux, Léo·Léa **devient dévôt du culte de l'Ascension**, sans le dire à son paternel.

* si les PJs manquent **la transaction** entre « Le Marchand » et « Code-barres », considérez que Léo·Léa a assisté à la scène, et pourra en témoigner plus tard.

* **Objectifs** :
    1. Sauver son père
    2. Se planquer jusqu'à ce que ça se tasse
    3. Pas « voler » non, bien sûr, mais « récupérer » ce qui a de la valeur et qui sera perdu une fois la station abandonnée...

* **Attitude** : empathique, Léo·Léa se persuade vite que les PJs ont « bon fond », et leur accordera sa confiance sans réserve.

* **Roleplay** : sourire timide; yeux baissés, évite le regard des joueurs; s'exprime de manière hésitante; _« Oui, euh... D'accord »_...

* **Mort probable** : possédée par une larve cosmique, à cause de Watters ou juste parcqu'iel en aura subtilisé une durant la panique de l'acte 3

### Watters et le culte de l'Ascension
Là où le scénario détaille parfaitement les actions de Watters, le culte et ses membrent sont très peu mentionnés.


### Jouer un PNJ
**Yno** fournit une fiche de personnage vierge sur son site : [misterfrankenstein.com](https://www.misterfrankenstein.com/wordpress/?page_id=3)

Si un PJ meurt, et qu'un joueur doit incarner un PNJ, procédez ainsi :
* définissez ses valeurs d'Adrénaline et de Santé, selon ce qu'il a déjà traversé.
* transmettez au joueur tout ce que le PNJ sait des événements, et les informations qui le concerne dans cette aide de jeu
* laissez-le choisir ses objectifs, en cohérence abvec le personnage
* laissez-le répartir 35 points dans ses **Aptitudes**
* laissez le joueur choisir 3 **Spécialités** à +1R, et une Spécialités à +2R, parmi celles listées pages 82 & 84


## Intro - Connivences
D'expérience, il est intéressant d'avoir des raisons diégétiques pour que les personnages se face confiance, ou au moins aient un bon prétexte pour ouvrir la conversation&nbsp;: les PJs entre eux, mais aussi les PJs envers les PNJs.

Dans cette idée, voici donc un tableau de _Connivences_, des liens entre PJs / PNJs que vous pourrez découper, puis les faire piocher à chaque joueur en début de partie (un ou deux chacun, comme vous voulez)&nbsp;:

Votre voisin de gauche vous semble familier... L'auriez-vous déjà croisé lors d'un précédent job ? | Votre voisin de droite est un parent éloigné, que vous n'aviez pas revu depuis l'enfance. | Le PJ du joueur en face de vous a une tête qui t'inspire confiance.
-|-|-
On dit que **Brett Bettany** est sur Terra Nova&nbsp;: tu l'as déjà croisé, c'est un ouvrier borné mais réglo. | On dit que **Kenneth O'Neil** est sur Terra Nova&nbsp;: tu l'as déjà croisé, c'est un marshal strict mais juste. | D'après les rumeurs, une nouvelle drogue de synthèse circulerait sur **Terra Nova**
On dit que l'église de l'**Ascension** est présente sur Terra Nova&nbsp;: leur culte a sale réputation. | Tu as entendu dire que Terra Nova comporterait un **laboratoire secret** d'expérimentation. | D'après les rumeurs, ça chauffe sur **Cepheus**, entre la _Global Extraction Corporation_ et les colons.
On dit qu'**Ellen Frost** est sur Terra Nova&nbsp;: c'est une syndicaliste pugnace mais intègre. Tu l'as déjà vu arranguer l'équipage d'une station, comme dans la vidéo ci-jointe → | [![QRCode linking to YouTube video on Camina Drummer speech from The Expanse](qrcode-Camina-Drummer-speech.png)](https://youtu.be/yfOmQ0Zln6Y)


## Acte 1 - L'œil pour le détail

La table ci-dessous fournit quelques éléments pour étoffer les descriptions de la station orbitale, et réaliser un peu de _foreshadowing_ des événements à venir.

Durant l'acte 1, quel que soit l'endroit où se situent les PJs dans Terra Nova, demandez leur un jet de **Percevoir (+ Observation)**.

Décrivez alors au(x) PJ(s) avec le plus grand nombre de réussites l'élement ci-dessous correspondant à ce niveau de réussite, en déterminant un élement au hasard dans la liste avec 1D6. Barrez ensuite le résultat obtenu&nbsp;: s'il est tiré à nouveau lors d'un prochain jet, ignorez-le et passez au suivant.

**1-2 réussites** :

1. À travers un hublot vous appercevez **Cepheus**. À cet instant, la planète est éclairée d'un halo surréel, saisissant de beauté... Puis cet instant de grâce se dissipe.

2. Un peu plus loin, un employé en uniforme vert fouille dans sa poche en se dirigeant vers un CommLink, et **trébuche**. Heureusement un **androïde** _« Miranda »_ le rattrape _in-extremis_, lui évitant de se fracturer le crâne sur un rebord de métal. L'employé repousse le robot avec mépris... et lui crâche même au visage.

3. Un spot vidéo de **Revolve** vante l'autonomie révolutionnaire et l'incroyable précision des gestes de leurs androïdes

4. Un spot vidéo de pub pour **Global Extraction Corporation**, où le PJ attentif aperçoit un exosquelette faire un bras d'honneur en arrière-plan d'une séquence. Les PJs pourront ensuite apprendre que'il s'agit de Frost.

5. Dans l'espace, on voit à travers un hublot deux dockers en combinaison intercepter adroitement un petit astéroïde et en **découper un morceau au cutter-plasma**. Les PJs pourront ensuite apprendre que cette opération avait pour but de récupérer du minerai précieux détecté dans cette météorite.

6. Plus loin, une paroi rassemble plusieurs **graffitis**&nbsp;: _« L'Intergalactique sera le genre humain »_, _« Mort aux androïdes »_, _« Pour échapper à votre condition, rejoignez l'église de l'Ascension »_...

**3+ réussites** :

1. Des dockers **tabassent un androïde** prostré dans un coin. Libre au PJ d'intervenir où non. S'ils le font, les dockers s'en iront rapidement en grommelant.

2. Un ouvrier fébrile apostrophe le PJ&nbsp;: _« Hé ! Tu me regardes depuis tout à l'heure&nbsp;: t'en veux ? 100 crédits les 10 doses. »_ Libre au PJ d'accepter ou non le deal ou de bavarder avec cet ouvrier, un grand maigrichon aux cheveux blancs noués en queue de cheval nommé **Curtis Oakes**. Celui-ci s'éloigne bien vite dès qu'il comprend qu'il n'a pas d'acheteur potentiel en face de lui.

3. Dans un coin de la pièce / coursive, vous apercevez une **flaque de vomi**, avec des restes d'aliments mal digérés, notamment des haricots blancs, de la viande, ainsi que de petites gélules.

4. Une employée de Revolve (l'ingénieure en chef **Cotton**) apostrophe un officier de la sécurité de la station (la marshal adjointe **Jones**). Les deux femmes semblent énervées mais n'élèvent pas la voix pour autant. Tout ce que le PJ peut distinguer de leur échange c'est qu'il est question de ressources manquantes.

5. Certaines personnes autour portent des **chaussures magnétiques**. Elles doivent leur permettarent de se déplacer à l'extérieur de la station, ou lorsque l'anneau générateur de gravité de la station est arrêté.

6. Un androïde Arnie de sécurité, en uniforme bleu, transporte une caisse à bout de bras, sur laquelle le PJ distingue la mention « **explosif** ». Il disparaît dans l'ascenseur / dans l'angle d'un couloir.


## Acte 2 - Big brother is watching you
<img alt="Crouching android" src="img/CrouchingAndroid.jpg" class="medium float-left">

Bien que les **CommLinks** continuent à fonctionner après l'attaque des androïdes, depuis la salle réseau **Cory 3 écoute tous les appels** passés à travers la station.

Il profitera donc des informations échangées par les humains survivants via les CommLinks pour envoyer des androïdes à leur poursuite pour les exterminer.

Bien sûr, aux joueurs de le découvrir par eux-même !
En tant qu'Admin, notez donc bien ce que les joueurs mentionnent comme lieux dans la station durant leurs échanges entre eux ou avec les PNJs par les CommLinks...


## Acte 2 - Back to medbay
Durant l'acte 2, je vous recommande d'infliger assez vites de sérieux dégâts aux PJs&nbsp;:

* ils prendront ainsi pleinement conscience de la dangerosité de l'environnement
* cela leur donnera une bonne raison de vouloir retourne au **cabinet médical** du niveau 5

... TODO


## Acte 2 - Trolley dilemna au laboratoire
Cette scène vise à mettre les PJs face à un dilemne moral : **de quel PNJ sauver la vie** ?

**Prérequis** à cette scène :

* les PJs arrivent au **niveau 3**
* **Daryl** s'y trouve, dans le laboratoire
* **Cotton** est déjà sur place, dans la salle d'analyse, ou elle accompagne les PJs et s'y précipite en arrivant, via le sas

**Disposition des lieux** :

* le **sas privé**, en plus de l'accès extérieur, comporte deux portes : l'une mène à une coursive, l'autre à la salle d'analyse
* la **salle d'analyse est un cul-de-sac**, et contient tous les échantillons et données les plus précieuses de Revolve sur la station
* des écrans suspendus au mur, visibles dans tout le laboratoire, permettent de voir ce qu'il se passe dans le sas privé et la salle d'analyse

Au début, laissez les PJs explorer les lieux, plus ou moins prudemment.
Ils ne doivent pas s'en douter, mais aucun danger ne les attend initiallement.

**Sullivan** sera probablement heureux de retrouver Daryl.
Celui-ci est soulagé de voir les PJs, et reprend espoir.
Rapidement, il explique qu'il va récupère ses prothèses de jambes pour pouvoir les accompagner.
Il se dirige alors vers le sas, où il commence à fouiller parmi les caisses entreposées.
Il se déplace en rampant, mais refuse toute aide.

De son côté, Cotton en train de récupérer un maximum de données et d'échantillons précieux, et déclenche également en secret un début d'incendie.
À ce moment là, 5 androïdes vont faire leur apparition.
La réussite d'un jet de **Percevoir (+ Observation)** permettra à certains PJs des les entendre arriver et d'anticiper leur arrivée en nombre, mais les PJs n'auront pas le temps de prévenir ou de rejoindre Daryl dans le sas.

Si les PJs sont trop combatifs et envisagent de leur faire face, indiquez que ces robots se sont **blindés** en soudant des plaques de métal sur leurs membres : torse, jambes, bras.
Cela les rend plus difficile à **Viser** (difficulté 3), et **réduit de 1 les dégâts au contact**.

L'idée est d'inciter les PJs à fuir ou se cacher initiallement.
Une fois dans le laboratoire, les androïdes entendent du bruit dans le sas et s'y dirigent immédiatement.
Daryl se planque dans une petite caisse et échappe initiallement à leur vigilance,
et les robots repèrent la présence de Cotton dans la salle d'analyse.
Comme celle-ci a bloqué la porte de son côté, ils commencent à la défoncer.

Les PJs peuvent suivre tout ce qui se passe en direct, y compris l'incendie qui se propage dans la salle d'analyse, et Cotton à l'intérieur, face à la caméra, qui leur fait de grands gestes d'appel à l'aide.

Dites aux joueurs qu'ils ont moins d'une minute pour réagir.
Si besoin, soufflez-leur que là où sont les PJs, ils accès aux commandes du sas...


## Acte ...
S'inspirer des travaux de l'acte 1 pour créer des situations lors des actes suivants
+ concevoir une situation spécifique au fantôme qui hante Arora
+ spécifier des morceaux audio spécifiques pour certaines scènes

Dans cette courte scène, tu vas jouer le **fantôme** qui hante **Arora**, à son insu.
Continue à jouer ton personnage, mais lorsque l'Admin (TODO)

Les androïdes ne se pressent pas et donnent une mort la moins douloureuse possible

![The Expanse](img/TheExpanse.webp)

<img class="large" alt="Androïde Cory 3" src="img/Cory3.jpg">

![](img/girl-with-gun.jpg)
<!-- Source : https://www.goodfon.com/fantasy/wallpaper-fantastika-art-devushka-sci-fi.html -->

![Donnager spaceship from The Expanse](img/TheExpanse-Donnager-by-7-X-cc-by.webp)

<img alt="" src="img/delivery_by_fernand0fc_bw_cc-by.jpg">

<img class="small" alt="Dead Spacer 2 Avatar by bmanhall" src="img/dead_space_2_avatar_by_bmanhall_eroded.png">


## Crédits & remerciements
Merci aux illustrateurs qui ont placé leur travail sous licence _Creative Commons_&nbsp;:

* [Blade Runner](https://www.deviantart.com/fernand0fc/art/Blade-Runner-825143976), [Delivery](https://www.deviantart.com/fernand0fc/art/Delivery-802145258), [HAZMAT](https://www.deviantart.com/fernand0fc/art/HAZMAT-695221129) & [HeadShots](https://www.deviantart.com/fernand0fc/art/HeadShots-743989425) de Fernando Correa - [CC BY](https://creativecommons.org/licenses/by/3.0/)
* [Helmet concepts](https://www.deviantart.com/akol3850/art/Helmet-concepts-540178128) de Godstime Ojinmah - [CC BY-NC](https://creativecommons.org/licenses/by-nc/3.0/)
* un dessin d'[Elliot Jolivet aka Tenseï réalisé lors d'Inktober 2017](https://www.behance.net/gallery/58695271/InkTober-2017)

<!-- Merci aux relecteurs & testeurs de cette aide de jeu : ... -->

Merci enfin aux développeurs des [logiciels libres](https://fr.wikipedia.org/wiki/Free/Libre_Open_Source_Software) employés&nbsp;: [le navigateur Firefox](https://www.mozilla.org/fr/firefox/), [le logiciel de dessin Gimp](https://www.gimp.org/), [l'éditeur de texte Notepad++](https://notepad-plus-plus.org/), [le lecteur de PDF Sumatra PDF](https://www.sumatrapdfreader.org), [le language de programmation Python](https://www.python.org/), les bibliothèques de code [mistletoe](https://pypi.org/project/mistletoe/) & [weasyprint](https://weasyprint.org/), et le terminal web [github.com/jacksonbenete/email_terminal](https://github.com/jacksonbenete/email_terminal). Les configurations des deux terminaux CommLinks sont disponibles ici : [Lucas-C/email_terminal/acte-1](https://github.com/Lucas-C/email_terminal/tree/acte-1) & [Lucas-C/email_terminal/acte-2](https://github.com/Lucas-C/email_terminal/tree/acte-2).

## Licence & feedbacks
<a class="float-left" rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">
    <img alt="Creative Commons License Attribution-NonCommercial-ShareAlike 4.0 Unported" src="img/cc-by-nc-sa.png">
</a>

Cette aide de jeu de Lucas Cimon est placée sous licence <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International</a>.

Les fichiers sources ayant permis de générer ce PDF sont disponibles [sur GitHub](https://github.com/Lucas-C/jdr/tree/master/ParadisPerdu). Version : 1.0

Cette aide de jeu est diffusée à prix libre.
Si vous souhaitez soutenir mes projets, vous pouvez me faire un don sur [lucas-c.itch.io](https://lucas-c.itch.io).

Je serais ravi d'avoir vos retours sur cette aide de jeu si vous l'employez.
Racontez-moi comment s'est passée votre partie via un commentaire [lucas-c.itch.io](https://lucas-c.itch.io) ou sur [mon blog](https://chezsoi.org/lucas/blog/pages/jeux-de-role.html).

<!--
Design goals:
* s'intégrer à l'histoire, en faisant de multiple références
* s'intégrer au système, en provoquant des jets de dés
* rendre la station plus "vivante" et mémorable
* fournir plus d'éléments scénaristiques structurants pour les actes 2 & 3
* forcer les joueurs à faire des choix cornéliens, aux conséquences palpables
* amener des éléments d'intrigue supplémentaires dans l'acte 1 qui seront exploitées lors des actes suivants
* donner le sentiment aux joueurs qu'ils risquent leur peau à tout instant dans les actes 2 & 3
  -> 
* ne pas rallonger la durée de partie excessivement

Séquence de filtres Gimp employés :
1. Couleurs > Seuil noir & blanc
2. Filtres > Flou > Flou gaussien : 0,5
3. Filtres > Génériques > Eroder
4. Filtres > Génériques > Dilater
Séquence alternative :
1. Convert to greyscale
2. Convert to indexed palette with 3/4 colors

Com'
* article blog : mentionner scénario Silent Hil qui m'avait marqué + adj Scavengers précédente
    + modifier le lien vers le blog ci-dessus une fois publié
* itch.io : modifier les liens itch.io ci-dessus une fois la page publiée
-->
