[![build status](https://github.com/Lucas-C/jdr/workflows/build/badge.svg)](https://github.com/Lucas-C/jdr/actions?query=branch%3Amaster)

Sources de <https://lucas-c.github.io/jdr/>

* mon site web : [chezsoi.org](https://chezsoi.org/lucas/blog/) - les articles à propos de jeux de rôle : [#jdr](https://chezsoi.org/lucas/blog/tag/jdr.html)
* les jeux en dévelopement : [Projets en cours](https://chezsoi.org/lucas/blog/pages/projets-en-cours.html)
* tous les JdR que j'ai conçu : [Mes jeux de rôle](https://chezsoi.org/lucas/blog/pages/jeux-de-role.html)

## Comment ça marche ?

### Génération de PDFs avec markdown-it & puppeteer
Les plus anciens prototypes dans ce repo reposent sur le script NodeJS [md2html](https://github.com/Lucas-C/linux_configuration/blob/master/bin/md2html.js)
pour générer une version HTML à partir de la version Markdown.

    npm ci
    node ./md2html.js file.md > file.html

Une version PDF peut ensuite être générée facilement avec [puppeter](https://pptr.dev/):

    node ./puppeteer-print.js $infile.html $outfile.pdf

#### Serveur local de développement

Nécessite Python et la lib `livereload`

    ./watch_and_serve.py

### Génération de PDFs avec WeasyPrint
Mes jeux les plus récents emploient [WeasyPrint](https://weasyprint.org/) et quelques autres bibliothèques Python pour générer des fichiers PDF à partir de fichier Markdown :

    pip install -r requirements.txt livereload xreload
    # exécuter ensuite le script *pdf.py dans le sous-dossier


## Notes
Emojis utiles : ⚅ ⚠️ 💡 ✏ ❤️ 💔 💋 🍺 ⚗ 🧪 🔬📡 💉 💊 🚪 📜 📘 🏷 🎫 💬 👁️‍🗨️ 👁 💀 ☠ ⚰ 👻 🐉 🐲 🔮 🧙 🕵️ 🔍 🗝 🔓
☀️ 🌀 🌳 ⛏ 🛠️ 🔧 ⚙ 🧰 🗡 ⚔ 🔫 🛡 🔪 🧨 🏹 🎯 🏃 🧹 🧯 🛢 🧱 📦 💼 💰 🪙 💎 🏺 🏆 🗺 🧭 🃏 🎴 ♟ 🧩 ⏳ ⏱ 🕓 🌡 ⛔ ☢ ☣ ♾ ♻ ✅ ✔ ❌
💣 🔥 ⚡ 🧲 💧 ☁️

Also: <https://shapecatcher.com>


## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br>Sauf indication contraire, le contenu de ce dépôt est sous license <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a>

<!--
Ideas:
- wrap content around a floated element’s bounding-box: https://css-tricks.com/almanac/properties/s/shape-outside/ -> limited to float right / left
- https://roughjs.com draw in a sketchy, hand-drawn-like, style
- SVG patterns: https://www.heropatterns.com/
- JS animations to integrate:
  * raining: https://www.dwitter.net/d/1494
  * rotating coin: https://www.dwitter.net/d/1231
  * rotating fractal: https://www.dwitter.net/d/4509
  * incredible animated "generating" pattern: https://www.dwitter.net/d/16784
  * birds incoming: https://www.dwitter.net/d/17888
  * squares appearing in the background: http://rachelbythebay.com/fun/square/
  * checkboxes: http://rachelbythebay.com/fun/chk/
  * https://github.com/ribab/quadart
  * A City in 185 Bytes of JS: https://www.reddit.com/r/generative/comments/o0xduf/a_city_in_185_bytes_of_javascript/
- https://markodenic.com/css-tips/
  * typing effect
  * `drop-shadow()` to create a shadow on the image’s **content**
  * smooth scrolling
  * `background-clip` to draw titles using a background image
- Joy Division effect: https://www.reddit.com/r/glitch_art/comments/gmftbv/gg_haze/
- take inspiration from this top banner: http://hondu.co
- cf. also notes.py libs lucashadfield/speck, Circle-Evolution
- https://www.reddit.com/r/proceduralgeneration/comments/gxqclx/automated_painting_in_python/
  (uses external brush images)
- https://github.com/georgedoescode/sketchbook/tree/master/06.19/recircles :
  nice small colored geometric shapes, ideal for small embellishments (JS -> canvas)

Cool fonts:
- Handwriting: https://www.dafont.com/fr/handwriting3.font?l[]=10&l[]=1
- Zalgo cryptic pseudo-font: https://stackoverflow.com/questions/6579844/how-does-zalgo-text-work
- sǝʌᴉʇɐuɹǝʇlɐ / https://qwerty.dev/backwards-text-generator/
-->
