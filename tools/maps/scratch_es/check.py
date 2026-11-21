# -*- coding: utf-8 -*-
import json, sys, re
sys.stdout.reconfigure(encoding="utf-8")
D = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\es.json", encoding="utf-8"))
T = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\es_titles.json", encoding="utf-8"))
allt = "\n".join(D.values())
words = sys.argv[1:]
for w in words:
    n = len(re.findall(re.escape(w), allt))
    ex = [k for k, v in D.items() if w in v][:3]
    print(f"{w!r}: {n} {ex}")
