import json,glob,runpy,os
src=json.load(open('work/src_c18.json',encoding='utf-8'))
D={}
for f in sorted(glob.glob('scratch/pt_c18/p1*.py')):
    D.update(runpy.run_path(f)['D'])
extra=[k for k in D if k not in src]
if extra: print('EXTRA',extra)
out={k:D[k] for k in src if k in D}
for k in out:
    if type(out[k])!=type(src[k]): print('TYPE',k)
    if isinstance(src[k],list):
        if len(src[k])!=len(out[k]) or any(len(a)!=len(b) for a,b in zip(src[k],out[k])): print('SHAPE',k)
miss=[k for k in src if k not in D]
print('done',len(out),'missing',len(miss))
json.dump(out,open('pt/c18.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
if os.path.exists('scratch/pt_c18/quotes.py'):
    Q=runpy.run_path('scratch/pt_c18/quotes.py')['Q']
    json.dump(Q,open('pt/quotes_c18.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
