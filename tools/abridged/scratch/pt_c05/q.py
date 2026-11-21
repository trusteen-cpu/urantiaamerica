import json
t=json.load(open('work/todo_pt_c05.json',encoding='utf-8'))
cuts={
'34.b38.q':('34:7.8','em todas as horas escuras',None),
'36.b5.q':('36:6.7','a concepção é inerente',None),
'37.b17.q':('37:3.4','Isso, sem dúvida',None),
'37.b28.q':('37:6.3','tal é a tônica','esclarecida.'),
'38.b14.q':('38:2.5','Vós fazeis bem','de culto.'),
'39.b40.q':('39:9.3','esses ministros espirituais',None),
'40.b5.q':('40:10.13','A suprema relação',None),
'40.b22.q':('40:5.19','Todas as almas','perfeição divina'),
'40.b39.q':('40:10.13','O Pai ama','eterna e única'),
}
out={}
for k,(v,a,b) in cuts.items():
    s=t[k]['verses'][v]; i=s.index(a)
    j=len(s) if b is None else s.index(b,i)+len(b)
    out[k]=s[i:j]
json.dump(out,open('pt/quotes_c05.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
