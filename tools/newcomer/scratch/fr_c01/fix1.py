# -*- coding: utf-8 -*-
import json, glob, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
here = os.path.dirname(os.path.abspath(__file__))
for p in glob.glob(os.path.join(here, "p*.py")):
    s = open(p, encoding="utf-8").read()
    if "sûrement" in s:
        open(p, "w", encoding="utf-8").write(s.replace("sûrement", "surement")); print("fixed", p)
O = os.path.join(H, "fr", "c01.json")
d = json.load(open(O, encoding="utf-8"))
d = json.loads(json.dumps(d, ensure_ascii=False).replace("sûrement", "surement"))
json.dump(d, open(O, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
