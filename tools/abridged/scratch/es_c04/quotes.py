import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
Q = {
"27.b33.q": "¡Qué florecimiento del plan y propósito eterno de los Dioses, que el amor inteligente del hijo criatura dé plena satisfacción al amor infinito del Padre Creador!",
"29.b5.q": "No pueden abandonar jamás, ni siquiera por una fracción de segundo, la supervisión directa de los circuitos de la energía del tiempo y del espacio.",
"30.b11.q": "Dios, como superpersona, eventúa; Dios, como persona, crea; Dios, como prepersona, fragmenta",
"32.b5.q": "Dios nos ha dado de sí mismo para que nosotros podamos ser como él",
"32.b21.q": "el que ha visto a un Hijo Creador, ha visto al Padre.",
"32.b33.q": "¡El objetivo de la eternidad os aguarda! ¡La aventura del logro de la divinidad se encuentra frente a vosotros! ¡La carrera por la perfección está en marcha!",
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c04.json'), encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
for k, v in Q.items():
    for c in todo[k]['cit'].split('|'):
        if v in todo[k]['verses'][c]:
            break
    else:
        raise SystemExit('not verbatim: ' + k)
json.dump({k: Q[k] for k in todo}, open(os.path.join(BASE, 'es', 'quotes_c04.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes ok', len(Q))
