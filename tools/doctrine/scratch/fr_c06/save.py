# -*- coding: utf-8 -*-
import json, os
H = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(H, "fr", "c06.json")
SRC = os.path.join(H, "work", "src_c06.json")


def save(U):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(U)
    for k in U:
        if k not in src: raise SystemExit("unknown key " + k)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))
