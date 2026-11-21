import json, os
H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, "..", "..", "es", "c09.json")
SRC = os.path.join(H, "..", "..", "work", "src_c09.json")
def add(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    for k, u in units.items():
        assert u["_ref"] == src[k]["_ref"], k
        assert len(u["msg"]) == len(src[k]["msg"]), (k, len(u["msg"]), len(src[k]["msg"]))
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D))
