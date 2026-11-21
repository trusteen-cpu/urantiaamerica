import json
t=json.load(open('work/todo_pt_c20.json',encoding='utf-8'))
def cut(k, start, end):
    v=list(t[k]['verses'].values())[0]
    i=v.index(start); j=v.index(end,i)+len(end)
    return v[i:j]
Q={}
Q['150.b11.q']=cut('150.b11.q','no Reino do c','filhas de Deus')
Q['153.b5.q']=cut('153.b5.q','é o esp','vida.')
Q['154.b5.q']=cut('154.b5.q','Pois todo aquele','minha irmã')
Q['154.b13.q']=cut('154.b13.q','As situa','do espírito')
Q['154.b23.q']=cut('154.b23.q','Esse mundo nunca','ampla escala')
Q['154.b31.q']=cut('154.b31.q','Não, mais','obedecê-la')
Q['155.b5.q']=cut('155.b5.q','A religião da mente','revelação progressiva')
Q['155.b16.q']=cut('155.b16.q','a lealdade sincera','verdadeiras.')
Q['155.b25.q']=cut('155.b25.q','A religião do esp','progresso.')
assert set(Q)==set(t)
json.dump(Q,open('pt/quotes_c20.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
import sys; sys.stdout.reconfigure(encoding='utf-8')
for k,v in Q.items(): print(k,v)
