import json, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(BASE, "es", "c02.json")
SRC = os.path.join(BASE, "work_es", "src_c02.json")

def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "of", len(src))

def U(q, paras):
    return {"question": q, "answer": "\n\n".join(paras)}
