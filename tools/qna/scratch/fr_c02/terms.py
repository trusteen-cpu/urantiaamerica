# -*- coding: utf-8 -*-
import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
G = json.load(open(os.path.join(H, "..", "..", "..", "glossary", "glossary_fr.json"), encoding="utf-8"))
for w in sys.argv[1:]:
    hits = [f"{e} → {t}" for e, t, d in G if w.lower() in e.lower()]
    print(f"[{w}]", " | ".join(hits[:6]) or "-")
