[![](https://travis-ci.org/Lucas-C/jdr.svg?branch=master)](https://travis-ci.org/Lucas-C/jdr)

La plupart des prototypes dans ce repo reposent sur le script NodeJS [md2html](https://github.com/Lucas-C/linux_configuration/blob/master/bin/md2html.js)
pour générer une version HTML à partir de la version Markdown.

Une version PDF peut être générée facilement avec NodeJS:

    npm install -g puppeteer-cli
    puppeteer print $infile.html $outfile.pdf

## Serveur local de développement

Nécessite Python et la lib `livereload`

    ./watch_and_serve.py

## Notes
Emojis utiles : ⚅ ⚠️ 💡 ✏ ❤️ 💔 💋 🍺 ⚗ 🧪 🔬📡 💉 💊 🚪 📜 📘 🏷 🎫 💬 👁️‍🗨️ 👁 💀 ☠ ⚰ 👻 🐉 🐲 🔮 🧙 🕵️ 🔍 🗝 🔓
☀️ 🌀 🌳 ⛏ 🛠️🔧⚙🧰 🗡 ⚔ 🔫 🛡 🔪 🧨 🏹 🎯 🏃 🧹 🧯 🛢 🧱 📦 💼 💰 🪙 💎 🏺 🏆 🗺 🧭 🃏 🎴 ♟ 🧩 ⏳ ⏱ 🕓 🌡 ⛔ ☢ ☣ ♾ ♻ ✅ ✔ ❌

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Le contenu de ce dépôt est sous license <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a>

<!--
Ideas:
- https://css-tricks.com/almanac/properties/s/shape-outside/ -> limited to float right / left
- SVG patterns: https://www.heropatterns.com/
- JS animations to integrate:
  * https://www.dwitter.net/d/1494
  * https://www.dwitter.net/d/888
  * https://www.dwitter.net/d/1231
  * https://www.dwitter.net/d/4509
  * https://www.dwitter.net/d/16784
  * http://rachelbythebay.com/fun/square/
  * http://rachelbythebay.com/fun/chk/
  * https://github.com/ribab/quadart
- top banner: http://hondu.co
Cool fonts:
- Handwriting: https://www.dafont.com/fr/handwriting3.font?l[]=10&l[]=1
- Zalgo: https://stackoverflow.com/questions/6579844/how-does-zalgo-text-work
-->
