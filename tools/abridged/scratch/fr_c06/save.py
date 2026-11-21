import json, os
BASE = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged"
SRC = os.path.join(BASE, "work", "src_c06.json")
OUT = os.path.join(BASE, "fr", "c06.json")

def save(F):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in F.items():
        assert k in src, k
        s = src[k]
        assert type(s) == type(v), k
        if isinstance(s, list):
            assert len(s) == len(v), (k, len(s), len(v))
            for a, b in zip(s, v):
                assert len(a) == len(b), (k, a, b)
        cur[k] = v
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(out), "/", len(src))
    papers = sorted({k.split('.')[0] for k in F})
    for p in papers:
        miss = [k for k in src if k.split('.')[0] == p and k not in out]
        if miss: print("missing", p, miss)
