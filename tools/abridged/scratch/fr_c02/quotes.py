import json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
todo = json.load(open('work/todo_fr_c02.json', encoding='utf-8'))
data = json.load(open('../data/fr.json', encoding='utf-8'))
# key: (verse, start anchor, end anchor inclusive)
spec = {
 '8.b4.q': ('8:0.3', 'l’Esprit Infini, en possession', 'à l’existence.'),
 '8.b20.q': ('8:4.2', 'Dieu est amour', 'l’Esprit est ministère'),
 '8.b33.q': ('8:6.4', 'le Créateur Conjoint', 'une personne divine.'),
 '8.b37.q': ('8:6.4', 'Que celui qui a des oreilles', 'ce que dit l’Esprit.'),
 '9.b44.q': ('9:6.9', 'l’Esprit Infini est pour toutes', 'mental du Créateur'),
 '10.b4.q': ('10:3.1', 'Bien qu’il n’existe', 'divines de la Déité.'),
 '10.b43.q': ('10:7.1', 'Il y a perfection', 'des Déités éternelles.'),
 '11.b35.q': ('11:4.5', 'l’œil n’a pas vu', 'à la vie de la chair'),
 '12.b4.q': ('12:7.12', 'le Père n’est très éloigné', 'il habite en vous'),
 '13.b15.q': ('13:1.23', 'Nous sommes au courant', 'comme une réalité absolue.'),
 '13.b30.q': ('13:4.5', 'C’est ainsi que l’esprit', 'créatures des royaumes.'),
 '15.b5.q': ('15:14.9', 'votre sphère est administrée', 'seul monde habité existant.'),
}
out = {}
for k in todo:
    v, a, b = spec[k]
    t = data[v]
    i = t.index(a); j = t.index(b, i) + len(b)
    out[k] = t[i:j]
    print(k, out[k])
json.dump(out, open('fr/quotes_c02.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
