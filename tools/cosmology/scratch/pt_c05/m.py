# -*- coding: utf-8 -*-
import json, os, sys, importlib
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC = json.load(open(os.path.join(H, "work", "src_c05.json"), encoding="utf-8"))
OUT = os.path.join(H, "pt", "c05.json")
cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
for p in sys.argv[1:]:
    mod = importlib.import_module(p)
    for k, v in mod.D.items():
        if k not in SRC: print("unknown key", k); continue
        cur[k] = v
D = {k: cur[k] for k in SRC if k in cur}
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(D), "/", len(SRC), "missing:", [k for k in SRC if k not in D][:10])
