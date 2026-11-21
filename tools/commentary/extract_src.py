# -*- coding: utf-8 -*-
# 역주 해설(Paper-by-Paper Commentary, 196편 + 머리말) 스페인어·프랑스어·포르투갈어판 — 번역 단위 다시 묶기
#   원천: 극동판 tools/zh/commentary/src/cNN.json (영어 단위, 읽기만) + skeleton.json (쪽 구조)
#         = E:/OneDrive/유란시아 작업/uui-en/commentary/data/pNNN.json 에서 extract_commentary.py 가 뽑은 것.
#   결과: src/cNN.json (영어 단위, 키는 zh 와 같음 — pNNN.lead / pNNN.foot / pNNN.sI.h / pNNN.sI.bJ / ui.*)
#         src/skeleton.json {"papers": 쪽 구조, "chunks": {cNN: [pNNN, …]}}
#   묶음: 편 단위로 이어 붙여 영어 약 12,000–16,000 낱말(블록 인용 낱말 제외)씩. ui.* 는 c01.
#   다시 돌리면 src/ 를 새로 쓴다(<l>/ 번역본은 건드리지 않음 — 묶음 경계를 바꾸면 번역본 키도 옮겨야 하므로 번역 시작 뒤에는 돌리지 말 것).
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
ZH = os.path.join(FE, "tools", "zh", "commentary")
EN_DATA = r"E:/OneDrive/유란시아 작업/uui-en/commentary/data"
LO, TARGET, HI = 12000, 14000, 16000
SRC = os.path.join(H, "src"); os.makedirs(SRC, exist_ok=True)


def words(x):
    if isinstance(x, str): return len(re.sub(r"⟦/?Q[^⟧]*⟧", " ", x).split())
    if isinstance(x, dict): return sum(words(v) for k, v in x.items() if k not in ("cit", "ref", "q"))
    if isinstance(x, list): return sum(words(v) for v in x)
    return 0


U = {}
for f in sorted(glob.glob(os.path.join(ZH, "src", "c[0-9][0-9].json"))):
    U.update(json.load(open(f, encoding="utf-8")))
SKEL = json.load(open(os.path.join(ZH, "skeleton.json"), encoding="utf-8"))
UI = {k: v for k, v in U.items() if k.startswith("ui.")}
papers = []
for n in range(197):
    P = f"p{n:03d}"
    D = {k: v for k, v in U.items() if k.startswith(P + ".")}
    assert D and P in SKEL, P
    papers.append((P, D))
assert sum(len(d) for _, d in papers) + len(UI) == len(U), "unassigned units"

# 원천 확인: 극동판 영어 data 와 lead·블록 수가 같은지 (다르면 zh src 가 낡은 것)
stale = []
if os.path.isdir(EN_DATA):
    for P, D in papers:
        E = json.load(open(os.path.join(EN_DATA, P + ".json"), encoding="utf-8"))
        nb = sum(len(s["blocks"]) for s in E["sections"])
        if E["lead"] != D[P + ".lead"] or nb != sum(1 for k in D if re.search(r"\.b\d+$", k)): stale.append(P)
if stale: print("WARN zh src differs from the English data for:", stale)

# 묶기
# 고르게 나누기: 묶음 수 N = 전체/TARGET 반올림, 누적 낱말 수가 k·전체/N 에 가장 가까운 편 경계에서 자른다.
# (ui.* 는 c01 에 들어가므로 첫 묶음 낱말 수에 넣는다)
pw = [words(D) for _, D in papers]
total = sum(pw) + words(UI)
N = max(1, round(total / TARGET))
chunks, cur, acc, k = [], [], words(UI), 1
for (P, D), x in zip(papers, pw):
    if cur and k < N and abs(acc - k * total / N) < abs(acc + x - k * total / N):
        chunks.append(cur); cur, k = [], k + 1
    cur.append((P, D)); acc += x
chunks.append(cur)

CH = {}
tot = 0
print("chunk  papers      units  words  blockq  inlineq")
for ci, ch in enumerate(chunks, 1):
    cid = f"c{ci:02d}"
    out = dict(UI) if ci == 1 else {}
    for P, D in ch: out.update(D)
    json.dump(out, open(os.path.join(SRC, cid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    CH[cid] = [P for P, _ in ch]
    wc = words(out); tot += wc
    nq = sum(1 for v in out.values() if isinstance(v, dict) and "q" in v)
    ni = sum(json.dumps(v, ensure_ascii=False).count("⟦Q ") for v in out.values())
    print(f"{cid}    {ch[0][0]}-{ch[-1][0]}  {len(out):5d}  {wc:5d}  {nq:5d}  {ni:5d}")
for f in glob.glob(os.path.join(SRC, "c[0-9][0-9].json")):
    if os.path.basename(f)[:-5] not in CH: os.remove(f)
json.dump({"papers": SKEL, "chunks": CH}, open(os.path.join(SRC, "skeleton.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("total words", tot, "chunks", len(CH))
