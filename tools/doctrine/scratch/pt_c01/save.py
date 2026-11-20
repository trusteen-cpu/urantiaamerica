import json, os
here = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(here, "..", "..", "pt", "c01.json")
SRC = os.path.join(here, "..", "..", "work", "src_c01.json")


def merge(new):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in new:
        if k not in src:
            raise KeyError("unknown key " + k)
    cur.update(new)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "of", len(src))
