#!/usr/bin/env python3
# USAGE: ./watch_and_serve.py [--pdf]
import sys
from glob import glob
from os import listdir
from os.path import basename, dirname, isdir, splitext
from unittest.mock import patch

from livereload.server import Server, StaticFileHandler, shell


SCRIPT_DIR = dirname(__file__)


class CustomStaticFileHandler(StaticFileHandler):
    'Adds UTF charset to COntent-Type header for HTML files'
    def get_content_type(self):
        if splitext(self.absolute_path)[1] == '.html':
            return 'text/html; charset=utf-8'
        return super().get_content_type()


def chain(cmd1_func, cmd2_str):
    def run_shell():
        cmd1_func()
        return shell(cmd2_str)()
    return run_shell


server = Server()
for folder in [SCRIPT_DIR] + [d for d in listdir(SCRIPT_DIR) if isdir(d)]:
    md_filenames = set(glob(folder + '/*.md'))
    md2html_cmds = []
    for md_filename in md_filenames:
        base_md_filename, cwd = basename(md_filename), dirname(md_filename)
        if base_md_filename in ('index.md', 'LICENSE.md', 'README.md'):
            continue
        output_html_filepath = folder + '/index.html' if base_md_filename.replace('.md', '') == folder else md_filename.replace('.md', '.html')
        cmd = shell('md2html ' + base_md_filename, cwd=cwd, output=output_html_filepath)
        print('Watching', md_filename, '->', output_html_filepath, end='')
        if '--pdf' in sys.argv:
            output_pdf_filepath = md_filename.replace('.md', '.pdf')
            cmd = chain(cmd, f'puppeteer print {output_html_filepath} {output_pdf_filepath}')
            print('->', output_pdf_filepath, end='')
        print()
        server.watch(md_filename, cmd)
        md2html_cmds.append(cmd)
    for html_filename in glob(folder + '/*.html'):
        if not html_filename.endswith('/index.html') and html_filename.replace('.html', '.md') not in md_filenames:
            print('Watching', html_filename)
            for cmd in md2html_cmds:
                server.watch(html_filename, cmd)
    for css_filename in glob(folder + '/*.css'):
        print('Watching', css_filename)
        for cmd in md2html_cmds:
            server.watch(css_filename, cmd)
    for js_filename in glob(folder + '/*.js'):
        print('Watching', js_filename)
        for cmd in md2html_cmds:
            server.watch(js_filename, cmd)
with patch('livereload.server.StaticFileHandler', CustomStaticFileHandler):
    server.serve(root=SCRIPT_DIR)
