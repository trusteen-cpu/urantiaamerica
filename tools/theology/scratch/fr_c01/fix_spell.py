# -*- coding: utf-8 -*-
import json, os, re, glob
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"


def fx(s):
    s = re.sub(r"\bcroit\b", "croît", s)  # all uses in c01 prose are croître
    s = s.replace("sûre", "sure")
    return s


p = os.path.join(H, "fr", "c01.json")
D = json.load(open(p, encoding="utf-8"))
D = {k: fx(v) for k, v in D.items()}
json.dump(D, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for f in glob.glob(os.path.join(H, "scratch", "fr_c01", "t_ch*.py")):
    t = open(f, encoding="utf-8").read()
    open(f, "w", encoding="utf-8").write(fx(t))
print("ok")
