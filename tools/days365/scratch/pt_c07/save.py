import json, os
BASE = os.path.join(os.path.dirname(__file__), "..", "..")
SRC = os.path.join(BASE, "work", "src_c07.json")
OUT = os.path.join(BASE, "pt", "c07.json")

def save(U):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(U)
    for k, u in U.items():
        s = src[k]
        assert u["_ref"] == s["_ref"], k
        assert len(u["msg"]) == len(s["msg"]), (k, len(u["msg"]), len(s["msg"]))
    D = {}
    for k in src:
        if k in cur:
            D[k] = {"_ref": cur[k]["_ref"], "t": cur[k]["t"], "msg": cur[k]["msg"], "pr": cur[k]["pr"]}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
