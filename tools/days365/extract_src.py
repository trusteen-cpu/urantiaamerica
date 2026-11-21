# -*- coding: utf-8 -*-
# 365 Days with The Urantia Book (days365) — es/fr/pt: English translation units
#   Units come from the Far East Chinese port (tools/zh/days365/src/c01..c07.json, English, with ⟦Q cit⟧…⟦/Q⟧ markers
#   around verbatim Urantia Book quotations). Read only; nothing in the Far East folder is changed.
#   Re-chunked here to ~14,000 English words per chunk (keys dNNN kept). UI strings are "ui.*" keys in c01.
#   Writes src/c01..cNN.json.  Re-run: python extract_src.py   (do not re-run once translation has started)
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
ZSRC = os.path.join(FE, "tools", "zh", "days365", "src")
SRC = os.path.join(H, "src"); os.makedirs(SRC, exist_ok=True)

UI = {
    "ui.page_title": "365 Days with The Urantia Book",
    "ui.meta_description": "One passage of The Urantia Book for every day of the year, with a meditation and a practice for the day.",
    "ui.og_description": "One passage a day, a year-long spiritual journey.",
    "ui.subtitle": "One passage a day, a year-long spiritual journey",
    "ui.aria_choose_day": "Choose a day",
    "ui.prev": "‹ Prev",
    "ui.aria_prev": "Previous day",
    "ui.next": "Next ›",
    "ui.aria_next": "Next day",
    "ui.aria_month": "Month",
    "ui.aria_day": "Day",
    "ui.today_button": "Today",
    "ui.loading": "Loading…",
    "ui.toc_summary": "All 365 days",
    "ui.about_html": "The quotations are reproduced word for word from the official translation of <i>The Urantia Book</i> published by Urantia Foundation. The meditations are commentary on each passage and are not part of <i>The Urantia Book</i> itself.",
    "ui.day_label": "DAY {n}",
    "ui.open_in_book": "Open in The Urantia Book",
    "ui.cite_prefix": "— The Urantia Book",
    "ui.practice_label": "Today",
    "ui.load_error": "The daily pages could not be loaded. Please reload the page.",
    "ui.paper_label": "Paper {n}",
}

U = {}
for f in sorted(glob.glob(os.path.join(ZSRC, "c0[1-7].json"))):
    U.update(json.load(open(f, encoding="utf-8")))
assert len(U) == 365 and list(U) == ["d%03d" % i for i in range(1, 366)], "zh source incomplete"

strip = lambda s: re.sub(r"⟦/?Q[^⟧]*⟧", "", s)
words = lambda u: len((strip(u["t"]) + " " + " ".join(map(strip, u["msg"])) + " " + strip(u["pr"])).split())
total = sum(words(u) for u in U.values())
N = 15; target = total / N
chunks, cur, acc = [], [], 0
for k, u in U.items():
    cur.append(k); acc += words(u)
    if acc >= target * (len(chunks) + 1) and len(chunks) < N - 1:
        chunks.append(cur); cur = []
if cur: chunks.append(cur)

for f in glob.glob(os.path.join(SRC, "c[0-9][0-9].json")): os.remove(f)
for i, ks in enumerate(chunks, 1):
    D = dict(UI) if i == 1 else {}
    D.update({k: U[k] for k in ks})
    json.dump(D, open(os.path.join(SRC, "c%02d.json" % i), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    nq = sum(json.dumps(U[k], ensure_ascii=False).count("⟦Q ") for k in ks)
    print("c%02d" % i, ks[0], "-", ks[-1], sum(words(U[k]) for k in ks), "words,", nq, "inline quotations", "(+ UI)" if i == 1 else "")
print("total words", total)
