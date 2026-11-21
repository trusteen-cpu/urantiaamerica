import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
todo = json.load(open(os.path.join(BASE, 'work', 'todo_fr_c09.json'), encoding='utf-8'))
Q = {
"65.b5.q": "si l’individu connait réellement Dieu et désire vraiment le trouver et devenir semblable à lui, alors sa survie est assurée en dépit des handicaps du temps.",
"66.b5.q": "Le libre arbitre humain est suprême en matière de morale. Même l’Ajusteur de Pensée intérieur se refuse à contraindre l’homme à former une seule pensée ou à accomplir un seul acte contraire au choix de la volonté personnelle de l’homme.",
"66.b10.q": "Je ne comprenais pas alors que Caligastia était en train de tomber insidieusement amoureux de lui-même ; je ne saisissais pas encore pleinement les subtilités de l’orgueil de la personnalité.",
"67.b5.q": "le péché d’un être quelconque ne dérobe jamais à un autre le droit divin de jouir de la survie de la personnalité.",
}
assert set(Q) == set(todo), set(todo) ^ set(Q)
for k, v in Q.items():
    vs = list(todo[k]['verses'].values())[0]
    assert ' '.join(v.split()) in ' '.join(vs.split()), k
json.dump(Q, open(os.path.join(BASE, 'fr', 'quotes_c09.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
