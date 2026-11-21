import json, os
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SRC = json.load(open(os.path.join(H, "work", "src_c11.json"), encoding="utf-8"))
OUT = os.path.join(H, "es", "c11.json")


def save(units):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, u in units.items():
        s = SRC[k]
        assert len(u["msg"]) == len(s["msg"]), (k, len(u["msg"]), len(s["msg"]))
        cur[k] = {"_ref": s["_ref"], "t": u["t"], "msg": u["msg"], "pr": u["pr"]}
    D = {k: cur[k] for k in SRC if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
