import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
s=json.load(open('work/src_c18.json',encoding='utf-8'))
th=json.load(open('work/title_hints_es.json',encoding='utf-8'))
inl=json.load(open('work/inline_es_c18.json',encoding='utf-8'))
todo=json.load(open('work/todo_es_c18.json',encoding='utf-8'))
with open('scratch/es_c18/src.txt','w',encoding='utf-8') as f:
    for k,v in s.items():
        f.write(k+' '+json.dumps(v,ensure_ascii=False)+'\n')
        if k in th: f.write('   HINT '+th[k]+'\n')
        if k in inl:
            for x in inl[k]:
                f.write('   INL '+json.dumps(x,ensure_ascii=False)+'\n')
with open('scratch/es_c18/todo.txt','w',encoding='utf-8') as f:
    for k,v in todo.items(): f.write(k+' '+json.dumps(v,ensure_ascii=False,indent=0)+'\n\n')
