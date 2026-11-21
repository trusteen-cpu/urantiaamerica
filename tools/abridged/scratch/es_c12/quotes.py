import json
t=json.load(open('work/todo_es_c12.json',encoding='utf-8'))
def V(k): return list(t[k]['verses'].values())[0]
def cut(k,a,b=None):
    v=V(k); i=v.index(a); j=v.index(b,i)+len(b) if b else len(v)
    return v[i:j]
Q={}
Q['86.b5.q']=cut('86.b5.q','Y los Ajustadores divinos','amor a Dios.')
Q['89.b16.q']=cut('89.b16.q','le ense','egoístas.'.encode('ascii','ignore').decode() or 'x') if False else None
v=V('89.b16.q'); Q['89.b16.q']=v[v.index('; le ense')+2:]
v=V('90.b5.q'); i=v.index('La religión finalmente'.replace('ó','ó')) if False else v.index('finalmente alcanza')-len('La religión '); Q['90.b5.q']=v[i:v.index(', el amor que inunda')]
v=V('90.b19.q'); Q['90.b19.q']=v[:v.index('Dios.')+5]
v=V('92.b36.q'); i=v.index('pero s'); Q['92.b36.q']=v[i:v.index(', porque esto')]
v=V('93.b5.q'); i=v.index('«Soy'); Q['93.b5.q']=v[i+1:v.index('»',i)]
v=V('93.b28.q'); i=v.index('Dios acuerda hacer'); Q['93.b28.q']=v[i:v.index('. Hasta ese')+1]
for k,x in Q.items(): print(k,'|',x)
json.dump(Q,open('es/quotes_c12.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
