import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
OUT = os.path.join(H, "fr", "c01.json")
SRC = json.load(open(os.path.join(H, "work", "src_c01.json"), encoding="utf-8"))


def save(new):
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    D.update(new)
    bad = [k for k in D if k not in SRC]
    assert not bad, bad
    D = {k: D[k] for k in SRC if k in D}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(SRC))
