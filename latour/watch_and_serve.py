#!/usr/bin/env python3
from livereload import Server, shell
regen_html = shell('md2html latour.md', output='latour.html')
server = Server()
server.watch('latour.md', regen_html)
server.serve()
