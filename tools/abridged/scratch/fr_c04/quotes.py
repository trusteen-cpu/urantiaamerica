import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
todo = json.load(open('work/todo_fr_c04.json', encoding='utf-8'))
data = json.load(open('../data/fr.json', encoding='utf-8'))
spec = {
 '25.b5.q': ('25:1.6', 'Bravo, bon', 'univers.'),
 '27.b33.q': ('27:7.7', 'l’amour intelligent', 'Créateur !'),
 '28.b29.q': ('28:6.9', 'Si la survie', 'rattrapées.'),
 '29.b5.q': ('29:3.5', 'Ces êtres ne peuvent', 'espace.'),
 '29.b21.q': ('29:4.13', 'La personnalité ne', 'mental.'),
 '30.b11.q': ('30:1.99', 'En tant que superpersonne', 'se fragmente'),
 '32.b5.q': ('32:4.12', 'Dieu s’est donné', 'lui ressembler'),
 '32.b21.q': ('32:3.6', 'C’est un fait, quiconque', 'le Père.'),
 '32.b33.q': ('32:5.8', 'Le but', 'engagée !'),
}
out = {}
for k in todo:
    v, a, b = spec[k]
    t = data[v]
    i = t.index(a); j = t.index(b, i) + len(b)
    out[k] = t[i:j]
    print(k, out[k])
json.dump(out, open('fr/quotes_c04.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
