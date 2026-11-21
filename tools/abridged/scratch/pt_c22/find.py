import json,re,sys
d=json.load(open('../data/pt.json',encoding='utf-8'))
for w in sys.argv[1:]:
    rx=re.compile(w)
    hits=[(k,m.group(0)) for k,v in d.items() for m in rx.finditer(v)]
    from collections import Counter
    print(w, Counter(h[1] for h in hits).most_common(6), [h[0] for h in hits[:3]])
