# -*- coding: utf-8 -*-
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
todo = json.load(open('work/todo_es_c17.json', encoding='utf-8'))
def cut(k, a, b=None):
    v = todo[k]['verses'][todo[k]['cit'].split('|')[0]]
    i = v.index(a)
    j = v.index(b, i) + len(b) if b else len(v)
    return v[i:j]
Q = {
 "128.b10.q": cut("128.b10.q", "Tenemos un Soberano", "no pecó"),
 "128.b26.q": cut("128.b26.q", "La casa de José", "puedan trabajar"),
 "129.b5.q": cut("129.b5.q", "Jesús es la senda nueva", "a la eternidad."),
 "129.b25.q": cut("129.b25.q", "No podéis aspirar", "vivió la suya."),
 "130.b5.q": cut("130.b5.q", "ningún hombre es extraño", "conoce a Dios."),
 "130.b38.q": cut("130.b38.q", "Tu problema no es", "te ha encontrado a ti"),
 "131.b38.q": cut("131.b38.q", "Dios no recompensa", "lo que es"),
 "131.b47.q": cut("131.b47.q", "Por fin tengo", "salvación eterna"),
 "134.b5.q": cut("134.b5.q", "Que se haga", "en el Paraíso"),
}
assert set(todo) == set(Q)
json.dump({k: Q[k] for k in todo}, open('es/quotes_c17.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
