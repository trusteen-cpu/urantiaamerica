import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
OUT = os.path.join(BASE, 'es', 'quotes_c22.json')
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c22.json'), encoding='utf-8'))
Q = {
"168.b25.q": "No se niega la respuesta a ninguna oración sincera",
"169.b12.q": "este hijo que estaba muerto, ahora vive nuevamente; estaba perdido y ahora lo he encontrado",
"169.b30.q": "El Dios de los universos gobierna una vasta creación, pero es el Padre en el cielo el que envía su espíritu para que habite en vuestra mente.",
"169.b36.q": "Pero yo he venido para mostraros que, mientras vosotros buscáis a Dios, Dios del mismo modo os busca a vosotros.",
"170.b32.q": "Así pues, la así llamada iglesia cristiana se vuelve el capullo en el cual está ahora durmiendo el concepto del reino de Jesús.",
"170.b38.q": "el reino es la voluntad de su Padre celestial que domina y trasciende en el corazón del creyente",
"171.b5.q": "el Hijo del Hombre no vino para ser ministrado sino para ministrar",
"172.b5.q": "No me preocupan los muros de ladrillos y piedras; pero quisiera derrocar los muros del prejuicio, la mojigatería, y el odio que se alzan frente a esta predicación del amor del Padre por todos los hombres",
"172.b24.q": "Esta pobre viuda echó más que todos los demás",
"173.b12.q": "Mi casa será llamada casa de oración para todas las naciones, mas vosotros la habéis hecho cueva de ladrones",
"173.b35.q": "No tendré aquí a nadie sino a los que se regocijan de aceptar mi invitación, y que me hacen el honor de llevar los mantos nupciales que tan generosamente se les han proveído",
"174.b12.q": "Y cuando amáis a vuestro hermano, ya le habéis perdonado.",
"174.b21.q": "mi Padre no es el Dios de los muertos sino el de los vivos.",
"174.b35.q": "El perdón divino es inevitable; es inherente e inalienable a la infinita comprensión de Dios",
"175.b11.q": "el que quiere ser más grande entre vosotros debe ser el siervo de todos.",
"176.b5.q": "Libremente habéis recibido; por lo tanto, libremente debéis dar de la verdad del cielo",
"176.b17.q": "El ojo de la carne contempla al Hijo del Hombre en la carne, pero sólo el ojo del espíritu podrá contemplar al Hijo del Hombre glorificado por su Padre",
}
assert set(Q) == set(todo), set(todo) ^ set(Q)
for k, v in Q.items():
    vs = todo[k]['verses']
    assert any(v.replace(' ', '') in t.replace(' ', '') for t in vs.values()), k
json.dump({k: Q[k] for k in todo}, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(Q))
