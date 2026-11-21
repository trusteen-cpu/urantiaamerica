import json, os, importlib.util, glob
B=os.path.dirname(os.path.abspath(__file__)); R=os.path.join(B,'..','..')
src=json.load(open(os.path.join(R,'work/src_c12.json'),encoding='utf-8'))
T={}
for f in sorted(glob.glob(os.path.join(B,'p*.py'))):
    s=importlib.util.spec_from_file_location('m',f); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); T.update(m.T)
out={}
for k,v in src.items():
    if k in T:
        t=T[k]
        assert type(t)==type(v),k
        if isinstance(v,list):
            assert len(t)==len(v) and all(len(a)==len(b) for a,b in zip(t,v)),('shape',k)
        out[k]=t
extra=set(T)-set(src); assert not extra,extra
json.dump(out,open(os.path.join(R,'es/c12.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('done',len(out),'of',len(src))
