import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(BASE, "fr", "c18.json")
SRC = os.path.join(BASE, "work", "src_c18.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    for k in units:
        if k not in src:
            raise SystemExit("unknown key " + k)
        if type(units[k]) != type(src[k]):
            raise SystemExit("type " + k)
        if isinstance(src[k], list):
            if len(units[k]) != len(src[k]) or any(len(a) != len(b) for a, b in zip(units[k], src[k])):
                raise SystemExit("table shape " + k)
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print("saved", len(D), "of", len(src), "missing", len(missing))
    pref = sorted(set(k.split(".")[0] for k in units))
    print("missing in these papers:", [k for k in missing if k.split(".")[0] in pref])
