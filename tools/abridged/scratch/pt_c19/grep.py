import json,re,sys
d=json.load(open('../data/pt.json',encoding='utf-8'))
for w in sys.argv[1:]:
    rx=re.compile(w)
    hits={}
    for k,v in d.items():
        p=int(k.split(':')[0])
        if not (128<=p<=196): continue
        for m in rx.finditer(v):
            s=v[max(0,m.start()-25):m.end()+25]
            hits.setdefault(m.group(0),[]).append(k)
    print(w, {a:(len(b),b[:2]) for a,b in hits.items()})
