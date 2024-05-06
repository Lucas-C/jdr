Présentation officielle du jeu : https://www.misterfrankenstein.com/wordpress/?p=5388

Les aides de jeux officielles sont téléchargeables sur cette page : https://www.misterfrankenstein.com/wordpress/?page_id=3

Mes notes de préparation : [lien public SimpleNote](http://simp.ly/p/gWh9MJ)

# Lieux emblématiques
Une aide de jeu pour aider la meneuse de jeu à décrire la différentes zone de la station,
et créer des intrigues complémentaires via l'environnement :

* [TerraNova-LieuxEmblematiques.md](./TerraNova-LieuxEmblematiques.md)
* [TerraNova-LieuxEmblematiques.pdf](https://lucas-c.github.io/jdr/ParadisPerdu/TerraNova-LieuxEmblematiques.pdf)

Pour regénérer le PDF avec Python :
```
pip install mistletoe weasyprint
./adj2pdf.py
```

# Galerie d'images
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-acte-1/
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-acte-2/
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-acte-3/
* https://www.pinterest.fr/drmaxkurt/paradis-perdu-persos/

Pour télécharger et afficher ces albums dans une galerie web locale avec [Sigal](http://sigal.saimon.org/en/latest/), qui intègre notamment un mode diaporama :
```
./build.sh
sigal serve --browser
```

# Clips vidéos
* [Falling Frontier Trailer @ YouTube](https://www.youtube.com/watch?v=I4zto6KRnWQ) : les 2 premières minutes pour l'intro
* [Enders Game Battle School @ YouTube](https://www.youtube.com/watch?v=t-dxN6VU-Io) : pour l'arrivée sur la station
* [Dead Space | Bande-annonce officielle @ YouTube](https://www.youtube.com/watch?v=l5WeBNfX-og) : pour introduire les créatures dans l'acte 3
* [Dead Space | Lullaby Trailer @ YouTube](https://www.youtube.com/watch?v=2f7sJyIDU-Q) : pour l'acte 3

Le script `gallery/gen_video_clips.sh` se charge de télécharger certaines de ces vidéos pour les rendre disponibles dans la galerie Sigal.

## Voix d'androïdes
Le script [android-voice.sh](./android-voice.sh) permet une génération de voix robotique avec l'emploi de [espeak](https://doc.ubuntu-fr.org/espeak).
