import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(BASE, "fr", "c17.json")
SRC = os.path.join(BASE, "work", "src_c17.json")

def save(D):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    for k, v in D.items():
        assert k in src, k
        assert type(v) == type(src[k]), k
        if isinstance(v, list):
            assert len(v) == len(src[k]), k
            for a, b in zip(v, src[k]):
                assert len(a) == len(b), (k, a)
        cur[k] = v
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(out), "/", len(src))
