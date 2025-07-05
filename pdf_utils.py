import asyncio, io, logging, re
from contextlib import contextmanager
from datetime import datetime
from functools import partial
from pathlib import Path
from random import shuffle
from traceback import print_exc
from urllib.parse import quote
from time import perf_counter

from bs4.builder._htmlparser import HTMLParserTreeBuilder
from bs4 import BeautifulSoup, NavigableString
from fpdf import FPDF, FPDF_VERSION
from fpdf.util import get_scale_factor
from mistletoe import markdown, HtmlRenderer
from mistletoe.block_token import tokenize, BlockToken
import pikepdf
from pypdf import PageObject, PdfReader, PdfWriter
from weasyprint import HTML, CSS, VERSION as WP_VERSION
from weasyprint.text.fonts import FontConfiguration
try:
    from livereload.server import Server, StaticFileHandler
    from livereload.watcher import get_watcher_class
    from xreload import xreload
    OPT_DEPS_LOADED = True
except ImportError:
    OPT_DEPS_LOADED = False
    StaticFileHandler = object

AUTHOR = "Lucas Cimon"

ANCHOR_ID_CHAR_RANGE_TO_IGNORE = "[\x00-\x2F\x3A-\x40\x5B-\x60\x7B-\uFFFF]+"
ANCHOR_ID_CHAR_RANGE_TO_IGNORE_RE = re.compile(ANCHOR_ID_CHAR_RANGE_TO_IGNORE)
ANCHOR_ID_CHAR_RANGE_TO_IGNORE_PREFIX_RE = re.compile("^" + ANCHOR_ID_CHAR_RANGE_TO_IGNORE)

logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
logging.getLogger("livereload").setLevel(logging.INFO)
# logging.getLogger("weasyprint").setLevel(logging.DEBUG)
# Avoid some useless verbose logs:
logging.getLogger("fontTools.subset").level = logging.WARN
logging.getLogger("fontTools.ttLib.tables._h_e_a_d").level = logging.ERROR
logging.getLogger("fontTools.ttLib.tables.O_S_2f_2").level = logging.ERROR


def markdown2pdf(dir, md_filepath, css_filepath=None, lang=None, metadata=None, bookmarks=True):
    with open(md_filepath, encoding="utf8") as md_file:
        return md2pdf(dir, md_file.read(), css_filepath, lang, metadata, bookmarks)

def md2pdf(dir, md_content, css_filepath=None, lang=None, metadata=None, bookmarks=True):
    html = md2html(dir, md_content, css_filepath, lang, metadata)
    return html2pdf(dir, html, css_filepath, lang, metadata, bookmarks)

def md2html(dir, md_content, css_filepath=None, lang=None, metadata=None):
    md_content = handle_ponctuation_whitespaces(md_content)
    html = markdown(md_content, renderer=CustomHtmlRenderer)
    html = modify_html(html)
    lang_attr = f' lang="{lang}"' if lang else ''
    link_tag = f'<link rel="stylesheet" href="{css_filepath.name}">' if css_filepath else ''
    title = (metadata or {}).get("title") or "JdR - Work-in-progress"
    html_doc = f"""<!doctype html>
<html{lang_attr}>
    <head>
        <meta charset="utf-8">
        <title>{title}</title>
        {link_tag}
    </head>
    <body>{html}</body>
</html>"""
    with open(dir / "index.html", "w", encoding="utf8") as html_file:
        html_file.write(html_doc)
    return html

def html2pdf(dir, html, css_filepath=None, lang=None, metadata=None, bookmarks=True):
    start = perf_counter()
    font_config = FontConfiguration()
    css = CSS(filename=css_filepath, font_config=font_config)
    bytes_io = io.BytesIO()
    doc = HTML(base_url=str(dir), string=html).render(font_config=font_config, stylesheets=[css])
    if not bookmarks:
        for page in doc.pages:
            page.bookmarks = []
    doc.metadata.authors = [AUTHOR]
    doc.metadata.created = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat()
    if lang:
        doc.metadata.lang = lang
    if metadata:
        title = metadata.get("title")
        if title:
            doc.metadata.title = title
        description = metadata.get("description")
        if description:
            doc.metadata.description = description
        keywords = metadata.get("keywords")
        if keywords:
            if any(" " in word for word in keywords):
                raise ValueError(f"PDF keywords should not contain any whitespace: '{keywords}'")
            doc.metadata.keywords = keywords
    doc.write_pdf(bytes_io)
    print(f"WeasyPrint PDF building duration: {perf_counter() - start:.1f}s")
    return bytes_io


def handle_ponctuation_whitespaces(md_content):
    "Prevents line breaks before & after guillemets"
    md_content = md_content.replace(" :", "&nbsp;:")
    md_content = md_content.replace("« ", "«&nbsp;")
    md_content = md_content.replace(" »", "&nbsp;»")
    return md_content


def modify_html(html):
    soup = BeautifulSoup(html, builder=MyTreeBuilder, features="html.parser")
    add_id_attrs_on_headings(soup)
    shuffle_tables(soup)
    add_table_of_contents(soup)
    return soup.prettify(formatter="html5")


class MyTreeBuilder(HTMLParserTreeBuilder):
    # Recipe from: https://bugs.launchpad.net/beautifulsoup/+bug/1767999
    DEFAULT_PRESERVE_WHITESPACE_TAGS = set(["a", "b", "dd", "em", "h1", "h2", "h3", "h4", "li", "p", "strong", "td", "th"])


def add_id_attrs_on_headings(soup):
    for tag_name in ("h1", "h2", "h3", "h4"):
        for heading in soup.find_all(tag_name):
            if not heading.get("id"):
                heading["id"] = slugify(heading.get_text())

def slugify(s):
    # Reproduce slugify() in md2html.js
    s = s.strip()
    s = s.lower()
    s = re.sub(ANCHOR_ID_CHAR_RANGE_TO_IGNORE_PREFIX_RE, "", s)
    s = re.sub(ANCHOR_ID_CHAR_RANGE_TO_IGNORE_RE, "-", s)
    return quote(s)


def shuffle_tables(soup, max_cols=4):
    "Performs cells shuffling in <table> tags under a .shuffle-col${i}-rows CSS class"
    # Note: tables rendered by mistletoe always have <thead> & <tbody> tags
    # and cells in the first row are <th> while other cells are <td>
    for i in range(1, max_cols + 1):
        for div in soup.find_all(class_=f"shuffle-col{i}-rows"):
            rows = div.find("table").find_all("tr")
            # 1. We build a mapping of "old" indices to "new" indices:
            index_map = list(range(len(rows)))
            shuffle(index_map)
            # 2. We extract all target cells from the HTML tree:
            cells = []
            for row in rows:
                child_tags = [cell for cell in row.children if not isinstance(cell, NavigableString)]
                cell = child_tags[i - 1]
                cells.append(cell)
                cell.extract()
            # 3. We insert the cells at their new position in the HTML tree:
            for j, row in enumerate(rows):
                cell = cells[index_map[j]]
                cell.name = "th" if j == 0 else "td"
                row.insert(i, cell)


def add_table_of_contents(soup):
    'Adds items to <ul class="toc"> tags based on its data-tags attribute'
    for ul in soup.find_all("ul", class_="toc"):
        heading_tags = ul.get("data-tags", "").split(" ")
        uls, curr_ul = [ul], ul
        last_heading_level, curr_li = None, None
        for heading in soup.find_all(heading_tags):
            level = int(heading.name[1])
            if last_heading_level:
                if level > last_heading_level:
                    assert (level - last_heading_level) == 1, "Case currently not handled"
                    curr_ul = soup.new_tag("ul")
                    curr_li.append(curr_ul)
                    uls.append(curr_ul)
                elif level < last_heading_level:
                    assert (last_heading_level - level) == 1, "Case currently not handled"
                    uls.pop()
                    curr_ul = uls[-1]
            last_heading_level = level
            curr_li = soup.new_tag("li")
            curr_ul.append(curr_li)
            if not heading["id"]:
                raise RuntimeError(f"<{heading.name}> heading '{heading.get_text()}' has no ID")
            a = soup.new_tag("a", href="#" + heading["id"])
            a.string = heading.get_text()
            curr_li.append(a)


@contextmanager
def add_to_page(page: PageObject, unit="mm"):
    k = get_scale_factor(unit)
    format = (page.mediabox[2] / k, page.mediabox[3] / k)
    pdf = FPDF(format=format, unit=unit)
    pdf.add_page()
    yield pdf
    overlay_pdf = io.BytesIO(pdf.output())
    overlay_page = PdfReader(overlay_pdf).pages[0]
    page.merge_page(page2=overlay_page)

@contextmanager
def add_to_every_page_static(pdf_filepath, unit="mm", viewer_prefs=None):
    "Add the same content on every page"
    reader = PdfReader(pdf_filepath)
    k = get_scale_factor(unit)
    format = (reader.pages[0].mediabox[2] / k, reader.pages[0].mediabox[3] / k)
    writer = PdfWriter()
    writer.append(reader)
    pdf = FPDF(format=format, unit=unit)
    pdf.add_page()
    yield pdf
    overlay_pdf = io.BytesIO(pdf.output())
    overlay_page = PdfReader(overlay_pdf).pages[0]
    for page in writer.pages:
        page.merge_page(page2=overlay_page)
    if viewer_prefs:
        writer.create_viewer_preferences()
        for key, value in viewer_prefs.items():
            setattr(writer.viewer_preferences, key, value)
    writer.write(pdf_filepath)

def add_to_every_page_dynamic(pdf_filepath, unit="mm", viewer_prefs=None):
    "Add some variable content on every page"
    k = get_scale_factor(unit)
    writer = PdfWriter()
    writer.append(PdfReader(pdf_filepath))
    for page in writer.pages:
        format = (page.mediabox[2] / k, page.mediabox[3] / k)
        pdf = FPDF(format=format, unit=unit)
        pdf.add_page()
        yield pdf
        overlay_pdf = io.BytesIO(pdf.output())
        overlay_page = PdfReader(overlay_pdf).pages[0]
        page.merge_page(page2=overlay_page)
    if viewer_prefs:
        writer.create_viewer_preferences()
        for key, value in viewer_prefs.items():
            setattr(writer.viewer_preferences, key, value)
    writer.write(pdf_filepath)


def set_metadata(filepath, title=None, description=None, keywords=(), lang=None):
    """
    This is preferable over passing metadata= to markdown2pdf() because pikepdf also sets metadata as XMP
    """
    if not (title or description or keywords or lang):
        return
    with pikepdf.open(filepath, allow_overwriting_input=True) as pdf:
        with pdf.open_metadata(set_pikepdf_as_editor=False) as meta:
            meta["dc:creator"] = [AUTHOR]
            meta["pdf:Producer"] = "WeasyPrint & pikepdf"
            meta["xmp:CreateDate"] = datetime.now(datetime.utcnow().astimezone().tzinfo).isoformat()
            meta["xmp:CreatorTool"] = f"github.com/Lucas-C/jdr:fpdf{FPDF_VERSION}:pikepdf{pikepdf.__version__}:weasyprint{WP_VERSION}"
            if title:
                meta["dc:title"] = title
            if lang:
                meta["dc:language"] = lang
            if description:
                meta["dc:description"] = description
            if keywords:
                if any(" " in word for word in keywords):
                    raise ValueError(f"PDF keywords should not contain any whitespace: '{keywords}'")
                meta["dc:subject"] = " ".join(keywords)
                meta["pdf:Keywords"] = " ".join(keywords)
        pdf.save()


def add_pdf_annotations(pdf_filepath, annotations, viewer_prefs=None, font="Helvetica", size=12):
    """
    Args:
        pdf_filepath (str): path to the PDF document
        annotations (dict): map page indices (starting at 0) to dictionaries,
            with valid keys being "text_annotations" / "ink_annotations" / etc.,
            and values being the parameters passed to the corresponding FPDF methods.
        viewer_prefs (dict): viewer preferences, with keys as camel_case
    """
    for i, pdf in enumerate(add_to_every_page_dynamic(pdf_filepath, viewer_prefs=viewer_prefs)):
        page_annotations = annotations.get(i)
        if not page_annotations:
            continue
        for annot in page_annotations.get("text_annotations", ()):
            pdf.text_annotation(**annot)
        for annot in page_annotations.get("free_text_annotations", ()):
            pdf.set_font(font, size=size)
            pdf.free_text_annotation(**annot)
        for annot in page_annotations.get("ink_annotations", ()):
            pdf.ink_annotation(**annot)


def add_outline_items(pdf_filepath, outline_items, color=None, italic=False, bold=False):
    writer = PdfWriter()
    writer.append(PdfReader(pdf_filepath))
    for title in outline_items:
        writer.add_outline_item(title, page_number=None, color=color, italic=italic, bold=bold)
    writer.write(pdf_filepath)


async def start_watch_and_rebuild(module, *files_to_watch):
    "Watch files and on change, reload Python modules & call build_pdf()"
    if not OPT_DEPS_LOADED:
        raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
    files_to_watch += (__file__,)
    watcher = get_watcher_class()()
    for filepath in files_to_watch:
        watcher.watch(str(filepath), partial(module.build_pdf, Path(filepath)))
    print("Watcher started...")
    await watch_periodically(module, watcher)


async def watch_periodically(module, watcher, delay_secs=.8):
    try:
        watcher.examine()
    except Exception:
        print_exc()
    await asyncio.sleep(delay_secs)
    xreload(module, new_annotations={"XRELOADED": True})
    await asyncio.create_task(watch_periodically(module, watcher, delay_secs))


def watch_xreload_and_serve(module, root_dir, *files_to_watch):
    """
    * watch files and on change, reload Python modules & call build_pdf()
    * starts a HTTP server
    """
    if not OPT_DEPS_LOADED:
        raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
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
        super().__init__(TripleCommaDiv) #, DefinitionList)

    def render_definition_list(self, token) -> str:
        inner = self.render_inner(token)
        return f'<dl class="{token.classes}">{inner}</dl>'

    def render_triple_comma_div(self, token) -> str:
        inner = self.render_inner(token)
        return f'<div class="{token.classes}">{inner}</div>'

    # Override default implementation.
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


class DefinitionList(BlockToken):
    """
    Simple <dl> block. (["term", ": definition"])

    Inspirational specs:
    * https://www.markdownguide.org/extended-syntax/#definition-lists
    * https://github.com/Python-Markdown/markdown/blob/master/docs/extensions/definition_lists.md
    * https://pandoc.org/MANUAL.html#definition-lists

    I shared this implementation there: https://github.com/miyuchina/mistletoe/issues/229
    """

    @staticmethod
    def start(line):
        raise NotImplementedError

    @classmethod
    def read(cls, lines):
        raise NotImplementedError
        self.children = ...

    def __init__(self, match):
        self.children = match


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
