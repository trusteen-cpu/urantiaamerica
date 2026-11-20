import json, os
BASE = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\qna"
SRC = os.path.join(BASE, "work_fr", "src_c04.json")
OUT = os.path.join(BASE, "fr", "c04.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, (q, paras) in units.items():
        a = "\n\n".join(paras) if isinstance(paras, list) else paras
        n_en = src[k]["answer"].count("\n\n")
        n_fr = a.count("\n\n")
        nl_en = src[k]["answer"].count("\n")
        nl_fr = a.count("\n")
        if n_en != n_fr or nl_en != nl_fr:
            print("WARN", k, "paras", n_en, n_fr, "lines", nl_en, nl_fr)
        cur[k] = {"question": q, "answer": a}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "units")
