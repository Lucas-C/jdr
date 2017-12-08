    md2html CR_2016-12-18.md > index.html
    (tq img -a src < CR_2016-12-18.html && echo couverture.png && echo index.html) > rsync.include
    rsync --files-from=rsync.include -rv . ct-lucas:/usr/share/nginx/html/lucas/jdr/psirun/
