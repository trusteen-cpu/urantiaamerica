import json,sys,re
d=json.load(open('../data/fr.json',encoding='utf-8'))
pre=sys.argv[1]
for w in sys.argv[2:]:
    n=0
    for k,v in d.items():
        if pre and not k.startswith(pre): continue
        for m in re.finditer(w,v):
            print(k,w,'::',v[max(0,m.start()-60):m.end()+60].replace('\n',' ')); n+=1
            if n>=3: break
        if n>=3: break
