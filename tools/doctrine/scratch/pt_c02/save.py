import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(BASE, "pt", "c02.json")
SRC = os.path.join(BASE, "work", "src_c02.json")

def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    cur.update(units)
    for k in units:
        if k not in src:
            raise SystemExit("unknown key " + k)
        sv, tv = src[k], units[k]
        if type(sv) != type(tv):
            raise SystemExit("shape " + k)
        if isinstance(sv, dict):
            if "rows" in sv:
                assert len(sv["rows"]) == len(tv["rows"]), k
                for a, b in zip(sv["rows"], tv["rows"]):
                    assert len(a) == len(b), (k, a)
            else:
                assert len(sv["items"]) == len(tv["items"]), k
    D = {k: cur[k] for k in src if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print("saved", len(D), "of", len(src), "missing", len(missing), missing[:5])
