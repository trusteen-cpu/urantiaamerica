# -*- coding: utf-8 -*-
# 인용 자동 맞추기 (한 번 돌려 quotes_<l>.json 초안을 만든다; 이후 손으로 고친 것은 manual_<l>.json 에 둔다)
#   영어 인용이 영어 절의 몇 번째 문장들인지 찾고, 번역 절의 문장 수가 같으면 같은 번째 문장들을 글자 그대로 가져온다.
#   결과: quotes_<l>.json {"키 경로|cit": "공식 번역 인용"}, 맞추지 못한 것은 화면에 보고.
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
S = json.load(open(os.path.join(H, "src", "c01.json"), encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡]?[A-ZÀ-ÖØ-Þ0-9—–-])")
W = lambda s: re.sub(r"\W+", "", s).lower()


def sents(t):
    out, pos = [], 0
    for m in SPLIT.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def quotes(x, p=""):
    if isinstance(x, dict):
        if "cit" in x and "q" in x: yield p, x["cit"], x["q"]
        for k, v in x.items(): yield from quotes(v, f"{p}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from quotes(v, f"{p}[{i}]")


def span(q, cit):
    es = sents(EN[cit]); wq = W(q)
    for i in range(len(es)):
        for j in range(i, len(es)):
            if W(" ".join(es[i:j + 1])) == wq: return i, j, len(es)
    return None


def main(langs):
    for l in langs:
        res, fail = {}, []
        for k, v in S.items():
            for p, cit, q in quotes(v, k):
                sp = span(q, cit)
                if not sp: fail.append((p, cit, "partial sentence")); continue
                i, j, n = sp
                ts = sents(amq.text(l, cit))
                if len(ts) != n: fail.append((p, cit, f"count en {n} vs {len(ts)}")); continue
                t = " ".join(ts[i:j + 1])
                assert amq.check(l, cit, t)
                res[f"{p}|{cit}"] = t
        json.dump(res, open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "auto", len(res), "fail", len(fail))
        for f in fail: print("  ", *f)


main(sys.argv[1:] or ["es", "fr", "pt"])
