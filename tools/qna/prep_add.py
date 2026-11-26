# -*- coding: utf-8 -*-
# qna 새 질문 추가 준비 (2026-11-26: Q 121–144). prep.py 는 전체를 다시 나누므로 쓰지 않고, 기존 조각(c01–c06)은 그대로 두고
# 극동판 tools/zh/qna/src 의 새 조각(c04, c05 …)을 여기 새 조각(c07, c08 …)으로 덧붙인다.
#   python prep_add.py c04=c07 c05=c08
#   → src/units.json·src/chunks.json 에 추가, quotes_<l>.json 에 새 인용 추가(자동 맞춤 + manual_<l>.json), work_<l>/src_cNN.json 생성
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


def sents(t):
    out, pos = [], 0
    for m in SPLIT.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def span(q, cit):
    if cit not in EN: return None
    es = sents(EN[cit]); wq = W(q)
    for i in range(len(es)):
        for j in range(i, len(es)):
            if W(" ".join(es[i:j + 1])) == wq: return i, j, len(es)
    return None


U = json.load(open(os.path.join(H, "src", "units.json"), encoding="utf-8"))
CH = json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))
new = {}
for spec in sys.argv[1:]:
    fe, am = spec.split("=")
    if am in CH: raise SystemExit(f"{am} already in chunks.json")
    D = json.load(open(os.path.join(FE_SRC, f"{fe}.json"), encoding="utf-8"))
    for k in D:
        if k in U: raise SystemExit(f"{k} already in units.json")
    U.update(D); CH[am] = list(D); new[am] = list(D)
json.dump(U, open(os.path.join(H, "src", "units.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(CH, open(os.path.join(H, "src", "chunks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)

for l in amq.LANGS:
    mp = os.path.join(H, f"manual_{l}.json")
    manual = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
    qp = os.path.join(H, f"quotes_{l}.json")
    Q = json.load(open(qp, encoding="utf-8"))
    fail = []
    for am, ks in new.items():
        for k in ks:
            for n, m in enumerate(QM.finditer(U[k]["answer"])):
                cit, q = m.group(1), m.group(2)
                key = f"{k}#{n}"; t = None
                if key in manual: t = manual[key]
                else:
                    sp = span(q, cit)
                    if sp:
                        i, j, cnt = sp
                        ts = sents(amq.text(l, cit))
                        if len(ts) == cnt: t = " ".join(ts[i:j + 1])
                if t is not None and not amq.check(l, cit, t): t = None
                if t is None: fail.append((key, cit, q))
                Q.append([k, n, cit, t])
    json.dump(Q, open(qp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(l, "new quotes unresolved", len(fail))
    for f in fail: print("   ", f[0], f[1], "|", f[2][:90])
    QD = {(k, n): t for k, n, cit, t in Q}
    wd = os.path.join(H, f"work_{l}")
    for am, ks in new.items():
        D = {}
        for k in ks:
            v = U[k]; cnt = iter(range(1000))
            def rep(m, k=k, cnt=cnt):
                t = QD[(k, next(cnt))]
                return f"⟦Q {m.group(1)}⟧{t if t is not None else m.group(2)}⟦/Q⟧"
            D[k] = {"question": v["question"], "answer": QM.sub(rep, v["answer"])}
        json.dump(D, open(os.path.join(wd, f"src_{am}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for am, ks in new.items():
    print(am, ks[0], "-", ks[-1], sum(len((U[k]["question"] + " " + U[k]["answer"]).split()) for k in ks), "words")
