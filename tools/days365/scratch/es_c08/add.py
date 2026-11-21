import json, os, sys
H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, "..", "..", "es", "c08.json")
SRC = os.path.join(H, "..", "..", "work", "src_c08.json")
def add(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    for k, v in units.items():
        assert v["_ref"] == src[k]["_ref"], k
        assert len(v["msg"]) == len(src[k]["msg"]), (k, len(v["msg"]), len(src[k]["msg"]))
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D))
