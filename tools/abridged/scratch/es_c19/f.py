import json,sys,re
V=json.load(open('../data/es.json',encoding='utf-8'))
args=sys.argv[1:]
pref=None
if args and args[0].startswith('P='): pref=args[0][2:].split(','); args=args[1:]
for w in args:
    w=w.encode('ascii').decode('unicode_escape')
    hits=[(k,v) for k,v in V.items() if re.search(w,v,re.I) and (not pref or k.split(':')[0] in pref)]
    print('==',w,len(hits))
    for k,v in hits[:4]:
        m=re.search(w,v,re.I); print(' ',k,'...'+v[max(0,m.start()-80):m.end()+80]+'...')
