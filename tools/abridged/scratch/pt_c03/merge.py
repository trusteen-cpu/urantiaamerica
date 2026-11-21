import json,glob,os,runpy
B='E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/abridged/'
s=json.load(open(B+'work/src_c03.json',encoding='utf-8'))
D={}
for f in sorted(glob.glob(B+'scratch/pt_c03/p[0-9][0-9].py')):
    D.update(runpy.run_path(f)['D'])
out={k:D[k] for k in s if k in D}
extra=[k for k in D if k not in s]
print('have',len(out),'of',len(s),'extra',extra)
for k in out:
    a,b=s[k],out[k]
    if type(a)!=type(b): print('TYPE',k)
    elif isinstance(a,list):
        if len(a)!=len(b) or any(len(x)!=len(y) for x,y in zip(a,b)): print('SHAPE',k)
json.dump(out,open(B+'pt/c03.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
qf=B+'scratch/pt_c03/quotes.py'
if os.path.exists(qf):
    Q=runpy.run_path(qf)['Q']
    json.dump(Q,open(B+'pt/quotes_c03.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
