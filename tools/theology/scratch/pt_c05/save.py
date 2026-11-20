import json, os
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(H, "..", "..")
SRC = os.path.join(T, "work", "src_c05.json")
OUT = os.path.join(T, "pt", "c05.json")

def save(new):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k in new:
        assert k in src, k
    cur.update(new)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print("saved", len(D), "of", len(src), "missing next:", missing[:3])
