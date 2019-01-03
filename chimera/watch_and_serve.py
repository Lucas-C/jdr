#!/usr/bin/env python3
from livereload import Server, shell
server = Server()
server.watch('chimera.md', shell('md2html chimera.md', output='chimera.html'))
server.serve()
