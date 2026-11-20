import json, re, sys
V = json.load(open('../data/es.json', encoding='utf-8'))
words = sys.argv[1:]
out = open('scratch/es_c06/find.txt', 'w', encoding='utf-8')
for w in words:
    hits = [(k, t) for k, t in V.items() if re.search(w, t)]
    out.write(f"== {w}: {len(hits)}\n")
    for k, t in hits[:3]:
        m = re.search(w, t)
        out.write(f"  {k}: ...{t[max(0,m.start()-60):m.end()+60]}...\n")
