import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
SRC = os.path.join(BASE, "work", "src_c02.json")
OUT = os.path.join(BASE, "pt", "c02.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    D = {}
    for k in src:
        if k in cur:
            u = cur[k]
            assert u["_ref"] == src[k]["_ref"], k
            assert len(u["msg"]) == len(src[k]["msg"]), (k, len(u["msg"]), len(src[k]["msg"]))
            D[k] = {"_ref": u["_ref"], "t": u["t"], "msg": u["msg"], "pr": u["pr"]}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
