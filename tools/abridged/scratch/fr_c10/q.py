import json
V=json.load(open('work/todo_fr_c10.json',encoding='utf-8'))
def cut(k,start,end):
    v=list(V[k]['verses'].values())[0]
    i=v.index(start); j=v.index(end,i)+len(end)
    return v[i:j]
Q={}
Q["71.b35.q"]=cut("71.b35.q","L’éducation, c’est","toute la vie, de")[:-4]
Q["72.b5.q"]=cut("72.b5.q","Ces gens se sont","la civilisation")
Q["73.b5.q"]=cut("73.b5.q","Éden était l’unique","d’Urantia.")
Q["73.b19.q"]=cut("73.b19.q","À l’extérieur","d’Urantia.")
Q["73.b35.q"]=cut("73.b35.q","se mobiliser","bien besoin.")
Q["74.b5.q"]=cut("74.b5.q","Allez maintenant","en vie.")
Q["74.b22.q"]=cut("74.b22.q","Que cet acte","que Dieu.")
Q["75.b5.q"]=cut("75.b5.q","la perfection est","origine.")
Q["75.b22.q"]=cut("75.b22.q","il constituait","plan divin.")
Q["76.b5.q"]=cut("76.b5.q","Ce sont les peuples","les peuples.")
Q["76.b27.q"]=cut("76.b27.q","Vous serez rappel","auparavant.")
Q["77.b42.q"]=cut("77.b42.q","Les générations","habité.")
for k,v in Q.items(): print(k,v)
assert set(Q)==set(V)
json.dump(Q,open('fr/quotes_c10.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
