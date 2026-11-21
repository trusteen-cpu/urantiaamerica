import json, os
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(H, "es", "c01.json")
SRC = json.load(open(os.path.join(H, "work", "src_c01.json"), encoding="utf-8"))


def merge(T):
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    bad = [k for k in T if k not in SRC]
    if bad: raise SystemExit("unknown keys: %s" % bad)
    for k, v in T.items():
        e = SRC[k]
        if isinstance(e, list):
            assert isinstance(v, list) and len(v) == len(e) and all(len(a) == len(b) for a, b in zip(v, e)), "shape " + k
        else:
            assert isinstance(v, str), k
    cur.update(T)
    D = {k: cur[k] for k in SRC if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(SRC))


def show(prefix):
    for k, v in SRC.items():
        if k.split(".")[0] == prefix:
            print(k, json.dumps(v, ensure_ascii=False))
