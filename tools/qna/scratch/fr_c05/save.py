import json, os
BASE = os.path.join(os.path.dirname(__file__), "..", "..")
OUT = os.path.join(BASE, "fr", "c05.json")
SRC = os.path.join(BASE, "work_fr", "src_c05.json")

def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    D.update(units)
    ordered = {k: D[k] for k in src if k in D}
    json.dump(ordered, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in units.items():
        n1 = src[k]["answer"].count("\n\n"); n2 = v["answer"].count("\n\n")
        b1 = src[k]["answer"].count("**"); b2 = v["answer"].count("**")
        print(k, "paras", n1, n2, "OK" if n1 == n2 else "MISMATCH", "bold", b1, b2)
    print("saved", len(ordered), "units")
