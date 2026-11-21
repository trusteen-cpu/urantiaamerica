import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
d=json.load(open('work/src_c06.json',encoding='utf-8'))
inl=json.load(open('work/inline_es_c06.json',encoding='utf-8'))
with open('scratch/es_c06/src.txt','w',encoding='utf-8') as f:
    for k,v in d.items():
        f.write(k+' '+json.dumps(v,ensure_ascii=False)+'\n')
        for x in inl.get(k,[]):
            f.write('   INLINE cit=%s auto=%s\n'%(x['cit'],x['auto']))
            if not x['auto']:
                f.write('     en=%s\n'%x['en'])
                for vk,vv in x['verses'].items(): f.write('     %s: %s\n'%(vk,vv))
