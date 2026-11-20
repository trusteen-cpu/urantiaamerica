# -*- coding: utf-8 -*-
import json, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(H, "es", "c01.json")
SRC = os.path.join(H, "work", "src_c01.json")

def save(new):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(new)
    bad = [k for k in new if k not in src]
    if bad: print("UNKNOWN KEYS", bad)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src), "missing:", [k for k in src if k not in D][:5])
