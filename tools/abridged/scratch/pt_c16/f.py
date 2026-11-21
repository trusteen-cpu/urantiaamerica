import json,sys,re
d=json.load(open('../data/pt.json',encoding='utf-8'))
rx=re.compile(sys.argv[1]); n=int(sys.argv[2]) if len(sys.argv)>2 else 4
c=0
for k,v in d.items():
    for m in rx.finditer(v):
        print(k,'|',v[max(0,m.start()-60):m.end()+60]); c+=1; break
    if c>=n: break
