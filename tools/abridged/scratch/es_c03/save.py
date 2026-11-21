import json, os
BASE = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged"
SRC = os.path.join(BASE, "work", "src_c03.json")
OUT = os.path.join(BASE, "es", "c03.json")


def save(U):
    src = json.load(open(SRC, encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in U:
        assert k in src, k
        assert type(U[k]) == type(src[k]), k
        if isinstance(src[k], list):
            assert len(U[k]) == len(src[k]), k
            for a, b in zip(U[k], src[k]):
                assert len(a) == len(b), (k, a)
    D.update(U)
    D = {k: D[k] for k in src if k in D}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print("saved", len(D), "of", len(src), "missing", len(missing), missing[:3])
