# -*- coding: utf-8 -*-
# 인용 보기 (읽기 전용):  python show_q.py <l> cNN [키 앞부분 예: ch03.s2]
#   인용마다: 키·절 번호, 영어 인용, 공식 번역 인용(자동/손으로 자른 것) 또는 TO CUT BY YOU + 영어 절 전체 + 공식 번역 절 전체.
#   python show_q.py <l> todo cNN   → 손으로 잘라야 할 인용만
#   python show_q.py <l> term "Adjuster"   → 용어집(../glossary/glossary_<l>.json) 찾기
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

l = sys.argv[1]
if sys.argv[2] == "term":
    w = sys.argv[3].lower()
    for e, t, d in json.load(open(os.path.join(H, "..", "glossary", f"glossary_{l}.json"), encoding="utf-8")):
        if w in e.lower() or w in t.lower(): print(f"{e}  →  {t}   | {d[:120]}")
    raise SystemExit
only_todo = sys.argv[2] == "todo"
c = sys.argv[3] if only_todo else sys.argv[2]
pre = sys.argv[3] if len(sys.argv) > 3 and not only_todo else ""
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
AUTO = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
mp = os.path.join(H, l, f"quotes_{c}.json")
MAN = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
for k, v in S.items():
    if not isinstance(v, dict) or not k.startswith(pre): continue
    refs = v["cit"] if isinstance(v["cit"], list) else [v["cit"]]
    for i, (r, t) in enumerate(zip(refs, v["text"])):
        key = f"{k}#{i}"
        if key in MAN: off, tag = MAN[key], "CUT (yours)"
        elif key in AUTO: off, tag = AUTO[key], "auto"
        else: off, tag = None, "TO CUT BY YOU"
        if only_todo and key in AUTO: continue
        print(f"=== {key}  [{r}]  {tag}" + ("  (whole verse)" if v["whole"] else ""))
        print("EN quote :", t)
        if off is not None:
            print(f"{l.upper()} quote :", off)
            if tag.startswith("CUT"): print("   check:", "OK" if amq.check(l, r, off) else "NOT VERBATIM")
        if off is None or tag.startswith("CUT"):
            print("EN verse :", EN[r])
            print(f"{l.upper()} verse :", amq.text(l, r))
        print()
