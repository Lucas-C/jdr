#!/usr/bin/env python3
from glob import glob
from os import listdir
from os.path import basename, dirname, isdir
from livereload import Server, shell

SCRIPT_DIR = dirname(__file__)

server = Server()
for folder in [SCRIPT_DIR] + [d for d in listdir(SCRIPT_DIR) if isdir(d)]:
    md_filenames = set(glob(folder + '/*.md'))
    for md_filename in md_filenames:
        base_md_filename, cwd = basename(md_filename), dirname(md_filename)
        if base_md_filename in ('index.md', 'LICENSE.md', 'README.md'):
            continue
        print('Watching', md_filename)
        output = folder + '/index.html' if folder != SCRIPT_DIR else md_filename.replace('.md', '.html')
        cmd = shell('md2html ' + base_md_filename, cwd=cwd, output=output)
        server.watch(md_filename, cmd)
        for html_filename in glob(folder + '/*.html'):
            if html_filename.replace('.html', '.md') not in md_filenames:
                print('Watching', html_filename)
                server.watch(html_filename, cmd)
server.serve(root=SCRIPT_DIR)
