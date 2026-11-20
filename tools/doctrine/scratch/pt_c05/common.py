# -*- coding: utf-8 -*-
import json, os
D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(D, "..", ".."))
SRC = os.path.join(ROOT, "work", "src_c05.json")
OUT = os.path.join(ROOT, "pt", "c05.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in units:
        assert k in src, k
    cur.update(units)
    out = {k: cur[k] for k in src if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(out), "of", len(src))
