import json
d=json.load(open('../data/pt.json',encoding='utf-8'))
def cut(v,a,b=None):
    s=d[v]; i=s.index(a)
    if b is None: return a
    j=s.index(b,i)+len(b); return s[i:j]
Q={}
Q["187.b5.q"]=cut("187:2.4","As idéias, os motivos","em uma crise.")
Q["187.b13.q"]=cut("187:2.4","Pai, perdoa-lhes","o que fazem")
Q["187.b28.q"]=cut("187:5.6","Depois de uma vida assim","“Está acabado”.")
Q["190.b19.q"]=cut("190:3.1","não vos esqueçais de ministrar","confins da Terra")
Q["191.b5.q"]=cut("191:5.3","quanto a mim, quero a vida","irmãos na carne")
Q["191.b10.q"]=cut("191:1.2","Eu sabia que não era de coração","antes mesmo de me pedires")
Q["192.b5.q"]=cut("192:2.13","Nada que um filho de Deus faça","pode ser comum.")
Q["192.b15.q"]=cut("192:2.1","O amor é o ancestral","verdadeiro e belo")
Q["192.b25.q"]=cut("192:4.8","os seus bem-intencionados representantes","religião sobre Jesus.")
Q["193.b5.q"]=cut("193:0.4","A vossa mensagem não mudou","evangelho do Reino.")
Q["193.b21.q"]=cut("193:4.13","na vida, ele ignorar","ficar sem amigos.")
Q["194.b5.q"]=cut("194:3.13","Até Pentecostes","que também busca o homem")
Q["195.b27.q"]=cut("195:5.12","lembrai-vos de que as manchas","do bem último.")
Q["195.b33.q"]=cut("195:6.16","uma vez que vós começais","já vos encontrou.")
Q["196.b5.q"]=cut("196:0.13","Jesus não exige","acreditem junto com ele")
t=json.load(open('work/todo_pt_c24.json',encoding='utf-8'))
assert set(t)==set(Q)
Q={k:Q[k] for k in t}
json.dump(Q,open('pt/quotes_c24.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in Q.items(): print(k,v)
