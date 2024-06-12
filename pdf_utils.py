import asyncio, io, logging, re
from datetime import datetime
from traceback import print_exc
from urllib.parse import quote

from bs4.builder._htmlparser import HTMLParserTreeBuilder
from bs4 import BeautifulSoup
from mistletoe import markdown, HtmlRenderer
from mistletoe.block_token import tokenize, BlockToken
import pikepdf
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

ANCHOR_ID_CHAR_RANGE_TO_IGNORE = "[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+"
ANCHOR_ID_CHAR_RANGE_TO_IGNORE_RE = re.compile(ANCHOR_ID_CHAR_RANGE_TO_IGNORE)
ANCHOR_ID_CHAR_RANGE_TO_IGNORE_PREFIX_RE = re.compile("^" + ANCHOR_ID_CHAR_RANGE_TO_IGNORE)


def markdown2pdf(dir, md_filepath, css_filepath=None, lang=None):
    with open(md_filepath, encoding="utf8") as md_file:
        md_content = md_file.read()
    md_content = handle_ponctuation_whitespaces(md_content)
    html = markdown(md_content, renderer=CustomHtmlRenderer)
    html = add_id_attrs_on_headings(html)
    lang_attr = f' lang="{lang}"' if lang else ''
    link_tag = f'<link rel="stylesheet" href="{css_filepath.name}">' if css_filepath else ''
    html_doc = f"""<!doctype html>
<html{lang_attr}>
    <head>
        <meta charset="utf-8">
        <title>JdR - Work-in-progress</title>
        {link_tag}
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


def handle_ponctuation_whitespaces(md_content):
    "Prevents line breaks before & after guillemets"
    md_content = md_content.replace(" :", "&nbsp;:")
    md_content = md_content.replace("« ", "«&nbsp;")
    md_content = md_content.replace(" »", "&nbsp;»")
    return md_content


class MyTreeBuilder(HTMLParserTreeBuilder):
    # Recipe from: https://bugs.launchpad.net/beautifulsoup/+bug/1767999
    DEFAULT_PRESERVE_WHITESPACE_TAGS = set(["a", "b", "em", "h1", "h2", "h3", "h4", "li", "p", "strong", "td", "th"])

def add_id_attrs_on_headings(html):
    soup = BeautifulSoup(html, builder=MyTreeBuilder, features="html.parser")
    for tag_name in ("h1", "h2", "h3", "h4"):
        for heading in soup.find_all(tag_name):
            heading["id"] = slugify(heading.string)
    return soup.prettify(formatter="html5")


def slugify(s):
    # Reproduce slugify() in md2html.js
    s = s.strip()
    s = s.lower()
    s = re.sub(ANCHOR_ID_CHAR_RANGE_TO_IGNORE_PREFIX_RE, "", s)
    s = re.sub(ANCHOR_ID_CHAR_RANGE_TO_IGNORE_RE, "-", s)
    return quote(s)


def set_metadata(filepath, title=None, description=None, keywords=()):
    with pikepdf.open(filepath, allow_overwriting_input=True) as pdf:
        with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
            if title:
                meta["dc:title"] = title
            if description:
                meta["dc:description"] = description
            if keywords:
                meta["pdf:Keywords"] = " ".join(keywords)
            meta["dc:creator"] = ["Lucas Cimon"]
            meta["xmp:MetadataDate"] = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat()
        pdf.save()


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
    def __init__(self):
        super().__init__(TripleCommaDiv)

    def render_triple_comma_div(self, token) -> str:
        inner = self.render_inner(token)
        return f'<div class="{token.classes}">{inner}</div>'

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


class TripleCommaDiv(BlockToken):
    """
    Simple <div> block. (["::: class1 class2", ..., ":::"])
    Block start is indicated by a line starting with at least three ":" characters.
    Same for the block end.
    The exact number of ":" characters does not matter at all.

    This aims to be compliant / cover the same functionality as markdown-it-container:
    https://www.npmjs.com/package/markdown-it-container

    I shared this implementation there: https://github.com/miyuchina/mistletoe/issues/217

    Attributes:
        classes (str): CSS class names inserted in the "class" HTML attribute
    """

    @staticmethod
    def start(line):
        return line.startswith(":::")

    @classmethod
    def read(cls, lines):
        first_line = next(lines)
        classes = first_line.lstrip(":").strip()
        delimiter = cls._delimiter_from_line(first_line)
        child_lines = []
        for line in lines:
            if line.startswith(delimiter):
                if line[len(delimiter)] != ":":
                    # End block found:
                    break
                else:
                    print(f"WARN: Unexpected longer delimiter: '{line.rstrip()}' - Expected block end delimiter: {delimiter}")
            child_lines.append(line)
        children = tokenize(child_lines)
        return classes, children

    @staticmethod
    def _delimiter_from_line(line):
        level = 0
        while line[3 + level] == ":":
            level += 1
        return ":" * (3 + level)

    def __init__(self, match):
        self.classes, self.children = match


class CustomStaticFileHandler(StaticFileHandler):
    "Adds UTF charset to Content-Type header for HTML files"
    def get_content_type(self):
        content_type = super().get_content_type()
        if content_type == "text/html":
            content_type = "text/html; charset=utf-8"
        return content_type
