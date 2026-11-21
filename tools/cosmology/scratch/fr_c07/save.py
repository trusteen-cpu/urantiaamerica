import json, os, re
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
OUT = os.path.join(H, "fr", "c07.json")


def fix(s):
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", s)
    s = re.sub(r"(?<=\d) (?=\d{3}\b)", "\u00a0", s)
    s = s.replace("'", "’")
    return s


def save(T):
    src = json.load(open(os.path.join(H, "work", "src_c07.json"), encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    for k, v in T.items():
        assert k in src, k
        if isinstance(src[k], list):
            assert isinstance(v, list) and len(v) == len(src[k]), k
            v = [fix(x) for x in v]
        else:
            assert isinstance(v, str), k
            v = fix(v)
        cur[k] = v
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))
