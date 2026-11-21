import json, re, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
SRC = os.path.join(BASE, "work", "src_c04.json")
OUT = os.path.join(BASE, "fr", "c04.json")


def fixnum(s):
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"(\d) (\d{3})(?!\d)", "\\1\u00a0\\2", s)
    return s


def fix(v):
    if isinstance(v, list):
        return [fixnum(x) for x in v]
    return fixnum(v)


def save(new):
    src = json.load(open(SRC, encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in new:
        if k not in src:
            print("NOT IN SRC", k)
    D.update(new)
    out = {k: fix(D[k]) for k in src if k in D}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(len(out), "/", len(src))
