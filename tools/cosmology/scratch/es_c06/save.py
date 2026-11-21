import json, os, sys, importlib
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
SRC = json.load(open(os.path.join(H, "work", "src_c06.json"), encoding="utf-8"))
OUT = os.path.join(H, "es", "c06.json")
T = {}
for part in sys.argv[1:]:
    T.update(importlib.import_module(part).D)
old = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
old.update(T)
bad = [k for k in old if k not in SRC]
if bad: print("EXTRA", bad)
D = {k: old[k] for k in SRC if k in old}
for k in D:
    if isinstance(SRC[k], list) and (not isinstance(D[k], list) or len(D[k]) != len(SRC[k])): print("CELLS", k)
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(D), "/", len(SRC), "missing:", [k for k in SRC if k not in D][:10])
