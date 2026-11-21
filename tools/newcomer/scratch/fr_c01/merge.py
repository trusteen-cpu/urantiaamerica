# -*- coding: utf-8 -*-
# usage: python merge.py p1  -> merges D from pN.py into fr/c01.json (source order)
import json, os, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
SRC = json.load(open(os.path.join(H, "work", "src_c01.json"), encoding="utf-8"))
OUT = os.path.join(H, "fr", "c01.json")
cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
for name in sys.argv[1:]:
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), name + ".py")
    spec = importlib.util.spec_from_file_location(name, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.D.items():
        assert k in SRC, ("extra", k)
        ev = SRC[k]
        if isinstance(ev, list): assert isinstance(v, list) and len(v) == len(ev), ("len", k)
        if isinstance(ev, dict): assert isinstance(v, dict) and set(v) == set(ev), ("dict", k)
        if isinstance(ev, str): assert isinstance(v, str) and "\n" not in v, ("str", k)
        cur[k] = v
out = {k: cur[k] for k in SRC if k in cur}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
missing = [k for k in SRC if k not in out]
print("have", len(out), "of", len(SRC), "; first missing:", missing[:3])
