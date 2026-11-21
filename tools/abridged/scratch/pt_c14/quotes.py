import json
t=json.load(open('work/todo_pt_c14.json',encoding='utf-8'))
def cut(k,start,end=None):
    v=list(t[k]['verses'].values())[0]
    i=v.index(start)
    if end is None: return v[i:]
    j=v.index(end,i)+len(end); return v[i:j]
Q={}
Q['102.b5.q']=cut('102.b5.q','as coisas humanas','para que sejam conhecidas')
Q['103.b43.q']=cut('103.b43.q','Quando a teologia','coisa viva.')
Q['105.b5.q']=cut('105.b5.q','E o rosto que')
Q['107.b5.q']=cut('107.b5.q','O Ajustador \u00e9, para','de Deus.')
Q['107.b10.q']=cut('107.b10.q','eles s\u00e3o de Deus','Deus.')
Q['108.b31.q']=cut('108.b31.q','Os Ajustadores s\u00e3o os ancestrais','evolucion\u00e1rias')
Q['109.b30.q']=cut('109.b30.q','Essa consagra','divina.')
assert list(Q)==list(t) or set(Q)==set(t)
json.dump({k:Q[k] for k in t},open('pt/quotes_c14.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in Q.items(): print(k,v)
