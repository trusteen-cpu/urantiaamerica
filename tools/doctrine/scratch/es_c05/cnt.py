import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "data", "es.json")
es = json.load(open(base, encoding="utf-8"))
for w in sys.argv[1:]:
    w = w.replace("_", " ")
    hits = [k for k, v in es.items() if w.lower() in v.lower()]
    print(w, len(hits), hits[:6])
