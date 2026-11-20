# -*- coding: utf-8 -*-
import json, os
D = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine"
SRC = os.path.join(D, "work", "src_c05.json")
OUT = os.path.join(D, "fr", "c05.json")


def save(T):
    S = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in T:
        if k not in S:
            raise KeyError("unknown key " + k)
    cur.update(T)
    out = {k: cur[k] for k in S if k in cur}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(T), "units; total", len(out), "/", len(S))
