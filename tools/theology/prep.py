# -*- coding: utf-8 -*-
# 도우미용 작업 파일 만들기 (한 번 돌린다; 원고가 바뀌면 다시)
#   work/src_cNN.json        번역할 영어 글 단위(인용·ui.* 제외) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json   자동으로 못 맞춘 인용: {"키#번째": {"cit", "en"(영어 인용), "why"}}
import glob, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(H, "work"), exist_ok=True)
TODO = {l: json.load(open(os.path.join(H, f"todo_{l}.json"), encoding="utf-8")) for l in ("es", "fr", "pt")}
for f in sorted(glob.glob(os.path.join(H, "src", "c[0-9][0-9].json"))):
    c = os.path.basename(f)[:-5]
    S = json.load(open(f, encoding="utf-8"))
    P = {k: v for k, v in S.items() if isinstance(v, str) and not k.startswith("ui.")}
    json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    line = [f"{c}: prose units {len(P)}, words {sum(len(v.split()) for v in P.values())}"]
    for l, T in TODO.items():
        t = {k: v for k, v in T.items() if k.split("#")[0] in S}
        json.dump(t, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        line.append(f"{l} todo {len(t)}")
    print(" · ".join(line))
