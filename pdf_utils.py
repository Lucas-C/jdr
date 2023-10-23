import asyncio, io, logging
from traceback import print_exc

try:
    from livereload.watcher import get_watcher_class
    from mistletoe import markdown
    from weasyprint import HTML, CSS
    from weasyprint.text.fonts import FontConfiguration
    from xreload import xreload
    OPT_DEPS_LOADED = True
except ImportError:
    OPT_DEPS_LOADED = False


def markdown2pdf(dir, md_filepath, css_filepath):
    with open(md_filepath, encoding="utf8") as md_file:
        html = markdown(md_file.read())
    html_doc = f"""<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Lab Escape - Scénario pour le JdR Sombre</title>
        <link rel="stylesheet" href="{css_filepath.name}">
    </head>
    <body>{html}</body>
</html>
    """
    with open(dir / "index.html", "w", encoding="utf8") as html_file:
        html_file.write(html_doc)
    font_config = FontConfiguration()
    css = CSS(filename=css_filepath, font_config=font_config)
    bytes_io = io.BytesIO()
    HTML(base_url=str(dir), string=html).write_pdf(bytes_io, stylesheets=[css], font_config=font_config)
    return bytes_io


async def start_watch_and_rebuild(module, *files_to_watch):
    if not OPT_DEPS_LOADED:
        raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
    logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.getLogger("livereload").setLevel(logging.INFO)
    watcher = get_watcher_class()()
    watcher.watch(__file__, module.build_pdf)
    for filepath in files_to_watch:
        watcher.watch(filepath, module.build_pdf)
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
