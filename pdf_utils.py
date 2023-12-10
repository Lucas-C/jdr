import asyncio, io, logging
from traceback import print_exc

from mistletoe import markdown, HtmlRenderer
from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration
try:
    from livereload.server import Server, StaticFileHandler
    from livereload.watcher import get_watcher_class
    from xreload import xreload
    OPT_DEPS_LOADED = True
except ImportError:
    OPT_DEPS_LOADED = False
    StaticFileHandler = object


def markdown2pdf(dir, md_filepath, css_filepath):
    with open(md_filepath, encoding="utf8") as md_file:
        html = markdown(md_file.read(), renderer=CustomHtmlRenderer)
    html_doc = f"""<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>JdR - Work-in-progress</title>
        <link rel="stylesheet" href="{css_filepath.name}">
    </head>
    <body>{html}</body>
</html>"""
    with open(dir / "index.html", "w", encoding="utf8") as html_file:
        html_file.write(html_doc)
    font_config = FontConfiguration()
    css = CSS(filename=css_filepath, font_config=font_config)
    bytes_io = io.BytesIO()
    HTML(base_url=str(dir), string=html).write_pdf(bytes_io, stylesheets=[css], font_config=font_config)
    return bytes_io


async def start_watch_and_rebuild(module, *files_to_watch):
    "Watch files and on change, reload Python modules & call build_pdf()"
    if not OPT_DEPS_LOADED:
        raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
    logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.getLogger("livereload").setLevel(logging.INFO)
    watcher = get_watcher_class()()
    watcher.watch(__file__, module.build_pdf)
    for filepath in files_to_watch:
        watcher.watch(str(filepath), module.build_pdf)
    print("Watcher started...")
    await watch_periodically(module, watcher)


async def watch_periodically(module, watcher, delay_secs=.8):
    try:
        watcher.examine()
    except Exception:
        print_exc()
    await asyncio.sleep(delay_secs)
    xreload(module, new_annotations={"XRELOADED": True})
    await asyncio.create_task(watch_periodically(module, watcher))


def watch_xreload_and_serve(module, root_dir, *files_to_watch):
    """
    * watch files and on change, reload Python modules & call build_pdf()
    * starts a HTTP server
    """
    if not OPT_DEPS_LOADED:
        raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
    logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.getLogger("livereload").setLevel(logging.INFO)
    def on_change():
        xreload(module, new_annotations={"XRELOADED": True})
        module.build_pdf()
    server = Server()
    for filepath in files_to_watch:
        server.watch(str(filepath), on_change)
    server.SFH = CustomStaticFileHandler
    print("Now starting HTTP server - blocking call to .serve()")
    server.serve(root=str(root_dir))


class CustomHtmlRenderer(HtmlRenderer):
    # Does not insert align="left" attributes in table cells,
    # in order for TidyHTML not to produce: Warning: <td> attribute "align" not allowed for HTML5
    def render_table_cell(self, token, in_header=False) -> str:
        template = '<{tag}{attr}>{inner}</{tag}>\n'
        tag = 'th' if in_header else 'td'
        if token.align is None:
            align = None
        elif token.align == 0:
            align = 'center'
        elif token.align == 1:
            align = 'right'
        attr = ' align="{}"'.format(align) if align else ''
        inner = self.render_inner(token)
        return template.format(tag=tag, attr=attr, inner=inner)


class CustomStaticFileHandler(StaticFileHandler):
    "Adds UTF charset to Content-Type header for HTML files"
    def get_content_type(self):
        content_type = super().get_content_type()
        if content_type == "text/html":
            content_type = "text/html; charset=utf-8"
        return content_type
