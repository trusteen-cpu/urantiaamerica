import json, os, sys, importlib
SRC = "work/src_c02.json"
OUT = "es/c02.json"
src = json.load(open(SRC, encoding="utf-8"))
D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
for name in sys.argv[1:]:
    m = importlib.import_module(name)
    for k, v in m.T.items():
        assert k in src, k
        D[k] = v
missing_in_mod = []
out = {k: D[k] for k in src if k in D}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(out), "of", len(src))
