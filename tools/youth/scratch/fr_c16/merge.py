import json,sys,glob,os,importlib.util
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('work/src_c16.json',encoding='utf-8'))
T={}
for f in sorted(glob.glob('scratch/fr_c16/part*.py')):
    sp=importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    for k in m.T:
        assert k in s,k
    T.update(m.T)
D={k:T[k] for k in s if k in T}
json.dump(D,open('fr/c16.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('units',len(D),'/',len(s))
for k in D:
    import re
    a=re.findall(r'⟦Q ([^⟧]+)⟧',s[k]); b=re.findall(r'⟦Q ([^⟧]+)⟧',D[k])
    if a!=b: print('MARKER MISMATCH',k,a,b)
