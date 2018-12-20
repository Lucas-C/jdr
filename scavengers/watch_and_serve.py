#!/usr/bin/env python3
from livereload import Server, shell
regen_html = shell('md2html adj-scavengers.md', output='adj-scavengers.html')
server = Server()
server.watch('adj-scavengers.md', regen_html)
server.serve()
