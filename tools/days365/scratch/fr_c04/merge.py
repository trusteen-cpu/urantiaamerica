import json,os,importlib.util,sys
src=json.load(open('work/src_c04.json',encoding='utf-8'))
out='fr/c04.json'
D=json.load(open(out,encoding='utf-8')) if os.path.exists(out) else {}
for p in sorted(f for f in os.listdir('scratch/fr_c04') if f.startswith('p') and f.endswith('.py')):
    spec=importlib.util.spec_from_file_location(p[:-3],'scratch/fr_c04/'+p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k,u in m.T.items():
        assert len(u['msg'])==len(src[k]['msg']),(k,len(u['msg']),len(src[k]['msg']))
        D[k]={'_ref':src[k]['_ref'],'t':u['t'],'msg':u['msg'],'pr':u['pr']}
D={k:D[k] for k in src if k in D}
json.dump(D,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(D),'units')
