# -*- coding: utf-8 -*-
import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"
SRC = json.load(open(os.path.join(H, "work", "src_c01.json"), encoding="utf-8"))


def _upd(path, new, order):
    D = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    D.update(new)
    if order is not None:
        D = {k: D[k] for k in order if k in D}
    os.makedirs(os.path.dirname(path), exist_ok=True)
    json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    return D


def save(T):
    bad = [k for k in T if k not in SRC]
    assert not bad, bad
    D = _upd(os.path.join(H, "fr", "c01.json"), T, list(SRC))
    print("c01 units:", len(D), "/", len(SRC))


def saveq(Q):
    D = _upd(os.path.join(H, "fr", "quotes_c01.json"), Q, None)
    print("quotes:", len(D))
