# -*- coding: utf-8 -*-
# 번역 참고: 목록 하나(또는 여러 개)의 영어 원고 단위 + 그 목록이 다루는 절의 영어·공식 번역 본문을 나란히 보인다.
#   python show_src.py es 45            (목록 45)
#   python show_src.py fr 45-50         (목록 45~50)
#   python show_src.py pt 7:4.4         (절 하나)
import json, os, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
REFS = json.load(open(os.path.join(H, "src", "refs.json"), encoding="utf-8"))
SRC = {}
for p in sorted(glob.glob(os.path.join(H, "src", "c[0-9][0-9].json"))):
    SRC.update(json.load(open(p, encoding="utf-8")))
l = sys.argv[1]
T = amq._load(l)
for a in sys.argv[2:]:
    if ":" in a:
        print("[%s] %s\n[%s %s] %s\n" % (a, EN.get(a, "-"), l, a, T.get(a, "-"))); continue
    lo, _, hi = a.partition("-")
    for n in range(int(lo), int(hi or lo) + 1):
        k = "L%03d" % n
        print("=" * 20, k, REFS[k]["ref"])
        print(json.dumps(SRC[k], ensure_ascii=False))
        for p in REFS[k]["src"]:
            print("[%s] %s\n[%s %s] %s" % (p, EN.get(p, "-"), l, p, T.get(p, "-")))
        print()
