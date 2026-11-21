import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
Q = {
"58.b13.q": "la vie agréable que vous menez sur Urantia est due à l’influence « fortuite » de plus de quarante phénomènes protecteurs apparemment accidentels et semblables à l’action de cette couche d’ozone très spéciale.",
"59.b5.q": "la mer a donné naissance aux formes de vie primitives du royaume et les a entretenues.",
"61.b30.q": "vos premiers ancêtres naquirent et se reproduisirent dans un milieu difficile, tonifiant et stimulant.",
"62.b5.q": "C’est la première décision mentale — d’un mental du type humain — sur Urantia, et elle établit automatiquement le circuit de communication",
"62.b18.q": "Si la grenouille ancestrale de toute l’humanité avait sauté cinq centimètres de moins dans une certaine occasion, tout le cours de l’évolution aurait été notablement changé.",
"62.b38.q": "L’évolution biologique avait une fois de plus atteint les niveaux humains de dignité volitive ; l’homme était apparu sur la planète 606 de Satania.",
"63.b5.q": "le récit de l’évolution, de la lutte pour la vie, de la mort et de la survie éternelle des parents exceptionnels de l’humanité tout entière.",
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_fr_c08.json'), encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
for k, v in Q.items():
    vv = list(todo[k]['verses'].values())
    assert any(v.replace(' ', '') in x.replace(' ', '') for x in vv), k
json.dump({k: Q[k] for k in todo}, open(os.path.join(BASE, 'fr', 'quotes_c08.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes ok', len(Q))
