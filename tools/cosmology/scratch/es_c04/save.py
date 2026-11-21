# -*- coding: utf-8 -*-
import json, os
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC = json.load(open(os.path.join(H, "work", "src_c04.json"), encoding="utf-8"))
OUT = os.path.join(H, "es", "c04.json")


def save(new):
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in new:
        if k not in SRC:
            raise SystemExit("unknown key " + k)
    cur.update(new)
    D = {k: cur[k] for k in SRC if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(SRC))
