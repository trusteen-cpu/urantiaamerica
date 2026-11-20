# -*- coding: utf-8 -*-
import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\qna"
OUT = os.path.join(H, "es", "c01.json")
SRC = json.load(open(os.path.join(H, "work_es", "src_c01.json"), encoding="utf-8"))
ES = json.load(open(os.path.join(H, "..", "data", "es.json"), encoding="utf-8"))


def V(k):
    """verse number + official Spanish verse text"""
    return k + " " + ES[k]


def W(k, inner, prefix=True):
    """official verse with a ⟦Q⟧ marker around `inner` (must occur verbatim)"""
    t = ES[k]
    assert inner in t, (k, inner)
    t = t.replace(inner, "⟦Q %s⟧%s⟦/Q⟧" % (k, inner), 1)
    return (k + " " + t) if prefix else t


def P(*paras):
    return "\n\n".join(paras)


def save(units):
    D = {}
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding="utf-8"))
    D.update(units)
    R = {k: D[k] for k in SRC if k in D}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(R), "/", len(SRC))
