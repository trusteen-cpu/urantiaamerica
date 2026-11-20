import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work_pt", "src_c06.json")
OUT = os.path.join(BASE, "pt", "c06.json")


def curly(s, k):
    out = []
    for p in s.split("\n\n"):
        if p.count('"') % 2:
            print("ODD QUOTES", k, p[:60])
            out.append(p)
            continue
        parts = p.split('"')
        r = parts[0]
        for i, x in enumerate(parts[1:]):
            r += ("“" if i % 2 == 0 else "”") + x
        out.append(r)
    return "\n\n".join(out)


def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in units.items():
        q, a = v
        if isinstance(a, list):
            a = "\n\n".join(a)
        q, a = curly(q, k), curly(a, k)
        n_src = src[k]["answer"].count("\n\n")
        n_new = a.count("\n\n")
        if n_src != n_new:
            print("PARA MISMATCH", k, n_src, n_new)
        cur[k] = {"question": q, "answer": a}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", list(units), "total", len(D))
