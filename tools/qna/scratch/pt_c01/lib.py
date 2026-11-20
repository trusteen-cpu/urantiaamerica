# -*- coding: utf-8 -*-
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
QNA = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(QNA))
import amq

OUT = os.path.join(QNA, "pt", "c01.json")
SRC = os.path.join(QNA, "work_pt", "src_c01.json")


def V(r):
    return amq.text("pt", r)


def VQ(r, *subs):
    t = V(r)
    for s in subs:
        assert s in t, (r, s)
        t = t.replace(s, "⟦Q %s⟧%s⟦/Q⟧" % (r, s), 1)
    return t


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    out = {k: cur[k] for k in src if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(out), "of", len(src))
