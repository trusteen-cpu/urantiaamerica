import json
d=json.load(open('../data/pt.json',encoding='utf-8'))
todo=json.load(open('work/todo_pt_c22.json',encoding='utf-8'))
# (key, verse, start snippet, end snippet) -> cut d[verse] from start to end inclusive (ASCII-safe snippets via unicode escapes not needed: file is utf-8 python)
C = json.load(open('scratch/pt_c22/qspec.json',encoding='utf-8'))
Q={}
for k,(v,a,b) in C.items():
    t=d[v]; i=t.index(a); j=t.index(b,i)+len(b); Q[k]=t[i:j]
assert set(Q)==set(todo), set(todo)^set(Q)
Q={k:Q[k] for k in todo}
json.dump(Q,open('pt/quotes_c22.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in Q.items(): print(k,'|',v)
