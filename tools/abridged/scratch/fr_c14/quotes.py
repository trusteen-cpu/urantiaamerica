import json, sys
sys.stdout.reconfigure(encoding='utf-8')
T = json.load(open('work/todo_fr_c14.json', encoding='utf-8'))
data = json.load(open('../data/fr.json', encoding='utf-8'))
def sent(cit, start, end):
    v = data[cit]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]
Q = {
 "102.b5.q": sent("102:1.1", "qu’il faut connaitre", "pour les connaitre."),
 "102.b14.q": sent("102:2.7", "La cristallisation", "mort spirituelle."),
 "104.b17.q": sent("104:2.4", "La Trinité est une réalité", "trois Déités Paradisiaques."),
 "104.b30.q": sent("104:4.46", "en lui, toutes choses subsistent", "subsistent"),
 "105.b5.q": sent("105:1.8", "La face que", "Père Universel d’amour."),
 "106.b25.q": sent("106:5.3", "Les trinités sont donc", "de personnalité."),
 "107.b5.q": sent("107:0.6", "L’Ajusteur est l’infaillible", "vers Dieu."),
 "107.b10.q": sent("107:1.2", "Ils sont de Dieu", "ils sont Dieu."),
 "107.b29.q": sent("107:6.2", "L’Ajusteur est la possibilité", "de se personnaliser."),
 "108.b15.q": sent("108:2.4", "Il n’y a ni intermédiaires", "reliés directement."),
 "108.b31.q": sent("108:6.7", "Les Ajusteurs sont les ancêtres", "âme immortelle en évolution"),
 "109.b5.q": sent("109:6.1", "Nulle expérience valable", "ne périt jamais."),
 "109.b26.q": sent("109:5.5", "L’hérédité peut", "aventure ascendante."),
}
assert set(Q) == set(T)
json.dump(Q, open('fr/quotes_c14.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in Q.items(): print(k, v)
