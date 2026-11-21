import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
D=json.load(open('../data/pt.json',encoding='utf-8'))
for a in sys.argv[1:]:
    if '-' in a:
        p,r=a.split(':'); s,rng=r.split('.') ; lo,hi=rng.split('-')
        for i in range(int(lo),int(hi)+1):
            k=f"{p}:{s}.{i}"; print(k, D.get(k,'')[:int(240)])
    else: print(a, D.get(a,''))
