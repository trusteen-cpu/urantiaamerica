import json, os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
todo = json.load(open(os.path.join(B, 'work', 'todo_es_c11.json'), encoding='utf-8'))
cuts = {
 "78.b5.q": ("78:8.12", "mucho antes de que los jinetes", "civilizaci\u00f3n del siglo veinte de Urantia."),
 "79.b5.q": ("79:4.9", "la religi\u00f3n, la verdadera", "basada en la fraternidad humana."),
 "79.b20.q": ("79:4.8", "alg\u00fan d\u00eda surgir\u00e1", "en b\u00fasqueda del Dios viviente"),
 "79.b30.q": ("79:6.10", "El est\u00edmulo de una religi\u00f3n", "en el desarrollo cultural."),
 "80.b5.q": ("80:9.15", "es un error pretender", "alpino y mediterr\u00e1neo."),
 "80.b10.q": ("80:1.8", "\u00c9stas fueron las circunstancias", "civilizaci\u00f3n europea."),
 "84.b34.q": ("84:7.30", "estos verdaderos padres ilustran", "todos sus hijos universales."),
}
Q = {}
for k in todo:
    v, a, b = cuts[k]
    t = todo[k]['verses'][v]
    i = t.index(a); j = t.index(b, i) + len(b)
    Q[k] = t[i:j]
json.dump(Q, open(os.path.join(B, 'es', 'quotes_c11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(Q))
