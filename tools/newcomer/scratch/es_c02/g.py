import json, sys
g = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\glossary\glossary_es.json", encoding="utf-8"))
for q in sys.argv[1:]:
    hits = [x for x in g if q.lower() in x[0].lower()]
    for h in hits[:6]:
        print(q, "=>", h[0], "|", h[1], "|", h[2][:70])
    if not hits:
        print(q, "=> (none)")
