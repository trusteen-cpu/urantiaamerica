import json,sys,os,importlib.util
sys.stdout.reconfigure(encoding='utf-8')
H=os.path.dirname(os.path.abspath(__file__))
src=json.load(open('work/src_c07.json',encoding='utf-8'))
A={}
for n in range(49,56):
    f=os.path.join(H,f'p{n}.py')
    if os.path.exists(f):
        sp=importlib.util.spec_from_file_location(f'p{n}',f); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); A.update(m.D)
extra=[k for k in A if k not in src]
if extra: print('EXTRA',extra)
out={k:A[k] for k in src if k in A}
for k in out:
    if type(out[k])!=type(src[k]): print('TYPE',k)
    if isinstance(src[k],list):
        if len(src[k])!=len(out[k]) or any(len(a)!=len(b) for a,b in zip(src[k],out[k])): print('SHAPE',k)
print('have',len(out),'of',len(src))
json.dump(out,open('pt/c07.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
