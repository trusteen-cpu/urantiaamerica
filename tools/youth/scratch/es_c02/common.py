# -*- coding: utf-8 -*-
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
YOUTH = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(YOUTH, "work", "src_c02.json")
OUT = os.path.join(YOUTH, "es", "c02.json")


def merge(new):
    src = json.load(open(SRC, encoding="utf-8"))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in new:
        assert k in src, k
    cur.update(new)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))
