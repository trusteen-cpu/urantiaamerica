# -*- coding: utf-8 -*-
# helper: merge a dict of units into es/c03.json, keeping source key order
import json, os
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC = os.path.join(H, "work", "src_c03.json")
OUT = os.path.join(H, "es", "c03.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in units.items():
        assert k in src, k
        assert len(v["msg"]) == len(src[k]["msg"]), (k, len(v["msg"]), len(src[k]["msg"]))
        cur[k] = {"_ref": src[k]["_ref"], "t": v["t"], "msg": v["msg"], "pr": v["pr"]}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
