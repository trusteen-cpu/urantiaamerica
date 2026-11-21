import json,glob,importlib.util,os
B='../../'
src=json.load(open(B+'work/src_c14.json',encoding='utf-8'))
U={}
for f in sorted(glob.glob('b*.py')):
    s=importlib.util.spec_from_file_location(f[:-3],f);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);U.update(m.U)
D={k:U[k] for k in src if k in U}
for k,v in D.items():
    assert v['_ref']==src[k]['_ref'],k; assert len(v['msg'])==len(src[k]['msg']),k
json.dump(D,open(B+'fr/c14.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(D),'units written')
