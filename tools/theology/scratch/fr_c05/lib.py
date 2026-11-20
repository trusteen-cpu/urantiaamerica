# -*- coding: utf-8 -*-
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
T = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"
sys.path.insert(0, os.path.join(T, ".."))
import amq  # noqa

OUT = os.path.join(T, "fr", "c05.json")
QOUT = os.path.join(T, "fr", "quotes_c05.json")


def load(p):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


def cut(ref, *pieces):
    """pieces: (start, end) substrings; piece = verse[start .. end inclusive]."""
    v = amq.text("fr", ref)
    out = []
    pos = 0
    for a, b in pieces:
        i = v.index(a, pos)
        j = v.index(b, i) + len(b)
        out.append(v[i:j].strip())
        pos = j
    s = " … ".join(out)
    assert amq.check("fr", ref, s), (ref, s)
    return s


def save(units, quotes):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    src = json.load(open(os.path.join(T, "work", "src_c05.json"), encoding="utf-8"))
    D = load(OUT)
    D.update(units)
    D = {k: D[k] for k in src if k in D}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    todo = json.load(open(os.path.join(T, "work", "todo_fr_c05.json"), encoding="utf-8"))
    Q = load(QOUT)
    Q.update(quotes)
    Q = {k: Q[k] for k in todo if k in Q}
    json.dump(Q, open(QOUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    miss = [k for k in units if k not in src]
    print("units", len(D), "/", len(src), "quotes", len(Q), "/", len(todo), "bad keys", miss)
