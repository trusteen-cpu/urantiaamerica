import json,os
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/../..')
t=json.load(open('work/todo_fr_c12.json',encoding='utf-8'))
v=lambda k:t[k]['verses'][t[k]['cit'].split('|')[0]]
def cut(k,start,end):
    s=v(k); i=s.index(start); j=s.index(end,i)+len(end); return s[i:j]
Q={}
Q['86.b5.q']=cut('86.b5.q','Et, depuis lors','amour pour Dieu.')
Q['87.b33.q']=cut('87.b33.q','Un culte dépourvu','Un culte authentique grandit.')
Q['89.b16.q']=cut('89.b16.q','elle lui enseigna','satisfactions égoïstes.')
Q['90.b5.q']=cut('90.b5.q','La religion aboutit','amour tout-puissant')
Q['90.b19.q']=cut('90.b19.q','L’évolution parvient','concept de Dieu.')
Q['92.b14.q']=cut('92.b14.q','La conscience, non','conduite humaine.')
Q['92.b36.q']=cut('92.b36.q','mais ils peuvent','Père de tous')
Q['93.b5.q']=cut('93.b5.q','Je suis Melchizédek','unique Dieu.')
Q['93.b28.q']=cut('93.b28.q','Dieu accepte de tout faire','suivre ses instructions.')
assert set(Q)==set(t)
json.dump(Q,open('fr/quotes_c12.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k in Q: print(k,Q[k])
