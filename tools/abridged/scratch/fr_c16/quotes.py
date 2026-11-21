import json, os
from common import BASE
Q = {
"119.b36.q": "Urantia est le sanctuaire sentimental de tout Nébadon ; la plus importante de dix-millions de planètes habitées",
"120.b10.q": "Tout au long de ton effusion sur Urantia, tu n’as besoin de te soucier que d’une chose, la communion ininterrompue entre toi et ton Père du Paradis.",
"121.b5.q": "Lorsque Micaël s’incarna sur Urantia, le monde offrait, pour l’effusion du Fils Créateur, les conditions les plus favorables qui aient jamais prévalu précédemment ou se soient présentées par la suite.",
"121.b31.q": "C’est à cette même génération qu’il donna ultérieurement son évangile de religion personnelle — la filiation avec Dieu.",
"121.b46.q": "Sous beaucoup de rapports, j’ai davantage servi de collecteur et d’éditeur que de narrateur original.",
"122.b5.q": "L’enfant de la promesse était venu au monde exactement de la même manière que tous les bébés avant et depuis ce jour.",
"122.b15.q": "Ne doute pas de ma parole, Marie, car ce foyer a été choisi comme habitat terrestre de l’enfant de la destinée.",
"123.b33.q": "Eux qui m’aiment tellement doivent être capables de faire plus pour moi et de me guider plus surement que des étrangers qui peuvent seulement voir mon corps et observer mes pensées, mais ne peuvent guère me connaitre vraiment.",
"124.b5.q": "L’heure est venue. Il est temps que tu commences à t’occuper des affaires de ton Père.",
"124.b32.q": "Ainsi prend fin la carrière du garçon de Nazareth et commence celle de l’adolescent. L’homme divin de plus en plus conscient de soi",
"125.b5.q": "le Père Céleste ne peut aimer ses enfants moins que tu ne m’aimes.",
"125.b25.q": "Il transmettait son enseignement par les questions qu’il posait.",
"126.b18.q": "Jésus avait une aptitude infaillible à reconnaitre la vérité et n’hésitait jamais à l’admettre, quelle que fût la source dont elle paraissait émaner.",
"127.b5.q": "Il apprend lentement à vivre la vie céleste tout en poursuivant son existence terrestre.",
"127.b13.q": "l’argent ne peut aimer.",
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_fr_c16.json'), encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
data = json.load(open(os.path.join(BASE, '..', 'data', 'fr.json'), encoding='utf-8'))
ws = lambda s: ''.join(s.split())
for k, v in Q.items():
    ok = any(ws(v) in ws(data[c]) for c in todo[k]['cit'].split('|'))
    print(k, 'OK' if ok else 'NOT FOUND')
json.dump({k: Q[k] for k in todo}, open(os.path.join(BASE, 'fr', 'quotes_c16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
