# -*- coding: utf-8 -*-
# usage: python save.py t_ch01.py   (module defining dict T)
import json, os, sys, runpy
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"
SRC = json.load(open(os.path.join(H, "work", "src_c01.json"), encoding="utf-8"))
OUT = os.path.join(H, "pt", "c01.json")
D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
for f in sys.argv[1:]:
    T = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), f))["T"]
    for k, v in T.items():
        assert k in SRC, k
        D[k] = v.strip()
D = {k: D[k] for k in SRC if k in D}
missing = [k for k in SRC if k not in D]
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(D), "missing", len(missing), missing[:5])
