# -*- coding: utf-8 -*-
import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.normpath(os.path.join(H, "..", ".."))
SRC = json.load(open(os.path.join(D, "work", "src_c01.json"), encoding="utf-8"))
OUT = os.path.join(D, "fr", "c01.json")


def save(units):
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in units:
        assert k in SRC, k
    cur.update(units)
    ordered = {k: cur[k] for k in SRC if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(ordered, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in SRC if k not in ordered]
    print("saved", len(ordered), "missing", len(missing), missing[:8])
