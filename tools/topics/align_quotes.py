# -*- coding: utf-8 -*-
# 인용 자동 맞추기: 영어 인용이 영어 절의 몇 번째 문장(들)인지 찾고, 공식 번역 절의 문장 수가 같으면 같은 번째 문장(들)을 글자 그대로 가져온다.
#   결과: auto_<l>.json {키: 공식 번역 인용}.  맞추지 못한 것은 work/todo_<l>.json 에 영어 인용·영어 절·번역 절과 함께 적는다
#   (그것은 quotes_spec.py 에 (시작 문구, 끝 문구) 로 손으로 정한다).
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
Q = json.load(open(os.path.join(H, "src", "quotes.json"), encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡]?[A-ZÀ-ÖØ-Þ0-9—–-])")
W = lambda s: re.sub(r"\W+", "", s).lower()


def sents(t):
    out, pos = [], 0
    for m in SPLIT.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def span(q, cit):
    es = sents(EN[cit]); wq = W(q)
    for i in range(len(es)):
        for j in range(i, len(es)):
            if W(" ".join(es[i:j + 1])) == wq: return i, j, len(es)
    return None


def beads(ens, ts, R):
    """길이 기반 문장 맞춤(Gale-Church 비슷): (영어 문장 범위, 번역 문장 범위) 목록. 1-1, 1-2, 2-1, 2-2, 1-3, 3-1 허용."""
    import math
    n, m = len(ens), len(ts)
    INF = float("inf")
    C = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]
    C[0][0] = 0
    moves = ((1, 1, 0), (1, 2, .6), (2, 1, .6), (2, 2, 1.0), (1, 3, 1.2), (3, 1, 1.2))
    for a in range(n + 1):
        for b in range(m + 1):
            if C[a][b] == INF: continue
            for da, db, pen in moves:
                if a + da > n or b + db > m: continue
                le = sum(len(x) for x in ens[a:a + da]) * R; lt = sum(len(x) for x in ts[b:b + db])
                c = C[a][b] + abs(math.log((lt + 5) / (le + 5))) * 3 + pen
                if c < C[a + da][b + db]: C[a + da][b + db] = c; B[a + da][b + db] = (a, b)
    if C[n][m] == INF: return None
    out, a, b = [], n, m
    while (a, b) != (0, 0):
        pa, pb = B[a][b]; out.append(((pa, a), (pb, b))); a, b = pa, pb
    out.reverse()
    # 맞춤이 믿을 만한가: 모든 구슬의 길이 비율이 그럴듯해야
    for (a0, a1), (b0, b1) in out:
        le = sum(len(x) for x in ens[a0:a1]) * R; lt = sum(len(x) for x in ts[b0:b1])
        if not 0.6 <= (lt + 5) / (le + 5) <= 1.65: return None
    return out


def en_range(q, en):
    """인용이 영어 절 문장들 중 어디(a..b)에 걸치는지, 그리고 그 문장들 중 몇 %를 덮는지."""
    if "…" in q or "..." in q: return None
    ens = sents(en)
    wq = W(q)
    acc, starts = "", []
    for x in ens: starts.append(len(acc)); acc += W(x)
    k = acc.find(wq)
    if k < 0: return None
    e = k + len(wq)
    a = max(i for i, st in enumerate(starts) if st <= k)
    b = max(i for i, st in enumerate(starts) if st < e)
    cover = len(wq) / len(W(" ".join(ens[a:b + 1])))
    return a, b, cover


def main(langs):
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    for l in langs:
        res, todo, ext = {}, {}, []
        for k, v in Q.items():
            cit, q = v["cit"], v["q"]
            ens, ts = sents(EN[cit]), sents(amq.text(l, cit))
            R = len(amq.text(l, cit)) / len(EN[cit])
            rr = en_range(q, EN[cit])
            why = "not found in English verse" if not rr else "no reliable alignment"
            if rr:
                a, b, cover = rr
                bd = beads(ens, ts, R)
                if bd:
                    sel = [(ea, ta) for ea, ta in bd if ea[0] <= b and ea[1] > a]  # 인용이 걸친 구슬들
                    ea0, ea1 = sel[0][0][0], sel[-1][0][1]
                    full = W(" ".join(ens[ea0:ea1]))
                    cov = len(W(q)) / len(full)
                    t = " ".join(ts[sel[0][1][0]:sel[-1][1][1]])
                    if cov > 0.999 or cov >= 0.8:
                        assert amq.check(l, cit, t)
                        res[k] = t
                        if cov < 0.999: ext.append(k)
                        continue
                    why = f"partial ({cov:.0%} of the aligned sentence(s))"
            todo[k] = {"cit": cit, "why": why, "en_quote": q, "en_verse": EN[cit], "verse": amq.text(l, cit)}
        json.dump(res, open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        json.dump(todo, open(os.path.join(H, "work", f"todo_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        json.dump(ext, open(os.path.join(H, "work", f"extended_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "auto", len(res), f"(of which {len(ext)} whole sentence for an 80%+ partial quote)", "todo", len(todo))


if __name__ == "__main__":
    main(sys.argv[1:] or ["es", "fr", "pt"])
