# -*- coding: utf-8 -*-
import json, os, importlib, sys
H = os.path.dirname(os.path.abspath(__file__))
Q = os.path.normpath(os.path.join(H, "..", ".."))
SRC = os.path.join(Q, "work_fr", "src_c02.json")
OUT = os.path.join(Q, "fr", "c02.json")
os.makedirs(os.path.dirname(OUT), exist_ok=True)

def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "of", len(src))

if __name__ == "__main__":
    sys.path.insert(0, H)
    for m in sys.argv[1:]:
        save(importlib.import_module(m).U)
