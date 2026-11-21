import json, os
B = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
Q = {
"65.b5.q": "si un determinado individuo en verdad conoce a Dios y desea encontrarle y llegar a ser como él, la supervivencia está garantizada a pesar de los obstáculos del tiempo.",
"66.b10.q": "No comprendí por aquel entonces que Caligastia se estaba enamorando insidiosamente de sí mismo; en ese momento, no entendía yo tan a fondo las sutilezas del orgullo de la personalidad.",
"67.b5.q": "jamás el pecado de ningún ser le roba a otro la realización del derecho divino de la supervivencia de la personalidad.",
"67.b37.q": "¿Qué hay de Amadón de Urantia, sigue inconmovible?",
"69.b42.q": "Cuando cambiéis el orden social, no os olvidéis de cambiarlo por otro mejor. No os dejéis persuadir de experimentar con las fórmulas descartadas de vuestros antecesores ¡Avanzad, no retrocedáis!",
}
todo = json.load(open(os.path.join(B, 'work', 'todo_es_c09.json'), encoding='utf-8'))
assert set(todo) == set(Q)
for k, v in Q.items():
    assert ''.join(v.split()) in ''.join(list(todo[k]['verses'].values())[0].split()), k
json.dump(Q, open(os.path.join(B, 'es', 'quotes_c09.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
