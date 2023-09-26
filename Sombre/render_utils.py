import asyncio, logging, sys
from traceback import print_exc

try:
    from livereload.watcher import get_watcher_class
    from xreload import xreload
    OPT_DEPS_LOADED = True
except ImportError:
    OPT_DEPS_LOADED = False

LINE_HEIGHT = 5.25
TILE_SIZE = 60


def iter_tile_pos(pdf, columns=4, rows=3):
    for j in range(rows):
        for i in range(columns):
            pdf.x = pdf.l_margin + i * TILE_SIZE
            pdf.y = pdf.t_margin + j * TILE_SIZE
            yield pdf, pdf.x, pdf.y


def render_img_tile(tpi, img, name="", desc="", border=False):
    pdf, x, y = next(tpi)
    pdf.image(img, w=TILE_SIZE, h=TILE_SIZE, keep_aspect_ratio=True)
    if border:
        pdf.rect(x, y , w=TILE_SIZE, h=TILE_SIZE)
    if name or desc:
        if name:
            pdf.x = x + .5 * TILE_SIZE
            pdf.y = y + .25 * TILE_SIZE
            pdf.set_font(size=20, style="B")
            pdf.cell(txt=name, h=LINE_HEIGHT, align="X")
        if desc:
            pdf.x = x + .5 * TILE_SIZE
            pdf.y = y + .7 * TILE_SIZE
            pdf.set_font(size=13, style="I")
            pdf.cell(txt=desc, h=LINE_HEIGHT, align="X")


async def start_watch_and_rebuild(module, mod_filepath):
    if not OPT_DEPS_LOADED:
        raise EnvironmentError("Missing optional dependencies livereload and/or xreload")
    logging.basicConfig(format="%(asctime)s %(name)s [%(levelname)s] %(message)s",
                        datefmt="%H:%M:%S", level=logging.INFO)
    logging.getLogger("livereload").setLevel(logging.INFO)
    watcher = get_watcher_class()()
    watcher.watch(__file__, module.build_pdf)
    watcher.watch(mod_filepath, module.build_pdf)
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
