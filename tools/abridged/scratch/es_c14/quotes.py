import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
data = json.load(open(os.path.join(BASE, '..', 'data', 'es.json'), encoding='utf-8'))
def cut(v, start, end):
    t = data[v]; i = t.index(start); j = t.index(end, i) + len(end); return t[i:j]
Q = {
 "102.b5.q": cut("102:1.1", "hay que conocer a las cosas humanas", "para poderlas conocer"),
 "104.b17.q": cut("104:2.4", "La Trinidad es una realidad de Deidad", "Deidades del Paraíso."),
 "105.b5.q": cut("105:1.8", "el rostro que el Infinito", "Padre Universal del amor."),
 "105.b31.q": cut("105:6.5", "Esta demora de tiempo", "desarrollo máximo."),
 "107.b10.q": cut("107:1.2", "son de Dios, y en cuanto", "son Dios."),
 "108.b31.q": cut("108:6.7", "Los Ajustadores son los antepasados", "almas inmortales evolutivas"),
 "109.b30.q": cut("109:6.5", "Esta consagración decisiva", "logro divino."),
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c14.json'), encoding='utf-8'))
assert set(Q) == set(todo)
json.dump(Q, open(os.path.join(BASE, 'es', 'quotes_c14.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
