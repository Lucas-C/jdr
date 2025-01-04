Dernière version du PDF: [OriMushi.pdf](https://lucas-c.github.io/jdr/OriMushi/OriMushi.pdf)

Pour regénérer le PDF avec Python :
```
pip install mistletoe weasyprint
./md2pdf.py
```

L'ouverture des fichiers `.fodg` nécessite l'installation préalable des polices `Odachi` & `Xangda Shiny`.

<!--
### OriMushi-FeuillePersonnageEtendue.fodg
Binary data (images) embedded in file:

(line 738 - draw:layer="controls")
<office:binary-data>/9j/4AAQSkZJRgABAQIAdgB2AAD/4QCuRXhpZgAASUkqAAgAAAAHABIBAwABAAAAAQAAABoB
       BQABAAAAYgAAABsBBQABAAAAagAAACgBAwABAAAAAwAAADEBAgANAAAAcgAAADIBAgAUAAAA
       gAAAAGmHBAABAAAAlAAAAAAAAAD8KQAAWwAAAPwpAABbAAAAR0lNUCAyLjEwLjM4AAAyMDI0
       OjEyOjI5IDE3OjA3OjUzAAEAAaADAAEAAAABAAAAAAAAAP/hDo1odHRwOi8vbnMuYWRvYmUu
    ac-illust-japanese-frame-square-brush-exceeding.jpg

(line 1089)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAAKoAAAClCAYAAADMIGZXAAAAw3pUWHRSYXcgcHJvZmlsZSB0
       eXBlIGV4aWYAAHjabVBbDsQgCPznFHsEeWjxOPaxyd5gj78odFObTuKADBkROL6fN7w6CAUk
    checkbox-cc0.png

(line 2091)
<office:binary-data>/9j/4AAQSkZJRgABAQEC0ALQAAD/4QX0RXhpZgAASUkqAAgAAAAJAA4BAgB7AgAAegAAABIB
    freepik-japanese-sumie-ink-circle.jpg

(line 48426)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAASwAAAFBCAYAAADNF5LxAAAAw3pUWHRSYXcgcHJvZmlsZSB0

(line 37343)
<office:binary-data>PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0idXRmLTgiPz4NCjwhRE9DVFlQRSBzdmcg
    freesvg-decorative-ying-yang-sign.svg

(line 39926)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAAsMAAALDCAYAAADwjA1CAAAACXBIWXMAAAX1AAAF9QGSAma6
    freesvg-decorative-ying-yang-sign.svg -> PNG

(line 48427)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAASwAAAFBCAYAAADNF5LxAAAAw3pUWHRSYXcgcHJvZmlsZSB0
       eXBlIGV4aWYAAHjabVBbDsQgCPznFHsEeVTxOPaV9AZ7/EXBpG12EocRdETg+F4nfDoIBWQp
    die-six.png

(line 49846)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAASwAAAFBCAYAAADNF5LxAAAAw3pUWHRSYXcgcHJvZmlsZSB0
       eXBlIGV4aWYAAHjabVBbDsQgCPznFHsEeah4HPtKeoM9/mLBpG12EofRUQRg/54HfAYIBSRX
    die-one.png

(line 51900)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAASwAAAFBCAYAAADNF5LxAAAAxHpUWHRSYXcgcHJvZmlsZSB0
       eXBlIGV4aWYAAHjabVBbDsQgCPznFHsEeVTxOPaV9AZ7/EXBpG12jMMI7YjA8b1O+HQQCshS
    die-five.png / die-four.png

(line 56555)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAABIkAAASyCAMAAAAF0UsEAAADAFBMVEVHcEz1X/8u0hEA+nsA
    sumi-e-cc0.png

(line 56869 - draw:layer="controls")
<office:binary-data>/9j/4AAQSkZJRgABAQIAdgB2AAD/4QCuRXhpZgAASUkqAAgAAAAHABIBAwABAAAAAQAAABoB
        BQABAAAAYgAAABsBBQABAAAAagAAACgBAwABAAAAAwAAADEBAgANAAAAcgAAADIBAgAUAAAA
        gAAAAGmHBAABAAAAlAAAAAAAAAD8KQAAWwAAAPwpAABbAAAAR0lNUCAyLjEwLjM4AAAyMDI0
        OjEyOjI5IDE3OjA2OjUwAAEAAaADAAEAAAABAAAAAAAAAP/hDo1odHRwOi8vbnMuYWRvYmUu
    ac-illust-japanese-frame-square-brush-partial.jpg

(line 57215 - draw:layer="controls")
<office:binary-data>/9j/4AAQSkZJRgABAQIAdgB2AAD/4QCuRXhpZgAASUkqAAgAAAAHABIBAwABAAAAAQAAABoB
       BQABAAAAYgAAABsBBQABAAAAagAAACgBAwABAAAAAwAAADEBAgANAAAAcgAAADIBAgAUAAAA
       gAAAAGmHBAABAAAAlAAAAAAAAAD8KQAAWwAAAPwpAABbAAAAR0lNUCAyLjEwLjM4AAAyMDI0
       OjEyOjI5IDE3OjA3OjUzAAEAAaADAAEAAAABAAAAAAAAAP/hDo1odHRwOi8vbnMuYWRvYmUu
    ac-illust-japanese-frame-square-brush-exceeding.jpg

(line 64305 - draw:layer="controls")
<office:binary-data>/9j/4AAQSkZJRgABAQIAdgB2AAD/4QCuRXhpZgAASUkqAAgAAAAHABIBAwABAAAAAQAAABoB
        BQABAAAAYgAAABsBBQABAAAAagAAACgBAwABAAAAAwAAADEBAgANAAAAcgAAADIBAgAUAAAA
        gAAAAGmHBAABAAAAlAAAAAAAAAD8KQAAWwAAAPwpAABbAAAAR0lNUCAyLjEwLjM4AAAyMDI0
        OjEyOjI5IDE3OjA2OjUwAAEAAaADAAEAAAABAAAAAAAAAP/hDo1odHRwOi8vbnMuYWRvYmUu
    ac-illust-japanese-frame-square-brush-partial.jpg

(line 64663)
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAArwAAAIzCAYAAADiXMpOAAAAxnpUWHRSYXcgcHJvZmlsZSB0
       eXBlIGV4aWYAAHjabVBBDsMgDLvzij0hxCkNz6Erk/aDPX+BpNLY5oqE2sIEp/56PtJtgLMk
    arrow.png

(line 69253 - draw:layer="layout")
<office:binary-data>iVBORw0KGgoAAAANSUhEUgAAAd0AAAE+CAYAAADI7cpCAAABhWlDQ1BJQ0MgcHJvZmlsZQAA
    plus1die.png
    
tl;dr : the solution was to move all objets to the draw:layer="layout" (some were in the "controls" layer)
-->
