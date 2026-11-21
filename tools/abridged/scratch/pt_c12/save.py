import json, os, sys, importlib
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
src = json.load(open(os.path.join(AB, "work", "src_c12.json"), encoding="utf-8"))
out_p = os.path.join(AB, "pt", "c12.json")
D = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {}
for mod in sys.argv[1:]:
    m = importlib.import_module(mod)
    for k, v in m.T.items():
        assert k in src, ("unknown key", k)
        s = src[k]
        assert type(s) == type(v), ("type", k)
        if isinstance(s, list):
            assert len(s) == len(v), ("rows", k)
            for a, b in zip(s, v):
                assert len(a) == len(b), ("cells", k, a, b)
        D[k] = v
O = {k: D[k] for k in src if k in D}
json.dump(O, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(O), "of", len(src))
missing = [k for k in src if k not in O]
print("missing", len(missing), missing[:5])
