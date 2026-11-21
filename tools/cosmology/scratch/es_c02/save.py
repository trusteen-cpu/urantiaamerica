import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
OUT = os.path.join(H, "es", "c02.json")


def save(P):
    src = json.load(open(os.path.join(H, "work", "src_c02.json"), encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in P:
        assert k in src, k
        assert type(P[k]) is type(src[k]), k
        if isinstance(src[k], list): assert len(P[k]) == len(src[k]), k
    D.update(P)
    D = {k: D[k] for k in src if k in D}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src), "missing:", [k for k in src if k not in D][:10])
