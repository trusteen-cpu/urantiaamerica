# -*- coding: utf-8 -*-
# usage: python v.py 101:6.9 101:6.10 ...   (prints official fr verses)
import sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
for r in sys.argv[1:]:
    try:
        print(r, "|", amq.text("fr", r))
    except KeyError:
        print(r, "| ?")
