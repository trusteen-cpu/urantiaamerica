# -*- coding: utf-8 -*-
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(H, "..", "..", "work", "src_c02.json"), encoding="utf-8"))
ch = sys.argv[1]
for k, v in S.items():
    if not k.startswith(ch + ":"):
        continue
    if isinstance(v, str):
        print(f"[{k}] {v}")
    elif "cap" in v:
        print(f"[{k}] TABLE {v['cap']}")
        for r in v["rows"]:
            print("   | " + " | ".join(r))
    else:
        print(f"[{k}] BOX {v['title']}")
        for it in v["items"]:
            print("   - " + it)
