import json,sys
s=json.load(open('work/src_c22.json',encoding='utf-8'))
inl=json.load(open('work/inline_pt_c22.json',encoding='utf-8'))
out=open('scratch/pt_c22/dump.txt','w',encoding='utf-8')
for k,v in s.items():
    out.write('## '+k+'\n'+json.dumps(v,ensure_ascii=False)+'\n')
    if k in inl:
        for q in inl[k]:
            out.write('   >> cit=%s auto=%s\n'%(q['cit'],q['auto']))
            if not q['auto']:
                for vk,vt in q['verses'].items(): out.write('      [%s] %s\n'%(vk,vt))
out.close()
t=json.load(open('work/todo_pt_c22.json',encoding='utf-8'))
o=open('scratch/pt_c22/todo.txt','w',encoding='utf-8')
for k,q in t.items():
    o.write('## %s cit=%s why=%s\nEN: %s\n'%(k,q['cit'],q['why'],q['en']))
    for vk,vt in q['verses'].items(): o.write('   [%s] %s\n'%(vk,vt))
o.close()
