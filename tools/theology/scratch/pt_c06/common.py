# -*- coding: utf-8 -*-
import json, os, sys
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa

SRC = os.path.join(H, "work", "src_c06.json")
OUT = os.path.join(H, "pt", "c06.json")
QOUT = os.path.join(H, "pt", "quotes_c06.json")
TODO = os.path.join(H, "work", "todo_pt_c06.json")


def save_units(T):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in src if k.split(".")[0] == list(T)[0].split(".")[0] and k not in T]
    print("saved", len(D), "of", len(src), "missing in this chapter:", missing)


def cut(cit, pieces):
    """pieces: list of (start, end) snippets; returns verbatim pieces joined by ' … '."""
    v = amq.text("pt", cit)
    out, pos = [], 0
    for a, b in pieces:
        i = v.index(a, pos)
        j = v.index(b, i) + len(b)
        out.append(v[i:j])
        pos = j
    return " … ".join(out)


def save_quotes(Q):
    todo = json.load(open(TODO, encoding="utf-8"))
    cur = json.load(open(QOUT, encoding="utf-8")) if os.path.exists(QOUT) else {}
    for k, (cit, pieces) in Q.items():
        assert k in todo and todo[k]["cit"] == cit, k
        s = cut(cit, pieces)
        assert amq.check("pt", cit, s)
        cur[k] = s
    D = {k: cur[k] for k in todo if k in cur}
    json.dump(D, open(QOUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("quotes saved", len(D), "of", len(todo))
