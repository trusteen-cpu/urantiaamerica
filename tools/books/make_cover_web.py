# -*- coding: utf-8 -*-
"""Web front covers of "The Life and Teachings of Jesus" in es / fr / pt.
   Same look as the Korean cover (cream, gold + red double frame, ornament, ch54 art), but with
   the title in each language.  Writes site/books-img/jesus-book/cover_<l>.jpg (700 x 1037).
   usage: python make_cover_web.py"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "..", "site")
BOOK = r"E:\OneDrive\내 문서\유란시아\출판 최종파일\예수의 삶과 가르침"
ART = os.path.join(BOOK, "그림", "ch54.png")
ORN = os.path.join(BOOK, "도구", "orn", "divider_title.png")
FB, FR, FI = r"C:\Windows\Fonts\GARABD.TTF", r"C:\Windows\Fonts\GARA.TTF", r"C:\Windows\Fonts\GARAIT.TTF"

RED, TEAL, GOLD = (122, 31, 43), (62, 102, 112), (176, 138, 74)
CREAM, INK = (248, 242, 228), (70, 58, 50)
S = 2                      # draw at 2x, then downscale
W, H = 700 * S, 1037 * S

T = {
    "es": ("La historia que los evangelios no contaron",
           ["La vida y las", "enseñanzas de Jesús"],
           "La vida de Jesús según la Parte IV de El libro de Urantia", "Jay Han"),
    "fr": ("L’histoire que les Évangiles n’ont pas racontée",
           ["La vie et les", "enseignements de Jésus"],
           "La vie de Jésus selon la quatrième partie du Livre d’Urantia", "Jay Han"),
    "pt": ("A história que os evangelhos não contaram",
           ["A vida e os", "ensinamentos de Jesus"],
           "A vida de Jesus segundo a Parte IV de O Livro de Urântia", "Jay Han"),
}


def font(p, size):
    return ImageFont.truetype(p, int(size * S))


def fit(d, s, path, size, maxw):
    while d.textlength(s, font=font(path, size)) > maxw * S:
        size -= 1
    return font(path, size)


def make(l):
    kick, title, line, author = T[l]
    img = Image.new("RGB", (W, H), CREAM)
    vig = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vig).rectangle((40 * S, 40 * S, W - 40 * S, H - 40 * S), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(50 * S))
    img = Image.composite(img, Image.new("RGB", (W, H), (232, 220, 196)), vig)
    d = ImageDraw.Draw(img)

    # double frame + corner stars
    x0, y0, x1, y1 = 36 * S, 36 * S, W - 36 * S, H - 36 * S
    d.rectangle((x0, y0, x1, y1), outline=GOLD, width=3 * S)
    d.rectangle((x0 + 7 * S, y0 + 7 * S, x1 - 7 * S, y1 - 7 * S), outline=RED, width=1 * S)
    star = ImageFont.truetype(r"C:\Windows\Fonts\seguisym.ttf", 15 * S)
    for cx, cy in ((x0, y0), (x1, y0), (x0, y1), (x1, y1)):
        d.ellipse((cx - 10 * S, cy - 10 * S, cx + 10 * S, cy + 10 * S), fill=CREAM, outline=GOLD, width=2 * S)
        d.text((cx, cy), "✦", font=star, fill=RED, anchor="mm")

    cx = W // 2
    d.text((cx, 112 * S), kick, font=fit(d, kick, FI, 24, 540), fill=TEAL, anchor="mm")
    tf = min(fit(d, t, FB, 54, 560).size for t in title)
    tf = ImageFont.truetype(FB, tf)
    y = 168 * S
    for t in title:
        d.text((cx, y), t, font=tf, fill=RED, anchor="mm")
        y += int(tf.size * 1.12)

    o = Image.open(ORN).convert("RGBA")
    ow = 300 * S
    o = o.resize((ow, round(o.height * ow / o.width)), Image.LANCZOS)
    oy = y - int(tf.size * 0.35)
    img.paste(o, (cx - ow // 2, oy), o)

    # art with the white paper made transparent
    art = Image.open(ART).convert("RGB")
    aw = 580 * S
    art = art.resize((aw, round(art.height * aw / art.width)), Image.LANCZOS)
    a = np.asarray(art).astype(np.int16)
    white = (a.min(axis=2) > 238) & ((a.max(axis=2) - a.min(axis=2)) < 14)
    m = Image.fromarray(np.where(white, 0, 255).astype("uint8")).filter(ImageFilter.GaussianBlur(1.5 * S))
    ay = oy + o.height + 14 * S
    maxh = 700 * S - ay + 300 * S
    if art.height > maxh:
        art = art.resize((round(art.width * maxh / art.height), maxh), Image.LANCZOS)
        m = m.resize(art.size, Image.LANCZOS)
    img.paste(art, (cx - art.width // 2, ay), m)
    d = ImageDraw.Draw(img)

    ly = ay + art.height + 34 * S
    d.text((cx, ly), line, font=fit(d, line, FI, 21, 560), fill=INK, anchor="mm")
    d.text((cx, H - 118 * S), author, font=font(FB, 30), fill=RED, anchor="mm")

    out = img.resize((700, 1037), Image.LANCZOS)
    p = os.path.join(SITE, "books-img", "jesus-book", f"cover_{l}.jpg")
    out.save(p, quality=90)
    print(p)


for l in T:
    make(l)
