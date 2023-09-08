#!/usr/bin/env python3
import webbrowser
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from livereload.server import Server

PORT = 8000
SCRIPT_DIR = Path(__file__).parent

def gen_index_html():
    env = Environment(loader=FileSystemLoader(SCRIPT_DIR), autoescape=True,
                      trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("Sombre-Tuile-editor.html")
    (SCRIPT_DIR / "index.html").write_text(template.render())

gen_index_html()
SERVER = Server()
SERVER.watch("SombreZero-TuilePerso.svg", gen_index_html)
SERVER.watch("Sombre-Tuile-editor.html", gen_index_html)
webbrowser.open(f'http://localhost:{PORT}')
SERVER.serve(root=str(SCRIPT_DIR), port=PORT)
