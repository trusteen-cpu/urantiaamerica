# -*- coding: utf-8 -*-
# 「A Thousand Questions and Answers」(qna) es·fr·pt — 준비 단계 (영어판이 바뀌었을 때만 다시 돌린다)
#   1) 극동판 tools/zh/qna/src/c0*.json (영어 단위, ⟦P⟧·⟦Q⟧ 표시가 된 것; 읽기만) → src/units.json (한 파일) + src/chunks.json (번역 조각 나누기)
#   2) ⟦Q k⟧영어⟦/Q⟧ 인용 67곳을 공식 번역에서 자른다: 문장 단위 자동 맞춤(auto) + manual_<l>.json(손으로 정한 것, 우선)
#      → quotes_<l>.json  [[unit, n번째, cit, 공식 인용문 또는 null], ...]
#   3) 번역자용 원고 work_<l>/cNN.json : 영어 단위인데 ⟦Q⟧ 안은 이미 공식 번역 인용문 (번역자는 표시째 그대로 둔다)
#   python prep.py          (인용 못 맞춘 것을 보고)
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(H, "..")))
import amq  # noqa: E402

FE_SRC = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\zh\qna\src"
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
QM = re.compile(r"⟦Q ([^⟧\s]+)⟧(.*?)⟦/Q⟧", re.S)
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡]?[A-ZÀ-ÖØ-Þ0-9—–-])")
W = lambda s: re.sub(r"\W+", "", s).lower()
NCHUNK = 6


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


def main():
    U = {}
    for c in ("c01", "c02", "c03"):
        U.update(json.load(open(os.path.join(FE_SRC, f"{c}.json"), encoding="utf-8")))
    os.makedirs(os.path.join(H, "src"), exist_ok=True)
    json.dump(U, open(os.path.join(H, "src", "units.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # chunks by word count (ui goes with c01)
    qs = [k for k in U if k.startswith("q")]
    wc = {k: len(U[k]["question"].split()) + len(U[k]["answer"].split()) for k in qs}
    target = sum(wc.values()) / NCHUNK
    chunks, cur, acc = [], [], 0
    for k in qs:
        cur.append(k); acc += wc[k]
        if acc >= target * (len(chunks) + 1) and len(chunks) < NCHUNK - 1: chunks.append(cur); cur = []
    chunks.append(cur)
    chunks[0] = [k for k in U if k.startswith("ui.")] + chunks[0]
    CH = {f"c{i + 1:02d}": ks for i, ks in enumerate(chunks)}
    json.dump(CH, open(os.path.join(H, "src", "chunks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for c, ks in CH.items():
        print(c, ks[0] if not ks[0].startswith("ui") else "ui+" + [k for k in ks if k[0] == "q"][0], "-", ks[-1],
              sum(wc.get(k, 0) for k in ks), "words")

    for l in amq.LANGS:
        mp = os.path.join(H, f"manual_{l}.json")
        manual = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
        Q, fail = [], []
        for k in qs:
            for n, m in enumerate(QM.finditer(U[k]["answer"])):
                cit, q = m.group(1), m.group(2)
                key = f"{k}#{n}"
                t = None
                if key in manual:
                    t = manual[key]
                else:
                    sp = span(q, cit)
                    if sp:
                        i, j, cnt = sp
                        ts = sents(amq.text(l, cit))
                        if len(ts) == cnt: t = " ".join(ts[i:j + 1])
                if t is not None and not amq.check(l, cit, t): t = None
                if t is None: fail.append((key, cit, q))
                Q.append([k, n, cit, t])
        json.dump(Q, open(os.path.join(H, f"quotes_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "quotes", len(Q), "unresolved", len(fail))
        for f in fail: print("   ", f[0], f[1], "|", f[2][:90])
        # translator sources
        QD = {(k, n): t for k, n, cit, t in Q}
        wd = os.path.join(H, f"work_{l}"); os.makedirs(wd, exist_ok=True)
        for c, ks in CH.items():
            D = {}
            for k in ks:
                v = U[k]
                if isinstance(v, dict):
                    cnt = iter(range(1000))
                    def rep(m, k=k, cnt=cnt):
                        t = QD[(k, next(cnt))]
                        return f"⟦Q {m.group(1)}⟧{t if t is not None else m.group(2)}⟦/Q⟧"
                    D[k] = {"question": v["question"], "answer": QM.sub(rep, v["answer"])}
                else:
                    D[k] = v
            json.dump(D, open(os.path.join(wd, f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


main()
