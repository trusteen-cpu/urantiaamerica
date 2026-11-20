# -*- coding: utf-8 -*-
import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine"
SRC = os.path.join(H, "work", "src_c04.json")
OUT = os.path.join(H, "fr", "c04.json")


def save(T):
    S = json.load(open(SRC, encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in T:
        if k not in S:
            raise SystemExit("unknown key " + k)
        e, f = S[k], T[k]
        if isinstance(e, dict):
            if "rows" in e:
                assert len(e["rows"]) == len(f["rows"]), k
                for a, b in zip(e["rows"], f["rows"]):
                    assert len(a) == len(b), (k, a)
            if "items" in e:
                assert len(e["items"]) == len(f["items"]), k
    D.update(T)
    R = {k: D[k] for k in S if k in D}
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(R), "of", len(S))
