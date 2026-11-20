# -*- coding: utf-8 -*-
# 인용 자동 맞추기 → auto_<l>.json {"키#번째": "공식 번역 인용"}
#   절 전체 인용(whole) → 그 절 전체.
#   그 밖: 영어 인용을 ' … ' 토막으로 나누고, 토막마다 영어 절의 몇 번째 문장들인지 찾는다(문장 경계가 맞을 때만).
#   번역 절의 문장 수가 영어와 같으면 같은 번째 문장들을 글자 그대로 가져와 ' … ' 로 잇는다.
#   문장 중간에서 자른 토막이 있거나 문장 수가 다르면 자동으로 하지 않고 manual 목록(todo_<l>.json)에 넣는다.
#   실행: python align_quotes.py [es fr pt]
import glob, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
ELL = " … "


def sents(t):
    out, pos = [], 0
    for m in SPLIT.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def span(q, ss):
    wq = W(q)
    for i in range(len(ss)):
        acc = ""
        for j in range(i, len(ss)):
            acc += W(ss[j])
            if acc == wq: return i, j
            if len(acc) > len(wq): break
    return None


def quote_items():
    S = {}
    for f in sorted(glob.glob(os.path.join(H, "src", "c[0-9][0-9].json"))):
        S.update(json.load(open(f, encoding="utf-8")))
    for k, v in S.items():
        if isinstance(v, dict):
            refs = v["cit"] if isinstance(v["cit"], list) else [v["cit"]]
            for i, (r, t) in enumerate(zip(refs, v["text"])):
                yield f"{k}#{i}", r, t, v["whole"]


def align(l, r, t, whole):
    if whole: return amq.text(l, r), None
    es = sents(EN[r]); ts = sents(amq.text(l, r))
    if len(es) != len(ts): return None, f"sentence count en {len(es)} vs {l} {len(ts)}"
    out = []
    for seg in t.split(ELL):
        sp = span(seg.strip(), es)
        if not sp: return None, "partial sentence"
        out.append(" ".join(ts[sp[0]:sp[1] + 1]))
    q = ELL.join(out)
    x = (len(q) / len(t)) / (len(amq.text(l, r)) / len(EN[r]))   # 길이 비율이 절 전체 비율과 크게 다르면 문장 대응이 어긋난 것
    if not 0.7 <= x <= 1.4: return None, f"length mismatch {x:.2f}"
    return q, None


def main(langs):
    items = list(quote_items())
    for l in langs:
        res, todo = {}, {}
        for key, r, t, whole in items:
            q, why = align(l, r, t, whole)
            if q is not None:
                assert amq.check(l, r, q), (key, r)
                res[key] = q
            else:
                todo[key] = {"cit": r, "en": t, "why": why}
        json.dump(res, open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        json.dump(todo, open(os.path.join(H, f"todo_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "items", len(items), "auto", len(res), "to cut by hand", len(todo))


main(sys.argv[1:] or ["es", "fr", "pt"])
