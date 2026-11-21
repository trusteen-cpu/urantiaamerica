import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work", "src_c07.json")
OUT = os.path.join(BASE, "es", "c07.json")

def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    cur.update(units)
    for k, u in units.items():
        s = src[k]
        assert u["_ref"] == s["_ref"], k
        assert len(u["msg"]) == len(s["msg"]), (k, len(u["msg"]), len(s["msg"]))
    D = {k: cur[k] for k in src if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
