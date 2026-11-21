import json,re,sys
d=json.load(open('data/es.json',encoding='utf-8'))
for pat in sys.argv[1:]:
    print('==',pat)
    n=0
    for k,v in d.items():
        for m in re.finditer(pat,v,re.I):
            print(' ',k,'…'+v[max(0,m.start()-60):m.end()+60]+'…'); n+=1; break
        if n>=3: break
