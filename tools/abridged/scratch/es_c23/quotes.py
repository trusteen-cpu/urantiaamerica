import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
todo=json.load(open('work/todo_es_c23.json',encoding='utf-8'))
data=json.load(open('../data/es.json',encoding='utf-8')) if os.path.exists('../data/es.json') else None
# (key, verse, start phrase, end phrase) - cut from official verse
spec={
"177.b5.q":("177:1.3","Hasta un mancebo","del Dios de un universo"),
"177.b25.q":("177:4.10","Judas ansiaba","con todo su coraz"),
"178.b14.q":("178:1.15","es como la semilla del ser vivo","en nuevas manifestaciones"),
"178.b26.q":("178:3.2","Así como el Padre me envió","que he comenzado."),
"180.b32.q":("180:6.2","Es realmente beneficioso","el nuevo maestro."),
"181.b10.q":("181:1.6","En este mundo tendréis","al servicio sempiterno"),
"181.b20.q":("181:2.25","Vosotros no sois sino finitos","Sed pacientes y valerosos"),
"182.b25.q":("182:3.11","el espíritu había triunfado","a la duda incierta."),
"183.b11.q":("183:1.1","Estas experiencias inhumanas","voluntad divina del Padre"),
"185.b5.q":("185:3.4","mi reino es la familia","que está en el cielo."),
"185.b31.q":("185:7.2","Ninguna autoridad","dada de arriba."),
}
Q={}
for k,(v,a,b) in spec.items():
    t=todo[k]['verses'][v]
    i=t.index(a); j=t.index(b,i)+len(b)
    if b=="con todo su coraz": j=t.index("corazón",i)+len("corazón")
    Q[k]=t[i:j]
assert set(Q)==set(todo)
json.dump(Q,open('es/quotes_c23.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(Q))
