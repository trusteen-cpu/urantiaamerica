import json, os, sys, importlib
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
src = json.load(open(os.path.join(ROOT, "work", "src_c01.json"), encoding="utf-8"))
out = os.path.join(ROOT, "es", "c01.json")
cur = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
for p in ["p1", "p2", "p3", "p4"]:
    if os.path.exists(os.path.join(HERE, p + ".py")):
        cur.update(importlib.import_module(p).D)
extra = [k for k in cur if k not in src]
if extra: print("EXTRA", extra)
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", len(D), "of", len(src), "missing", [k for k in src if k not in D][:5])
