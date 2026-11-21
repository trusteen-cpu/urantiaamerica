import json
t=json.load(open('work/todo_pt_c19.json',encoding='utf-8'))
def cut(k, start, end):
    v=list(t[k]['verses'].values())[0]
    i=v.index(start); j=v.index(end,i)+len(end)
    return v[i:j]
Q={}
Q['142.b14.q']=cut('142.b14.q','um pai bom e verdadeiro','seus membros individuais')
Q['142.b26.q']=cut('142.b26.q','todo aquele que houver','vitória da vossa própria fé.')
Q['144.b14.q']=cut('144.b14.q','A prece é o respirar','vontade do Pai.')
Q['144.b37.q']=cut('144.b37.q','entre aqueles nascidos','é ainda maior')
Q['145.b32.q']=cut('145.b32.q','o Reino do Pai não podia','curas físicas')
Q['146.b17.q']=cut('146.b17.q','a intolerância é uma máscara','própria crença.')
Q['147.b28.q']=cut('147.b28.q','o sábado foi feito para o homem','para o sábado.')
Q['148.b5.q']=cut('148.b5.q','Deus reside dentro de ti','que Ele é')
Q['148.b44.q']=cut('148.b44.q','O Pai no céu não aflige','próprio desejo.')
Q['149.b35.q']=cut('149.b35.q','Eu vim ao mundo','no lugar do receio')
Q['149.b44.q']=cut('149.b44.q','é exatamente tal mudança','sobre a Terra.')
assert set(Q)==set(t)
json.dump(Q,open('pt/quotes_c19.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,v in Q.items(): print(k,v)
