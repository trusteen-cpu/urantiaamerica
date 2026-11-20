# -*- coding: utf-8 -*-
import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"
SRC = os.path.join(H, "work", "src_c06.json")
OUT = os.path.join(H, "fr", "c06.json")
QOUT = os.path.join(H, "fr", "quotes_c06.json")
FR = json.load(open(os.path.join(H, "..", "data", "fr.json"), encoding="utf-8"))


def _load(p):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


def save_units(T):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = _load(OUT)
    for k in T:
        assert k in src, k
    cur.update(T)
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("units", len(out), "/", len(src))


def cut(ref, start, end=None):
    v = FR[ref]
    i = v.index(start)
    if end is None:
        return v[i:]
    j = v.index(end, i) + len(end)
    return v[i:j]


def save_quotes(Q):
    cur = _load(QOUT)
    cur.update(Q)
    todo = json.load(open(os.path.join(H, "work", "todo_fr_c06.json"), encoding="utf-8"))
    out = {k: cur[k] for k in todo if k in cur}
    json.dump(out, open(QOUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("quotes", len(out), "/", len(todo))
