# -*- coding: utf-8 -*-
import json, os
H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(H, "..", "..", "fr", "c11.json"))
SRC = os.path.normpath(os.path.join(H, "..", "..", "work", "src_c11.json"))


def save(U):
    S = json.load(open(SRC, encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    D.update(U)
    out = {}
    for k, v in S.items():
        if k in D:
            u = D[k]
            assert u["_ref"] == v["_ref"], k
            assert len(u["msg"]) == len(v["msg"]), (k, len(u["msg"]), len(v["msg"]))
            out[k] = {"_ref": u["_ref"], "t": u["t"], "msg": u["msg"], "pr": u["pr"]}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(out), "units")
