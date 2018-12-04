#!/usr/bin/env python3
from livereload import Server, shell
regen_html = shell('md2html Scavengers.md', output='Scavengers.html')
server = Server()
server.watch('Scavengers.md', regen_html)
server.serve()
