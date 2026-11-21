import json, os, sys, importlib
BASE = os.path.join(os.path.dirname(__file__), "..", "..")
src = json.load(open(os.path.join(BASE, "work", "src_c08.json"), encoding="utf-8"))
out_p = os.path.join(BASE, "fr", "c08.json")
T = {}
for part in sys.argv[1:]:
    T.update(importlib.import_module(part).T)
old = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {}
old.update(T)
D = {k: old[k] for k in src if k in old}
for k in D:
    if isinstance(src[k], list):
        assert isinstance(D[k], list) and len(D[k]) == len(src[k]), k
json.dump(D, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(D), "/", len(src), "missing:", [k for k in src if k not in D][:10])
