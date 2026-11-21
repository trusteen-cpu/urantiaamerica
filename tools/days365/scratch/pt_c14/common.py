# -*- coding: utf-8 -*-
import json, os
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
OUT = os.path.join(H, "pt", "c14.json")
SRC = os.path.join(H, "work", "src_c14.json")


def save(D):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in D.items():
        assert k in src, k
        e = src[k]
        assert len(v["msg"]) == len(e["msg"]), (k, len(v["msg"]), len(e["msg"]))
        cur[k] = {"_ref": e["_ref"], "t": v["t"], "msg": v["msg"], "pr": v["pr"]}
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(out), "units")
