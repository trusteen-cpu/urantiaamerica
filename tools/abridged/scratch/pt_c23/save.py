import json, os
BASE = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged"
OUT = BASE + r"\pt\c23.json"
SRC = json.load(open(BASE + r"\work\src_c23.json", encoding="utf-8"))


def save(T):
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in T:
        assert k in SRC, k
        s = SRC[k]
        assert type(s) == type(T[k]), k
        if isinstance(s, list):
            assert len(s) == len(T[k]) and all(len(a) == len(b) for a, b in zip(s, T[k])), k
    D.update(T)
    D = {k: D[k] for k in SRC if k in D}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(D), "of", len(SRC))
