import json, os, sys, importlib
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
SRC = json.load(open(os.path.join(H, "work", "src_c03.json"), encoding="utf-8"))
OUT = os.path.join(H, "es", "c03.json")
D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
for name in sys.argv[1:]:
    T = importlib.import_module(name).T
    for k, v in T.items():
        assert k in SRC, k
        assert type(v) is type(SRC[k]), k
        if isinstance(v, list): assert len(v) == len(SRC[k]), k
        D[k] = v
D = {k: D[k] for k in SRC if k in D}
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(D), "/", len(SRC), "missing:", [k for k in SRC if k not in D][:10])
