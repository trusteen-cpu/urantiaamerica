import json, os
B = os.path.dirname(os.path.abspath(__file__)) + '/../../'
V = json.load(open(B + '../data/fr.json', encoding='utf-8'))
def cut(v, a, b):
    t = V[v]; i = t.index(a); j = t.index(b, i) + len(b); return t[i:j]
Q = {
 "78.b5.q": cut("78:8.12", "longtemps avant que les cavaliers", "du vingtième siècle."),
 "79.b5.q": cut("79:4.9", "la religion, la vraie", "fraternité humaine."),
 "79.b20.q": cut("79:4.8", "il peut arriver, un jour", "du Dieu vivant"),
 "79.b30.q": cut("79:6.10", "Le stimulant d’une religion", "développement culturel"),
 "80.b5.q": cut("80:9.15", "Il est fallacieux", "Méditerranéens."),
 "80.b10.q": cut("80:1.8", "Ce sont ces circonstances", "européenne moderne."),
 "80.b40.q": cut("80:9.15", "Même en l’an", "Amérique du Nord."),
 "84.b5.q": cut("84:6.8", "La famille est le plus grand", "mari et femme."),
 "84.b27.q": cut("84:6.8", "Le mariage est la mère", "de la société."),
 "84.b34.q": cut("84:7.30", "ces véritables parents", "enfants de l’univers."),
}
todo = json.load(open(B + 'work/todo_fr_c11.json', encoding='utf-8'))
assert list(Q) == list(todo) or set(Q) == set(todo)
json.dump({k: Q[k] for k in todo}, open(B + 'fr/quotes_c11.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
