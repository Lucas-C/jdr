#!/usr/bin/env python3
from livereload import Server, shell
regen_html = shell('md2html gdav.md', output='gdav.html')
server = Server()
server.watch('gdav.md', regen_html)
server.watch('resolution-table.html', regen_html)
server.serve()
