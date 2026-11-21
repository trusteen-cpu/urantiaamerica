import json, os
BASE = r'E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged'
T = json.load(open(os.path.join(BASE, 'work', 'todo_fr_c01.json'), encoding='utf-8'))
# key: (verse, start, end)  -> substring from start through end, inclusive
C = {
"0.b0.q": ("0:0.4", "Cette Introduction n’est donc", "des fascicules suivants"),
"1.b6.q": ("1:0.3", "Soyez parfaits", "je suis parfait."),
"1.b45.q": ("1:5.16", "Dans toutes vos afflictions", "en vous et avec vous."),
"2.b6.q": ("2:5.10", "Dieu est amour, mais", "n’est pas Dieu."),
"2.b50.q": ("2:6.4", "Dieu n’aime pas comme", "en tant que père."),
"2.b63.q": ("2:6.6", "Dieu en tant que père", "en tant que juge."),
"3.b6.q": ("3:1.4", "L’homme sort à la recherche", "dans son propre cœur."),
"4.b6.q": ("4:1.2", "le progrès est le mot de passe", "de l’univers"),
"4.b23.q": ("4:2.8", "la nature n’est pas Dieu.", "un objet d’adoration."),
"4.b36.q": ("4:4.5", "En premier et en dernier lieu", "est un Père."),
"5.b12.q": ("5:1.8", "Dieu est approchable", "la voie est ouverte"),
"5.b25.q": ("5:3.8", "Le mental mortel consent", "dirige cette adoration"),
"5.b44.q": ("5:6.12", "La porte de l’éternité", "du libre arbitre."),
"6.b7.q": ("6:8.3", "Dieu est la pensée initiatrice", "le verbe expressif."),
"6.b54.q": ("6:8.4", "les mortels conscients de Dieu", "Fils des Fils."),
"6.b56.q": ("6:3.5", "Dieu est amour, le Fils", "l’amour appliqué"),
"7.b6.q": ("7:0.4", "Le monde de l’esprit", "personnelle du Fils"),
"7.b12.q": ("7:1.2", "La gravité d’esprit", "diminuée par l’espace."),
"7.b48.q": ("7:5.11", "quiconque a vu", "Fils Éternel de Dieu."),
}
out = {}
for k in T:
    v, a, b = C[k]
    txt = T[k]['verses'][v]
    i = txt.find(a); j = txt.find(b, i)
    assert i >= 0 and j >= 0, k
    out[k] = txt[i:j + len(b)]
json.dump(out, open(os.path.join(BASE, 'fr', 'quotes_c01.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'quotes')
