# -*- coding: utf-8 -*-
import json, os
H = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(H, "..", "..", "work", "src_c02.json")
OUT = os.path.join(H, "..", "..", "es", "c02.json")


def save(T):
    S = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in T:
        if k not in S:
            raise SystemExit("unknown key " + k)
        v, e = T[k], S[k]
        if isinstance(e, dict) and "rows" in e:
            assert len(v["rows"]) == len(e["rows"]), k
            for a, b in zip(v["rows"], e["rows"]):
                assert len(a) == len(b), (k, a)
        if isinstance(e, dict) and "items" in e:
            assert len(v["items"]) == len(e["items"]), k
    cur.update(T)
    D = {k: cur[k] for k in S if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(T), "total", len(D), "of", len(S))


def _refcell(c):
    import re
    if re.fullmatch(r"[\d:.,~ ]+", c) and len(c.split()) >= 3 and ", " in c:
        i = c.rfind(", ")
        return c[:i] + " y " + c[i + 2:]
    return c


def table(cap, rows):
    return {"cap": cap, "rows": [[_refcell(c) for c in r] for r in rows]}


def box(items):
    return {"title": "Preguntas para la reflexión", "items": items}
