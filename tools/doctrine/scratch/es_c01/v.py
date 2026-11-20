import json, sys
es = json.load(open("../data/es.json", encoding="utf-8"))
for r in sys.argv[1:]:
    print("[" + r + "]", es.get(r))
    print()
