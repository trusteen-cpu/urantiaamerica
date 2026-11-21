# -*- coding: utf-8 -*-
# 청소년판(The Urantia Book for Young Readers) es/fr/pt — 번역 단위 만들기
#   극동판 tools/zh/youth/src/ 의 영어 단위(c01~c08, 약 3만 낱말씩)를 읽어 편 단위로 약 1만 2천~1만 6천 낱말씩 다시 나눈다.
#   키(pN.NNN, ui.*)와 값은 그대로. 극동판 파일은 읽기만 한다.
#   결과: src/cNN.json (영어 단위), src/_structure.json (편마다 [키, 종류] 순서 + _chunks) — 번역하지 않는다.
#   번역이 시작된 뒤에는 다시 돌리지 않는다(나누는 자리가 바뀔 수 있음).
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ZSRC = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\zh\youth\src"
SRC = os.path.join(H, "src"); os.makedirs(SRC, exist_ok=True)
LO, TARGET, HI = 12000, 14000, 16000

U = {}
for f in sorted(glob.glob(os.path.join(ZSRC, "c[0-9][0-9].json"))):
    U.update(json.load(open(f, encoding="utf-8")))
ST = json.load(open(os.path.join(ZSRC, "_structure.json"), encoding="utf-8"))
words = lambda v: len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split())

papers = sorted(int(k) for k in ST if k.isdigit())
pw = {n: sum(words(U[k]) for k, _ in ST[str(n)]["items"]) for n in papers}
ui = {k: v for k, v in U.items() if k.startswith("ui.")}
seen = set(ui) | {k for n in papers for k, _ in ST[str(n)]["items"]}
assert seen == set(U), f"keys differ: {sorted(set(U) ^ seen)[:10]}"

# 고르게 나누기: 덩이 수 = 전체/TARGET 반올림, 누적 낱말 수가 전체×i/덩이수 에 가장 가까운 편 경계에서 자른다.
total = sum(pw.values()) + sum(words(v) for v in ui.values())
k = max(1, round(total / TARGET))
groups, cur, acc, i = [], [], sum(words(v) for v in ui.values()), 1
for n in papers:
    goal = total * i / k
    if cur and i < k and abs(acc - goal) < abs(acc + pw[n] - goal):
        groups.append(cur); cur = []; i += 1
    cur.append(n); acc += pw[n]
groups.append(cur)

for f in glob.glob(os.path.join(SRC, "c[0-9][0-9].json")): os.remove(f)
struct = {str(n): ST[str(n)] for n in papers}
struct["_chunks"] = {}
tot_w = tot_q = 0
for i, g in enumerate(groups, 1):
    c = f"c{i:02d}"
    D = dict(ui) if i == 1 else {}
    for n in g:
        for k, _ in ST[str(n)]["items"]: D[k] = U[k]
    json.dump(D, open(os.path.join(SRC, c + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    wc = sum(words(v) for v in D.values()); nq = sum(v.count("⟦Q ") for v in D.values())
    desc = f"papers {g[0]}-{g[-1]}" + (" + UI strings" if i == 1 else "")
    struct["_chunks"][c] = desc
    tot_w += wc; tot_q += nq
    print(f"{c}\t{desc}\t{len(D)} units\t{wc} words\t{nq} quotations")
json.dump(struct, open(os.path.join(SRC, "_structure.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"total {tot_w} words, {tot_q} quotations, {len(groups)} chunks")
