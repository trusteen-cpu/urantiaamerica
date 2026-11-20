import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work_pt", "src_c04.json")
OUT = os.path.join(BASE, "pt", "c04.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in units.items():
        cur[k] = {"question": v[0].strip(), "answer": v[1].strip("\n")}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k in units:
        a, b = src[k]["answer"], D[k]["answer"]
        print(k, "paras", a.count("\n\n"), b.count("\n\n"), "lines", a.count("\n"), b.count("\n"), "bold", a.count("**"), b.count("**"))
    print("saved", len(D))
