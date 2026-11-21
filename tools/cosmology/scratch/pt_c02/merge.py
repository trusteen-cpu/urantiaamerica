import json, os
BASE = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
SRC = json.load(open(os.path.join(BASE, "work", "src_c02.json"), encoding="utf-8"))
OUT = os.path.join(BASE, "pt", "c02.json")

def merge(part):
    D = {}
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding="utf-8"))
    for k, v in part.items():
        assert k in SRC, k
        if isinstance(SRC[k], list):
            assert isinstance(v, list) and len(v) == len(SRC[k]), k
        else:
            assert isinstance(v, str), k
        D[k] = v
    R = {k: D[k] for k in SRC if k in D}
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(R), "of", len(SRC))
