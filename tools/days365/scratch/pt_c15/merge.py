import json,sys,os,glob,importlib.util
sys.stdout.reconfigure(encoding='utf-8')
here=os.path.dirname(os.path.abspath(__file__))
S=json.load(open('work/src_c15.json',encoding='utf-8'))
T={}
for f in sorted(glob.glob(os.path.join(here,'p*.py'))):
    sp=importlib.util.spec_from_file_location(os.path.basename(f)[:-3],f);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);T.update(m.D)
out={}
for k,u in S.items():
    if k in T:
        t=T[k]; assert len(t['msg'])==len(u['msg']),(k,len(t['msg']),len(u['msg']))
        out[k]={'_ref':u['_ref'],'t':t['t'],'msg':t['msg'],'pr':t['pr']}
json.dump(out,open('pt/c15.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('units',len(out))
