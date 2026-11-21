# -*- coding: utf-8 -*-
import json, os
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(H, "work", "src_c02.json")
OUT = os.path.join(H, "es", "c02.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    D = {}
    for k in src:
        if k in cur:
            u = cur[k]
            D[k] = {"_ref": src[k]["_ref"], "t": u["t"], "msg": u["msg"], "pr": u["pr"]}
            assert len(u["msg"]) == len(src[k]["msg"]), (k, len(u["msg"]), len(src[k]["msg"]))
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
