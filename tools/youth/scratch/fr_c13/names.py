import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
fr = json.load(open('../data/fr.json', encoding='utf-8'))
pats = sys.argv[1:]
for p in pats:
    rx = re.compile(p)
    hits = {}
    for k, v in fr.items():
        for m in rx.finditer(v):
            s = v[max(0, m.start()-15):m.end()+15]
            hits.setdefault(m.group(0), (k, s))
    print('==', p)
    for w, (k, s) in list(hits.items())[:6]:
        print('  ', w, '|', k, '|', s)
