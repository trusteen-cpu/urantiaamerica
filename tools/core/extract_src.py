# -*- coding: utf-8 -*-
# 핵심 진리 (core, "The Core Truth of the Urantia Book") 스페인어·프랑스어·포르투갈어판 — 번역 단위 만들기
#   극동판 tools/zh/core/src/{c01,c02,ui}.json (영어 단위, extract_core_src.py 가 site/core-en/index.html 에서 뽑은 것)을
#   그대로 가져와 영어 1.2만~1.5만 단어 묶음 5개로 다시 나눈다(키는 그대로). 극동판 파일은 읽기만 한다.
#   결과: src/c01..c05.json  (c01 에는 화면 글자 UI 키 71개도 들어 있다: "page_title", "logo", …  — 장 키는 "NN.…")
#   다시 돌리면 src/ 를 새로 쓴다(<l>/ 번역본은 건드리지 않음).
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
ZSRC = os.path.join(FE, "tools", "zh", "core", "src")
EN_PAGE = os.path.join(FE, "site", "core-en", "index.html")
SRC = os.path.join(H, "src"); os.makedirs(SRC, exist_ok=True)

CHUNKS = [("c01", 1, 13), ("c02", 14, 25), ("c03", 26, 33), ("c04", 34, 43), ("c05", 44, 52)]
REF = re.compile(r"\[(\d+:\d+\.\d+)\]")


def words(v):
    t = re.sub(r"⟦/?Q[^⟧]*⟧", " ", v)
    t = REF.sub(" ", t)
    t = re.sub(r"<[^>]+>|&\w+;", " ", t)
    return len(t.split())


units = {}
for c in ("c01", "c02"):
    units.update(json.load(open(os.path.join(ZSRC, c + ".json"), encoding="utf-8")))
UI = json.load(open(os.path.join(ZSRC, "ui.json"), encoding="utf-8"))

# 영어판 페이지와 맞는지 확인(장 52개, 제목이 같음)
s = open(EN_PAGE, encoding="utf-8").read()
i = s.index("const CHAPTERS=") + len("const CHAPTERS=")
ch, _ = json.JSONDecoder().raw_decode(s, i)
assert [c["num"] for c in ch] == list(range(1, 53))
for c in ch:
    assert units["%02d.title" % c["num"]] == c["title"], c["num"]
assert all(re.fullmatch(r"\d\d\.(title|\d{3}\.(h3|h4|p))", k) for k in units)
assert not set(UI) & set(units)

tot = 0
print("chunk | chapters | units | English words | ⟦Q⟧ quotations | [P:S.p] citations")
for cid, a, b in CHUNKS:
    d = {}
    if cid == "c01":
        d.update(UI)
    d.update({k: v for k, v in units.items() if a <= int(k[:2]) <= b})
    w = sum(words(v) for v in d.values()); tot += w
    nq = sum(v.count("⟦Q ") for v in d.values())
    nr = sum(len(REF.findall(v)) for v in d.values())
    json.dump(d, open(os.path.join(SRC, cid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{cid} | {a}-{b}{' + UI' if cid == 'c01' else ''} | {len(d)} | {w} | {nq} | {nr}")
assert sum(len(json.load(open(os.path.join(SRC, c + '.json'), encoding='utf-8'))) for c, _, _ in CHUNKS) == len(units) + len(UI)
print("total words", tot)
