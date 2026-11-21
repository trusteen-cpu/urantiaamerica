# -*- coding: utf-8 -*-
import json, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.abspath(os.path.join(HERE, "..", ".."))
src = json.load(open(os.path.join(AB, "work", "src_c10.json"), encoding="utf-8"))
out_p = os.path.join(AB, "pt", "c10.json")
D = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {}
for name in sorted(os.listdir(HERE)):
    if name.startswith("part_") and name.endswith(".py"):
        spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(HERE, name))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        D.update(m.D)
bad = [k for k in D if k not in src]
if bad: print("UNKNOWN KEYS", bad)
for k, v in D.items():
    if k in src and type(v) != type(src[k]): print("TYPE", k)
    if k in src and isinstance(v, list):
        if len(v) != len(src[k]) or any(len(a) != len(b) for a, b in zip(v, src[k])): print("SHAPE", k)
O = {k: D[k] for k in src if k in D}
json.dump(O, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(O), "/", len(src), "missing", [k for k in src if k not in D][:5])
