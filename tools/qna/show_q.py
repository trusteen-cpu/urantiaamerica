# -*- coding: utf-8 -*-
# 번역자 도우미 (읽기만 함):
#   python show_q.py es c03          → 그 조각의 ⟦Q⟧ 인용마다: 영어 인용, 영어 절 전체, 공식 번역 절 전체, 미리 자른 공식 인용(있으면)
#   python show_q.py es term "Thought Adjuster"   → 용어집(glossary_<l>.json)에서 영어 표제어가 맞는 항목
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.normpath(os.path.join(H, "..")))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
QM = re.compile(r"⟦Q ([^⟧\s]+)⟧(.*?)⟦/Q⟧", re.S)
l, c = sys.argv[1], sys.argv[2]
if c == "term":
    G = json.load(open(os.path.join(H, "..", "glossary", f"glossary_{l}.json"), encoding="utf-8"))
    w = sys.argv[3].lower()
    for e, t, d in G:
        if w in e.lower(): print(f"{e} → {t}")
    sys.exit()
U = json.load(open(os.path.join(H, "src", "units.json"), encoding="utf-8"))
CH = json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))
QS = {(k, n): t for k, n, cit, t in json.load(open(os.path.join(H, f"quotes_{l}.json"), encoding="utf-8"))}
for k in CH[c]:
    if not k.startswith("q"): continue
    for n, m in enumerate(QM.finditer(U[k]["answer"])):
        cit, q = m.group(1), m.group(2)
        t = QS[(k, n)]
        print(f"=== {k} quotation #{n}  [{cit}]  {'PRE-CUT (already in work file, keep it)' if t else 'TO CUT BY YOU'}")
        print("EN quote :", q)
        if t: print("official :", t)
        else:
            print("EN verse :", EN[cit])
            print(f"{l} verse :", amq.text(l, cit))
        print()
