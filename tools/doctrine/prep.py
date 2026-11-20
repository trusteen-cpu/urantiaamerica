# -*- coding: utf-8 -*-
# 도우미용 작업 파일 만들기 (원고나 auto 가 바뀌면 다시 돌린다)
#   work/src_cNN.json        번역할 영어 단위(인용 제외: 글·표·질문 상자·part·audio) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json   자동으로 못 맞춘 인용: {"chNN:i": {"cit", "en"(영어 인용), "why"}}
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(H, "work"), exist_ok=True)
TODO = {l: json.load(open(os.path.join(H, f"todo_{l}.json"), encoding="utf-8")) for l in ("es", "fr", "pt")}


def wc(x):
    if isinstance(x, str): return len(x.split())
    if isinstance(x, list): return sum(wc(i) for i in x)
    if isinstance(x, dict): return sum(wc(v) for k, v in x.items() if k != "cit")
    return 0


for f in sorted(glob.glob(os.path.join(H, "src", "c[0-9][0-9].json"))):
    c = os.path.basename(f)[:-5]
    S = json.load(open(f, encoding="utf-8"))
    P = {k: v for k, v in S.items() if not (isinstance(v, dict) and "cit" in v)}
    json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    line = [f"{c}: units {len(P)}, words {wc(list(P.values()))}"]
    for l, T in TODO.items():
        t = {k: v for k, v in T.items() if k in S}
        json.dump(t, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        line.append(f"{l} todo {len(t)}")
    print(" · ".join(line))
