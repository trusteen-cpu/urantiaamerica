import json, os
H = os.path.dirname(os.path.abspath(__file__))
COS = os.path.normpath(os.path.join(H, '..', '..'))
B = json.load(open(os.path.join(COS, '..', 'data', 'fr.json'), encoding='utf-8'))

def cut(v, a, b):
    t = B[v]
    i = t.index(a)
    j = t.index(b, i) + len(b)
    return t[i:j]

Q = {
 "w08.016": cut("0:7.1", "Dieu le Suprême, Dieu l’Ultime", "en expansion évolutionnaire."),
 "w08.040": cut("18:3.8", "ils n’ont pas gagné", "souverain expérientiel"),
 "w08.069": cut("117:2.3", "ces fils trinitisés par des créatures, tout", "croissance du Suprême."),
 "w08.091": cut("8:0.2", "À l’aurore", "éternelle et absolue."),
 "w08.161": cut("105:7.2", "mais Havona lui-même", "il est Havona."),
 "w08.180": cut("117:7.17", "Peut-être y aura-t-il", "pas pour longtemps !"),
 "w09.032": cut("38:1.1", "Les séraphins sont créés", "angéliques furent créés."),
 "w09.057": cut("117:2.4", "Une chose est certaine", "par une croissance."),
 "w09.070": cut("105:7.2", "Transcendantal ne signifie", "au sens fini."),
 "w09.100": cut("30:1.99", "En tant que superpersonne", "Dieu se fragmente"),
 "w09.106": cut("3:0.3", "La faculté de créer", "nature agissante."),
 "w09.119": cut("33:4.2", "Mais ces Fils, en union", "Radieuse Étoile du Matin"),
 "w09.131": cut("22:4.5", "car l’embrassement de la Trinité", "potentiels non réalisés des créatures."),
 "w09.141": cut("22:7.3", "Les créatures glorifiées", "épisodes de trinitisation."),
 "w09.152": cut("112:1.17", "Entre deux objets", "aboutissent à un système"),
 "w09.162": cut("109:7.4", "Ils sont omnipersonnels", "après la personnalité."),
 "w09.177": cut("0:5.4", "mais jamais l’impersonnel", "le don du Père du Paradis."),
 "w09.200": cut("24:7.2", "recevoir le privilège", "parmi ses semblables."),
 "w09.206": cut("25:1.4", "Dans la création de Servites", "pour un semi-physique."),
}
todo = json.load(open(os.path.join(COS, 'work', 'todo_fr_c05.json'), encoding='utf-8'))
assert list(todo) == list(Q), (set(todo) ^ set(Q))
json.dump(Q, open(os.path.join(COS, 'fr', 'quotes_c05.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
