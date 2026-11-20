# -*- coding: utf-8 -*-
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(H, "..", "..", "..", "glossary", "glossary_es.json"), encoding="utf-8"))
for w in sys.argv[1:]:
    w = w.lower()
    for e, t, d in G:
        if w in e.lower():
            print(f"{e} => {t}")
