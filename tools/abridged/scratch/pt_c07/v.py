import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
D=json.load(open('../data/pt.json',encoding='utf-8'))
for a in sys.argv[1:]:
    if a.startswith('?'):
        pat=a[1:]; n=0
        for k,v in D.items():
            for m in re.finditer(pat,v):
                print(k,'…',v[max(0,m.start()-60):m.end()+60]); n+=1
                break
            if n>=8: break
    else: print(a,D.get(a))
