- https://chezsoi.org/lucas/jdr/psirun/CR_2016-12-18.html
- https://chezsoi.org/lucas/jdr/psirun/CR_2017-12-27.html

    md2html CR_2016-12-18.md > CR_2016-12-18.html
    md2html CR_2017-12-27.md > CR_2017-12-27.html
    java -jar ditaa0_9.jar CR_2017-12-27_piste.txt

<!--
    for cr in CR_*.html; do echo $cr; tq img -a src < $cr; done > rsync.include
    rsync --files-from=rsync.include -rv . ct-lucas:/usr/share/nginx/html/lucas/jdr/psirun/
-->
