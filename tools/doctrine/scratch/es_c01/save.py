import json, os
OUT = "es/c01.json"

def save(U):
    src = json.load(open("work/src_c01.json", encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    D.update(U)
    R = {k: D[k] for k in src if k in D}
    json.dump(R, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(R), "/", len(src))
