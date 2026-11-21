import json, os
BASE = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
SRC = os.path.join(BASE, "work", "src_c03.json")
OUT = os.path.join(BASE, "pt", "c03.json")
QOUT = os.path.join(BASE, "pt", "quotes_c03.json")


def save(T):
    src = json.load(open(SRC, encoding="utf-8"))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in T:
        if k not in src:
            raise SystemExit("unknown key " + k)
        sv, tv = src[k], T[k]
        if isinstance(sv, list) and (not isinstance(tv, list) or len(tv) != len(sv)):
            raise SystemExit("bad list " + k)
        if isinstance(sv, dict) and not isinstance(tv, dict):
            raise SystemExit("bad dict " + k)
        if isinstance(sv, str) and not isinstance(tv, str):
            raise SystemExit("bad str " + k)
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))
