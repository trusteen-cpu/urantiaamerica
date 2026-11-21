import json,glob,os,importlib.util,sys
sys.stdout.reconfigure(encoding='utf-8')
src=json.load(open('work/src_c13.json',encoding='utf-8'))
out='pt/c13.json'
D=json.load(open(out,encoding='utf-8')) if os.path.exists(out) else {}
for f in sorted(glob.glob('scratch/pt_c13/part_*.py')):
    sp=importlib.util.spec_from_file_location('m',f); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    for k,v in m.U.items():
        assert len(v['msg'])==len(src[k]['msg']),(k,len(v['msg']),len(src[k]['msg']))
        D[k]={'_ref':src[k]['_ref'],'t':v['t'],'msg':v['msg'],'pr':v['pr']}
R={k:D[k] for k in src if k in D}
json.dump(R,open(out,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('units',len(R),'/',len(src))
