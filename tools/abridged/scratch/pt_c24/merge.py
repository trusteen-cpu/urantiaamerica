import json,os,sys,importlib.util
B=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(B,'..','..')
src=json.load(open(os.path.join(R,'work','src_c24.json'),encoding='utf-8'))
out=os.path.join(R,'pt','c24.json')
D=json.load(open(out,encoding='utf-8')) if os.path.exists(out) else {}
for p in range(187,197):
    f=os.path.join(B,'p%d.py'%p)
    if not os.path.exists(f): continue
    spec=importlib.util.spec_from_file_location('m%d'%p,f); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k,v in m.T.items():
        assert k in src,k
        assert type(v)==type(src[k]),k
        if isinstance(v,list):
            assert len(v)==len(src[k]) and all(len(a)==len(b) for a,b in zip(v,src[k])),k
        D[k]=v
    miss=[k for k in src if k.startswith('%d.'%p) and k not in m.T]
    if miss: print('missing',p,miss)
D={k:D[k] for k in src if k in D}
json.dump(D,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(D),'/',len(src))
