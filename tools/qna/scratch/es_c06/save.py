import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work_es", "src_c06.json")
OUT = os.path.join(BASE, "es", "c06.json")
def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, (q, paras) in units.items():
        cur[k] = {"question": q, "answer": "\n\n".join(paras) if isinstance(paras, list) else paras}
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k in units:
        ep = src[k]["answer"].count("\n\n"); tp = out[k]["answer"].count("\n\n")
        print(k, "paras", ep, tp, "OK" if ep == tp else "MISMATCH")
