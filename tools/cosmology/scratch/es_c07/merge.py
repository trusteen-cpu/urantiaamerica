# -*- coding: utf-8 -*-
import json, os, sys, importlib.util
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
S = os.path.join(H, "scratch", "es_c07")
src = json.load(open(os.path.join(H, "work", "src_c07.json"), encoding="utf-8"))
T = {}
for p in ("p1", "p2", "p3", "p4"):
    f = os.path.join(S, p + ".py")
    if os.path.exists(f):
        spec = importlib.util.spec_from_file_location(p, f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        T.update(m.T)
extra = set(T) - set(src)
assert not extra, extra
D = {}
for k, v in src.items():
    if k in T:
        t = T[k]
        if isinstance(v, list):
            assert isinstance(t, list) and len(t) == len(v), k
        else:
            assert isinstance(t, str), k
        D[k] = t
json.dump(D, open(os.path.join(H, "es", "c07.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", len(D), "of", len(src), "missing", [k for k in src if k not in D][:5])
