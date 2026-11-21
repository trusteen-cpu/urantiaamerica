import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
D=json.load(open('data/pt.json',encoding='utf-8'))
for a in sys.argv[1:]:
    if ':' in a and a[0].isdigit():
        print(a, D.get(a)); continue
    n=0
    for k,v in D.items():
        if re.search(a,v,re.I):
            m=re.search(a,v,re.I); print(k, '...'+v[max(0,m.start()-80):m.end()+80]+'...'); n+=1
            if n>4: break
