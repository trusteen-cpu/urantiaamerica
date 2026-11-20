# -*- coding: utf-8 -*-
import json, sys
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine"
S = json.load(open(H + r"\work\src_c04.json", encoding="utf-8"))
ch = sys.argv[1]
for k, v in S.items():
    if k.startswith(ch + ":"):
        print(k, "=>", json.dumps(v, ensure_ascii=False))
