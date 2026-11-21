import json,glob,importlib.util,os
s=json.load(open('work/src_c12.json',encoding='utf-8'))
A={}
for f in sorted(glob.glob('scratch/es_c12/part*.py')):
    sp=importlib.util.spec_from_file_location('m',f);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);A.update(m.D)
bad=[k for k in A if k not in s]
out={k:A[k] for k in s if k in A}
json.dump(out,open('es/c12.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('done',len(out),'of',len(s),'extra',bad)
