import json,os,importlib.util,glob
here=os.path.dirname(os.path.abspath(__file__))
src=json.load(open('work/src_c19.json',encoding='utf-8'))
T={}
for f in sorted(glob.glob(os.path.join(here,'p1*.py'))):
    spec=importlib.util.spec_from_file_location('m',f); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    T.update(m.D)
extra=set(T)-set(src); assert not extra, extra
out={k:T[k] for k in src if k in T}
for k in out:
    a,b=src[k],out[k]
    assert type(a)==type(b),k
    if isinstance(a,list):
        assert len(a)==len(b) and all(len(x)==len(y) for x,y in zip(a,b)),k
json.dump(out,open('pt/c19.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(out),'of',len(src),'missing:',[k for k in src if k not in T][:5])
