import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
SRC = os.path.join(BASE, "work", "src_c11.json")
OUT = os.path.join(BASE, "pt", "c11.json")

def save(part):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in part.items():
        assert k in src, k
        s = src[k]
        assert len(v["msg"]) == len(s["msg"]), (k, len(v["msg"]), len(s["msg"]))
        cur[k] = {"_ref": s["_ref"], "t": v["t"], "msg": v["msg"], "pr": v["pr"]}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
