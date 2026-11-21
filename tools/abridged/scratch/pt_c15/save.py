import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(BASE, "pt", "c15.json")
SRC = os.path.join(BASE, "work", "src_c15.json")
def add(D):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in D.items():
        assert k in src, k
        s = src[k]
        assert type(s) == type(v), k
        if isinstance(s, list):
            assert len(s) == len(v), k
            for a, b in zip(s, v): assert len(a) == len(b), (k, a, b)
        cur[k] = v
    res = {k: cur[k] for k in src if k in cur}
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in res]
    print("saved", len(res), "/", len(src), "missing", len(missing), missing[:3])
