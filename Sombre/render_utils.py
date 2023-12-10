LINE_HEIGHT = 5.25
TILE_SIZE = 60


def iter_tile_pos(pdf, columns=4, rows=3):
    for j in range(rows):
        for i in range(columns):
            pdf.x = pdf.l_margin + i * TILE_SIZE
            pdf.y = pdf.t_margin + j * TILE_SIZE
            yield pdf, pdf.x, pdf.y


def render_img_tile(tpi, img, name="", desc="", border=False, w_ratio=1, h_ratio=1):
    pdf, x, y = next(tpi)
    img_dx = TILE_SIZE * (1 - w_ratio) / 2
    img_dy = TILE_SIZE * (1 - h_ratio) / 2
    pdf.image(img, x=x + img_dx, y=y + img_dy, w=TILE_SIZE * w_ratio, h=TILE_SIZE, keep_aspect_ratio=True)
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
