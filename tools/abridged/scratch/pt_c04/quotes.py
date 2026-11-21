import json,io,os
D=json.load(io.open('../../../data/pt.json',encoding='utf-8'))
def cut(ref,start,end_incl):
    v=D[ref]; i=v.index(start); j=v.index(end_incl,i)+len(end_incl); return v[i:j]
Q={
"27.b33.q": cut("27:7.7","Que frutifica","Pai Criador!"),
"29.b5.q": cut("29:3.5","nunca, sequer","do tempo e do espaço."),
"30.b11.q": cut("30:1.99","Deus, enquanto suprapessoa","fragmenta-se"),
"32.b5.q": cut("32:4.12","Deus deu-Se","como Ele"),
"32.b21.q": cut("32:3.6","aquele que houver visto","terá visto o Pai."),
"32.b33.q": cut("32:5.8","A meta da eternidade","está em curso!"),
}
t=json.load(io.open('../../work/todo_pt_c04.json',encoding='utf-8'))
assert set(t)==set(Q)
Q={k:Q[k] for k in t}
json.dump(Q,io.open('../../pt/quotes_c04.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in Q.items(): print(k, v.encode('ascii','replace').decode())
