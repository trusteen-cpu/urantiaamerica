import json,sys,io,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
D=json.load(open('../data/pt.json',encoding='utf-8'))
pat=re.compile(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 5
c=0
for k,v in D.items():
    for m in pat.finditer(v):
        print(k, '...'+v[max(0,m.start()-60):m.end()+60]+'...'); c+=1; break
    if c>=n: break
