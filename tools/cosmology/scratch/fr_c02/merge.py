import json,os,glob,importlib.util,sys
H=os.path.dirname(os.path.abspath(__file__))
src=json.load(open('work/src_c02.json',encoding='utf-8'))
out='fr/c02.json'
D=json.load(open(out,encoding='utf-8')) if os.path.exists(out) else {}
for f in sorted(glob.glob(os.path.join(H,'p*.py'))):
    s=importlib.util.spec_from_file_location('m',f);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
    for k,v in m.T.items():
        assert k in src,k
        assert type(v)==type(src[k]),k
        if isinstance(v,list): assert len(v)==len(src[k]),k
        D[k]=v
D={k:D[k] for k in src if k in D}
json.dump(D,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(D),'/',len(src),'missing',[k for k in src if k not in D][:5])
