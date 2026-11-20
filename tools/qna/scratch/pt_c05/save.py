import json, os, sys
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work_pt", "src_c05.json")
OUT = os.path.join(BASE, "pt", "c05.json")


def save(key, question, paras):
    src = json.load(open(SRC, encoding="utf-8"))
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding="utf-8"))
    else:
        D = {}
    D[key] = {"question": question, "answer": "\n\n".join(paras)}
    # keep source order
    out = {k: D[k] for k in src if k in D}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    en = src[key]["answer"].split("\n\n")
    print(key, "paras", len(paras), "en", len(en), "OK" if len(paras) == len(en) else "MISMATCH")
