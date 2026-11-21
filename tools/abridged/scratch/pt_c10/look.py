import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
g=json.load(open('../glossary/glossary_pt.json',encoding='utf-8'))
T=json.load(open('../data/pt.json',encoding='utf-8'))
terms=sys.argv[1].split(',')
for t in terms:
    gl=[x[:2] for x in g if t.lower() in x[0].lower()][:4]
    print('G',t,gl)
for w in sys.argv[2].split(',') if len(sys.argv)>2 else []:
    hits=[(k,v) for k,v in T.items() if w in v][:3]
    for k,v in hits:
        i=v.find(w); print('T',w,k,'...'+v[max(0,i-60):i+80]+'...')
