import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\qna"
SRC = os.path.join(H, "work_fr", "src_c03.json")
OUT = os.path.join(H, "fr", "c03.json")


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    for k, v in units.items():
        a, b = src[k]["answer"], v["answer"]
        print(k, "paras", a.count("\n\n"), b.count("\n\n"), "nl", a.count("\n"), b.count("\n"), "bold", a.count("**"), b.count("**"))
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))


def P(*paras):
    return "\n\n".join(paras)
