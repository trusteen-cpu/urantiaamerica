import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
OUT = os.path.join(BASE, "pt", "c09.json")
SRC = os.path.join(BASE, "work", "src_c09.json")


def add(units):
    src = json.load(open(SRC, encoding="utf-8"))
    D = {}
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding="utf-8"))
    D.update(units)
    for k, u in units.items():
        assert u["_ref"] == src[k]["_ref"], k
        assert len(u["msg"]) == len(src[k]["msg"]), (k, len(u["msg"]), len(src[k]["msg"]))
    R = {k: D[k] for k in src if k in D}
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(R), "units")
