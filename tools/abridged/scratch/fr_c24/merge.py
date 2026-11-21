import json, os, sys, importlib.util
base = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged"
here = os.path.dirname(os.path.abspath(__file__))
src = json.load(open(base + r"\work\src_c24.json", encoding="utf-8"))
out_path = base + r"\fr\c24.json"
cur = json.load(open(out_path, encoding="utf-8")) if os.path.exists(out_path) else {}
for p in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location("m" + p, os.path.join(here, "p%s.py" % p))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.D.items():
        assert k in src, ("unknown key", k)
        s = src[k]
        assert type(s) == type(v), ("type", k)
        if isinstance(s, list):
            assert len(s) == len(v) and all(len(a) == len(b) for a, b in zip(s, v)), ("shape", k)
        s_q = json.dumps(s, ensure_ascii=False).count("⟦Q"); v_q = json.dumps(v, ensure_ascii=False).count("⟦Q")
        assert s_q == v_q, ("markers", k)
        cur[k] = v
    missing = [k for k in src if k.split(".")[0] == p and k not in m.D]
    if missing: print("missing in", p, missing)
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(D), "of", len(src))
