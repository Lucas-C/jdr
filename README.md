[![](https://travis-ci.org/Lucas-C/jdr.svg?branch=master)](https://travis-ci.org/Lucas-C/jdr)

La plupart des prototypes dans ce repo reposent sur le script NodeJS [md2html](https://github.com/Lucas-C/linux_configuration/blob/master/bin/md2html.js) pour générer une version HTML à partir de la version Markdown.

Une version PDF peut être générée facilement avec NodeJS:

    npm install -g puppeteer-cli
    puppeteer print $infile.html $outfile.pdf

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Le contenu de ce dépôt est sous license <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International</a>

<!--
Ideas:
- https://css-tricks.com/almanac/properties/s/shape-outside/ -> limited to float right / left
- JS animations to integrate:
  * https://www.dwitter.net/d/1494
  * https://www.dwitter.net/d/888
  * https://www.dwitter.net/d/1231
  * https://www.dwitter.net/d/4509
Cool manuscript fonts:
- https://www.dafont.com/fr/handwriting3.font?l[]=10&l[]=1
-->
