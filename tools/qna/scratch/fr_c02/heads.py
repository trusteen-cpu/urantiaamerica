# -*- coding: utf-8 -*-
import json, sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(H, "..", "..", "..", "data", "fr.json"), encoding="utf-8"))
papers = sys.argv[1].split(",")
n = int(sys.argv[2]) if len(sys.argv) > 2 else 90
for k, v in D.items():
    if k.split(":")[0] in papers and re.match(r"\s*\d+\.", v):
        print(k, v[:n])
