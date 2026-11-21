import json, os
from common import BASE
Q = {
 "94.b29.q": "La Deidad Absoluta no lucha pero es siempre victoriosa; no fuerza a la humanidad pero está siempre lista para responder a sus deseos auténticos",
 "95.b34.q": "Porque dondequiera que tres hombres hablen juntos, Dios está presente y es el cuarto",
 "96.b5.q": "La característica más singular y sorprendente de la historia religiosa de los hebreos concierne esta continua evolución del concepto de Deidad",
 "96.b20.q": "El eterno Dios es tu refugio, y acá abajo los brazos eternos",
 "96.b33.q": "Orará a Dios y hallará su favor y verá su faz con júbilo, pues Dios otorgará al hombre rectitud divina",
 "97.b5.q": "Dios no olvidará, Dios no abandonará",
 "97.b10.q": "El que es la Fuerza de Israel no mentirá ni se arrepentirá, porque no es hombre para que se arrepienta",
 "97.b25.q": "Oh hombre, él me ha mostrado qué es bueno; y qué es lo que espera el Señor de ti sino que seas justo y que ames la misericordia y que camines humildemente con tu Dios",
 "98.b37.q": "Ha dejado de ser desde hace mucho la religión de Jesús a pesar de que aún retrata valerosamente una religión bella sobre Jesús",
 "99.b26.q": "la verdadera religión consiste en conocer a Dios como a tu Padre y al hombre como a tu hermano.",
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c13.json'), encoding='utf-8'))
data = json.load(open(os.path.join(BASE, '..', 'data', 'es.json'), encoding='utf-8'))
assert set(Q) == set(todo)
for k, v in Q.items():
    vs = todo[k]['cit'].split('|')
    ok = any(''.join(v.split()) in ''.join(data[c].split()) for c in vs)
    assert ok, k
json.dump(Q, open(os.path.join(BASE, 'es', 'quotes_c13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes ok', len(Q))
