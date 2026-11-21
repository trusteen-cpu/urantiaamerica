import json, os
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC = os.path.join(H, "work", "src_c06.json")
OUT = os.path.join(H, "es", "c06.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    D = {}
    for k, v in src.items():
        if k in cur:
            u = cur[k]
            D[k] = {"_ref": v["_ref"], "t": u["t"], "msg": u["msg"], "pr": u["pr"]}
            assert len(u["msg"]) == len(v["msg"]), (k, len(u["msg"]), len(v["msg"]))
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
