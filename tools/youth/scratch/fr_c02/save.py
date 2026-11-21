import json, os, sys, importlib.util
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work", "src_c02.json")
OUT = os.path.join(BASE, "fr", "c02.json")
src = json.load(open(SRC, encoding="utf-8"))
cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
for f in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location("m", f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.P.items():
        assert k in src, k
        cur[k] = v
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("units", len(D), "/", len(src), "missing:", [k for k in src if k not in D][:5])
