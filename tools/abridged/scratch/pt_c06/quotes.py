import json
t=json.load(open('work/todo_pt_c06.json',encoding='utf-8'))
def cut(key,start,end=None,inc=True):
    v=list(t[key]['verses'].values())[0]
    i=v.index(start); j=len(v) if end is None else v.index(end,i)+(len(end) if inc else 0)
    return v[i:j]
Q={}
Q['43.b21.q']=cut('43.b21.q','As portas dos cora','reunidos')
Q['44.b37.q']=cut('44.b37.q','a verdadeira alma','filósofo.')
Q['46.b5.q']=cut('46.b5.q','E Jerusém é apenas')
Q['48.b31.q']=cut('48.b31.q','nenhum ato de bondade','totalmente',)
for k,v in Q.items(): print(k,v)
json.dump(Q,open('pt/quotes_c06.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
