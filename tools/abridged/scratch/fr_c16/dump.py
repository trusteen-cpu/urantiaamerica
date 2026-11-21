import json
d=json.load(open('work/src_c16.json',encoding='utf-8'))
inl=json.load(open('work/inline_fr_c16.json',encoding='utf-8'))
todo=json.load(open('work/todo_fr_c16.json',encoding='utf-8'))
hints=json.load(open('work/title_hints_fr.json',encoding='utf-8'))
out={}
for k,v in d.items():
    p=k.split('.')[0]
    s=out.setdefault(p,[])
    line=k+' '+json.dumps(v,ensure_ascii=False)
    if k in hints: line+='\n   HINT: '+hints[k]
    s.append(line)
for p,s in out.items():
    open('scratch/fr_c16/src_%s.txt'%p,'w',encoding='utf-8').write('\n'.join(s))
with open('scratch/fr_c16/inline.txt','w',encoding='utf-8') as f:
    for k,lst in inl.items():
        for x in lst:
            f.write('== %s %s\nEN: %s\n'%(k,x['cit'],x['en']))
            for vk,vv in x['verses'].items(): f.write('  %s: %s\n'%(vk,vv))
with open('scratch/fr_c16/todo.txt','w',encoding='utf-8') as f:
    for k,x in todo.items():
        f.write('== %s %s why=%s\nEN: %s\n'%(k,x['cit'],x['why'],x['en']))
        for vk,vv in x['verses'].items(): f.write('  %s: %s\n'%(vk,vv))
