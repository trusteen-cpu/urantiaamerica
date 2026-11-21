# -*- coding: utf-8 -*-
import json, os, sys
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
sys.path.insert(0, os.path.join(B, ".."))
SRC = json.load(open(os.path.join(B, "work", "src_c01.json"), encoding="utf-8"))
OUT = os.path.join(B, "pt", "c01.json")

def merge(T):
    import pt_old_spelling as P
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in T.items():
        assert k in SRC, k
        cur[k] = v
    def fx(x):
        if isinstance(x, str): return P.fix(x)
        if isinstance(x, list): return [fx(y) for y in x]
        if isinstance(x, dict): return {a: fx(b) for a, b in x.items()}
        return x
    D = {k: fx(cur[k]) for k in SRC if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("units", len(D), "/", len(SRC))
