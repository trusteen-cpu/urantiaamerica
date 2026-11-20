import json, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work_fr", "src_c06.json")
OUT = os.path.join(BASE, "fr", "c06.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, (q, a) in units.items():
        if isinstance(a, list):
            a = "\n\n".join(a)
        n_src = src[k]["answer"].count("\n\n")
        n_dst = a.count("\n\n")
        if n_src != n_dst:
            print("PARA MISMATCH", k, n_src + 1, n_dst + 1)
        cur[k] = {"question": q, "answer": a}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))
