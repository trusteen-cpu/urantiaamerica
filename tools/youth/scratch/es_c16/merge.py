import json,glob,importlib.util,os
B=os.path.dirname(os.path.abspath(__file__))
src=json.load(open('work/src_c16.json',encoding='utf-8'))
T={}
for f in sorted(glob.glob(B+'/p1*.py')):
    s=importlib.util.spec_from_file_location('m',f); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)
    T.update(m.T)
out={k:T[k] for k in src if k in T}
extra=[k for k in T if k not in src]
print('units',len(out),'/',len(src),'extra',extra)
json.dump(out,open('es/c16.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
