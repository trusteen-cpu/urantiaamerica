# -*- coding: utf-8 -*-
import json, sys, re
sys.stdout.reconfigure(encoding="utf-8")
D = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\es.json", encoding="utf-8"))
T = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\es_titles.json", encoding="utf-8"))
print(type(T), list(T.items())[:3] if isinstance(T, dict) else T[:3])
for k in ["0", "1", "179", "185", "186", "189", "190", "191", "192", "193", "158", "134", "135", "141"]:
    print(k, T.get(k) if isinstance(T, dict) else None)
for pat in [r"aposento \w+ \w+", r"\w+ aparición morontial", r"aparición \w+", r"hermano Jud\w+", r"PARTE \w+", r"Parte \w+"]:
    found = {}
    for v in D.values():
        for m in re.findall(pat, v):
            found[m] = found.get(m, 0) + 1
    print(pat, sorted(found.items(), key=lambda x: -x[1])[:15])
for c in ["191:0.1", "191:1.1", "192:0.1", "0:0.1"]:
    print(c, D[c][:200])
