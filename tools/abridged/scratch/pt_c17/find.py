import json,re,sys
pt=json.load(open('../data/pt.json',encoding='utf-8'))
for w in sys.argv[1:]:
    hits=[(k,v) for k,v in pt.items() if re.search(w,v)]
    print('==',w,len(hits))
    for k,v in hits[:2]:
        m=re.search(w,v); print('  ',k, v[max(0,m.start()-60):m.end()+60])
