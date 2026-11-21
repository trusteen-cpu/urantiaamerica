# -*- coding: utf-8 -*-
# 「유란시아서 요약본」(The Urantia Book, Abridged) 영어 원고 → tools/abridged/src/cNN.json
#   극동판 tools/zh/abridged/src/c01..c12.json(영어 단위, ⟦Q⟧ 표시 포함)을 그대로 가져와(읽기만 함)
#   편 단위로 다시 묶는다(덩어리당 영어 약 12,000~16,000 낱말). 키·값은 바꾸지 않는다. ui.* 는 c01 에.
#   다시 돌리면 src/ 를 새로 쓴다 — 번역이 시작된 뒤에는 돌리지 말 것(키가 다른 덩어리로 옮겨 갈 수 있음).
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ZH = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\zh\abridged\src"
TARGET, MAXW = 14000, 16000


def wc(v):
    if isinstance(v, list): return sum(wc(x) for x in v)
    return len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split())


D = {}
for f in sorted(os.listdir(ZH)):
    if re.fullmatch(r"c\d\d\.json", f):
        D.update(json.load(open(os.path.join(ZH, f), encoding="utf-8")))
UI = {k: v for k, v in D.items() if k.startswith("ui.")}
papers = {}
for k, v in D.items():
    if k.startswith("ui."): continue
    papers.setdefault(int(k.split(".")[0]), {})[k] = v
order = sorted(papers)
chunks, cur, cw = [], [], wc(list(UI.values()))
for no in order:
    w = sum(wc(v) for v in papers[no].values())
    if cur and cw + w > MAXW and cw >= TARGET - 3000:
        chunks.append((cur, cw)); cur, cw = [], 0
    cur.append(no); cw += w
if cur:
    if chunks and cw < 8000:
        a, b = chunks.pop(); chunks.append((a + cur, b + cw))
    else: chunks.append((cur, cw))
for f in os.listdir(os.path.join(H, "src")):
    if re.fullmatch(r"c\d\d\.json", f): os.remove(os.path.join(H, "src", f))
listing = []
for n, (nos, w) in enumerate(chunks, 1):
    cid = f"c{n:02d}"
    out = dict(UI) if n == 1 else {}
    for no in nos: out.update(papers[no])
    json.dump(out, open(os.path.join(H, "src", cid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    listing.append({"id": cid, "papers": f"{nos[0]}-{nos[-1]}", "words": w, "units": len(out)})
json.dump(listing, open(os.path.join(H, "src", "chunks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
assert sum(x["units"] for x in listing) == len(D)
for x in listing: print(x)
print("units", len(D), "words", sum(x["words"] for x in listing))
