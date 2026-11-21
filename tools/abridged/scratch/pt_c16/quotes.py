import json,re
t=json.load(open('work/todo_pt_c16.json',encoding='utf-8'))
spec={
'119.b36.q':('119:8.8',r'^(.*?habitados)'),
'120.b10.q':('120:1.4',r'^“(.*?Paraíso\.)'),
'121.b5.q':('121:1.1',r'(Quando Michael.*?desde então\.)'),
'121.b31.q':('121:5.18',r'(E a essa mesma.*?Deus\.)'),
'121.b46.q':('121:8.14',r'(Na realidade.*?original\.)'),
'122.b5.q':('122:8.2',r'^(.*?nasceu o menino prometido)'),
'122.b15.q':('122:3.1',r'(este lar foi escolhido.*?predestinado\.)'),
'123.b33.q':('123:6.9',r'(eles que tanto.*?de verdade)'),
'124.b32.q':('124:6.18',r'^(.*?autoconsciente)'),
'127.b5.q':('127:6.12',r'(Está aprendendo de vagar.*?terrena\.)'),
'127.b13.q':('127:2.8',r'(o dinheiro não pode amar)'),
}
out={}
for k,(v,rx) in spec.items():
    m=re.search(rx,t[k]['verses'][v]); out[k]=m.group(1)
assert set(out)==set(t)
json.dump(out,open('pt/quotes_c16.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for k,x in out.items(): print(k,x)
