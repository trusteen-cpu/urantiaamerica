import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
data = json.load(open(os.path.join(BASE, '..', 'data', 'es.json'), encoding='utf-8'))
def cut(v, start, end):
    t = data[v]; i = t.index(start); j = t.index(end, i) + len(end); return t[i:j]
Q = {
 "150.b11.q": cut("150:1.3", "en el reino del cielo no hay ricos", "hijos e hijas de Dios"),
 "151.b5.q": cut("151:3.1", "Pensad no s", "la oir\u00e9is vosotros."),
 "151.b26.q": cut("151:5.5", "\u00bfPor qu\u00e9 ten\u00e9is tanto miedo", "Paz, callaos"),
 "153.b5.q": cut("153:5.4", "es el esp\u00edritu el que da la vida", "son esp\u00edritu y vida."),
 "153.b15.q": cut("153:2.8", "yo soy el pan de la vida. El que viene", "jam\u00e1s tendr\u00e1 sed."),
 "154.b5.q": cut("154:6.5", "Puesto que el que haga la voluntad", "y mi hermana."),
 "154.b13.q": cut("154:2.5", "Las situaciones problem\u00e1ticas", "la mente, el alma y el esp\u00edritu"),
 "154.b23.q": cut("154:4.6", "Este mundo no ha intentado nunca", "las ense\u00f1anzas de Jes\u00fas"),
 "154.b31.q": cut("154:6.7", "No, m\u00e1s bien bendito", "se atreve a obedecerla."),
 "155.b5.q": cut("155:6.4", "La religi\u00f3n de la mente", "la revelaci\u00f3n progresiva"),
 "155.b16.q": cut("155:3.5", "la verdadera religi\u00f3n era la lealtad", "m\u00e1s veraces."),
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c20.json'), encoding='utf-8'))
assert set(Q) == set(todo)
json.dump(Q, open(os.path.join(BASE, 'es', 'quotes_c20.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
