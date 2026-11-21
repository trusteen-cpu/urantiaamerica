import json
t=json.load(open('work/todo_fr_c07.json',encoding='utf-8'))
def V(k): return list(t[k]['verses'].values())[0]
def between(k,a,b):
    s=V(k); i=s.index(a); j=s.index(b,i)+len(b); return s[i:j]
Q={}
Q['50.b35.q']=between('50.b35.q','agondontaires, qui','sont seuls.')
Q['51.b5.q']=between('51.b5.q','Chez ces immortels','relie Dieu à l’homme')
Q['51.b35.q']=between('51.b35.q','Si les Urantiens','rébellion.')
Q['52.b25.q']=between('52.b25.q','Sa vie est','seront libres.')
Q['52.b34.q']=between('52.b34.q','tôt ou tard','lumière et de vie.')
Q['53.b5.q']=between('53.b5.q','la foi est une armure','iniquité.')
Q['53.b21.q']=between('53.b21.q','gouvernement des Fils','sophismes')
Q['53.b36.q']=between('53.b36.q','quiconque est né','touche pas')
Q['54.b5.q']=between('54.b5.q','Dans un univers dominé','certaine.')
Q['54.b30.q']=between('54.b30.q','Aucune de ces','atteindre Dieu.')
Q['55.b47.q']=between('55.b47.q','Jésus de Nazareth','dix-neuf-cents ans.')
assert set(Q)==set(t)
json.dump(Q,open('fr/quotes_c07.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok')
