import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
AB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
s = json.load(open(os.path.join(AB, "work", "src_c12.json"), encoding="utf-8"))
h = json.load(open(os.path.join(AB, "work", "title_hints_pt.json"), encoding="utf-8"))
p = sys.argv[1]
for k, v in s.items():
    if k.split(".")[0] == p:
        print(k, json.dumps(v, ensure_ascii=False))
        if k in h: print("   HINT:", h[k])
