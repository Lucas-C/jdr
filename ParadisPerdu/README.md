Présentation officielle du jeu : [Paradis Perdu @ misterfrankenstein.com](https://www.misterfrankenstein.com/wordpress/?p=5388)

Les aides de jeux officielles sont téléchargeables sur cette page : <https://www.misterfrankenstein.com/wordpress/?page_id=3>

Mes notes de préparation : [lien public SimpleNote](http://simp.ly/p/gWh9MJ)

## Modules de secours
Une aide de jeu composée d'un ensemble de modules optionnels, pour ajouter des rebondissements supplémentaires au scénario original. Ils m'ont également beaucoup aidé en tant que MJ pour préparer ma partie, et compléter quelques points non détaillés dans le jeu de base :
[TerraNova-ModulesDeSecours.pdf](https://lucas-c.github.io/jdr/ParadisPerdu/TerraNova-ModulesDeSecours.pdf)

Pour regénérer le PDF avec Python :
```
pip install mistletoe weasyprint
./adj2pdf.py
```

## Galerie d'images
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-acte-1/
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-acte-2/
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-acte-3/
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-persos/

Pour télécharger et afficher ces albums dans une galerie web locale avec [Sigal](http://sigal.saimon.org/en/latest/), qui intègre notamment un mode diaporama :
```
./build.sh
sigal serve --browser
```

## Ambiance sonore
- Playlist officielle de Yno : [YouTube](https://youtube.com/playlist?list=PL5rCR6hQfFR7g_6M8tLFtZCsRoyf1tJ45)
- Playlist The Expanse : [YouTube](https://www.youtube.com/playlist?list=PLLcod52t0kpfVsHz0laVYGX0owh05NR5W)
- Playlist perso de musiques d'ambiances pour l'acte 1 : [YouTube](https://youtube.com/playlist?list=PLLgE-ga3W_kZtrfXpoCl29f0AaEm1lJ1W)
- Playlist perso de musiques d'ambiances pour les actes 2 & 3 : [YouTube](https://www.youtube.com/playlist?list=PLLgE-ga3W_kZxl-ncvX6RB6knVt3jO3CL)
- Morceaux pour scènes spécifiques : [playlist YouTube](https://www.youtube.com/playlist?list=PLLgE-ga3W_kb8BypATCINn9FFoo_IUAj0) - Emplois suggérés :
    * [CYBERPUNK IS COMING - Extra Terra](https://www.youtube.com/watch?v=6Pia2X856wo) : crescendo de tension qui monte doucement **→** parfait pour rythmer un rebondissement scénaristique
    * [Beam - Volkor X](https://www.youtube.com/watch?v=kT7kZ7HPJYM) : crescendo très épique **→** idéal pour une transition d'acte ou l'épilogue
    * [ludoWic - Katana ZERO](https://www.youtube.com/watch?v=_pMyRRFUMBE) : **→** 

## Clips vidéos
* [Trailer de L'Antre de Khamûl](https://www.youtube.com/watch?v=Za2wS_ldKTw)
* [Falling Frontier Trailer @ YouTube](https://www.youtube.com/watch?v=I4zto6KRnWQ) : les 2 premières minutes pour l'intro
* [Enders Game Battle School @ YouTube](https://www.youtube.com/watch?v=t-dxN6VU-Io) : pour l'arrivée sur la station
* [Dead Space | Bande-annonce officielle @ YouTube](https://www.youtube.com/watch?v=l5WeBNfX-og) : pour introduire les créatures dans l'acte 3
* [Dead Space | Lullaby Trailer @ YouTube](https://www.youtube.com/watch?v=2f7sJyIDU-Q) : pour l'acte 3

Le script [gen_video_clips.sh](./gen_video_clips.sh) se charge de télécharger certaines de ces vidéos pour les rendre disponibles dans la galerie Sigal.

## Voix d'androïdes
Le script [android-voice.sh](./android-voice.sh) permet une génération de voix robotique avec l'emploi de [espeak](https://doc.ubuntu-fr.org/espeak).
