import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
TH = os.path.normpath(os.path.join(HERE, "..", ".."))
SRC = os.path.join(TH, "work", "src_c04.json")
OUT = os.path.join(TH, "fr", "c04.json")


def save(T):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    cur.update(T)
    bad = [k for k in T if k not in src]
    if bad:
        raise SystemExit("unknown keys: %r" % bad)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))
