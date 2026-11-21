import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(ROOT, "fr", "c02.json")
SRC = json.load(open(os.path.join(ROOT, "work", "src_c02.json"), encoding="utf-8"))


def save(D):
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in D:
        if k not in SRC: raise SystemExit("not in source: " + k)
        ev = SRC[k]
        if isinstance(ev, list) and (not isinstance(D[k], list) or len(D[k]) != len(ev)):
            raise SystemExit("shape: " + k)
    cur.update(D)
    res = {k: cur[k] for k in SRC if k in cur}
    json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    miss = [k for k in SRC if k not in res]
    print(f"saved {len(res)}/{len(SRC)}; next missing: {miss[:5]}")
