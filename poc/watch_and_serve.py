#!/usr/bin/env python3
from livereload import Server, shell
server = Server()
regen_html = shell('md2html PorteObjectifCartes.md', output='PorteObjectifCartes.html')
server.watch('PorteObjectifCartes.md', regen_html)
server.watch('character-sheet.html', regen_html)
server.serve()
