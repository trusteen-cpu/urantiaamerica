import json
t=json.load(open('work/todo_fr_c13.json',encoding='utf-8'))
def v(k,c): return t[k]['verses'][c]
def between(s,a,b):
    i=s.index(a); j=s.index(b,i)+len(b); return s[i:j]
Q={}
Q['94.b29.q']=between(v('94.b29.q','94:6.6'),'La Déité Absolue','désirs sincères')
Q['95.b10.q']=between(v('95.b10.q','95:1.8'),'Mais l’erreur','révolution soudaine.')
Q['95.b34.q']=between(v('95.b34.q','95:7.6'),'Là où trois','une quatrième')
Q['96.b5.q']=between(v('96.b5.q','96:4.9'),'Le trait','concept de la Déité')
Q['96.b20.q']=between(v('96.b20.q','96:4.6'),'Le Dieu éternel','bras éternels.')
Q['96.b33.q']=between(v('96.b33.q','96:7.7'),'Il priera','divine droiture.')
Q['97.b5.q']=between(v('97.b5.q','97:7.9'),'Dieu n’oublierait','abandonnerait pas.')
Q['97.b10.q']=between(v('97.b10.q','97:1.4'),'La Force d','se repentir.')
Q['97.b25.q']=between(v('97.b25.q','97:5.6'),'Il m’a montré','avec ton Dieu.')
Q['98.b5.q']=between(v('98.b5.q','98:2.8'),'En Grèce','à la croyance.')
Q['98.b37.q']=between(v('98.b37.q','98:7.11'),'Il a cessé','à propos de Jésus')
Q['99.b26.q']=between(v('99.b26.q','99:5.2'),'la vraie religion','comme votre frère.')
Q['100.b15.q']=between(v('100.b15.q','100:2.7'),'Les sécurités temporelles','sont invulnérables.')
Q['101.b9.q']=between(v('101.b9.q','101:1.3'),'Ce sont vos pensées','vers Dieu.')
Q['101.b48.q']=between(v('101.b48.q','101:10.9'),'Le temps lui-même','de l’espace.')
assert set(Q)==set(t)
json.dump(Q,open('fr/quotes_c13.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,x in Q.items(): print(k,x)
