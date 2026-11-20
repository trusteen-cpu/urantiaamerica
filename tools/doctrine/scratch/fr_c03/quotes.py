import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
FR = json.load(open('../data/fr.json', encoding='utf-8'))
todo = json.load(open('work/todo_fr_c03.json', encoding='utf-8'))

# key: list of (start, end) markers inclusive, in verse order
C = {
 'ch12:9': [('l’impulsion du mental fini', 'l’expérience de la créature.')],
 'ch12:11': [('Le mental matériel', 'significations divines')],
 'ch12:16': [('Cette opération céleste', 'réalités superanimales')],
 'ch12:18': [('la naissance graduelle', 'Moniteur de Mystère.')],
 'ch12:22': [('La conscience de soi', 'de l’expérience humaine.')],
 'ch12:28': [('Le mental humain et l’Ajusteur divin', 'en tant qu’identités associées.')],
 'ch12:32': [('Dans la mesure où', 'devient indestructible.')],
 'ch12:34': [('Durant la vie, la volonté', 'l’âme morontielle.')],
 'ch12:39': [('Les erreurs du mental mortel', 'rejeter la survie.')],
 'ch13:16': [('Environ un an plus tard', 'reconnus comme tels.')],
 'ch13:24': [('Nous étions tous très préoccupés', 'nous ne le pouvions pas')],
 'ch13:39': [('L’altruisme n’était pas', 'aborigènes d’Urantia.')],
 'ch13:45': [('Tous les mortels habités', 'réciproque avec la divinité.')],
 'ch14:10': [('Parmi les émotions religieuses', 'la glace en face')],
 'ch14:14': [('mais ses progrès étaient si faibles', 'allait échouer.')],
 'ch14:41': [('Au début, les tribus Sangik', 'la race la plus ancienne.')],
 'ch14:49': [('Il n’y a plus de problèmes', 'la paix et la tranquillité.')],
 'ch15:3': [('Partant de ce début magnifique', 'aveuglement aux relations cosmiques.')],
 'ch15:10': [('Il a dû exister un orgueil', 'et peut-être de l’univers.')],
 'ch15:12': [('Le choix délibéré du mal', 'constitue l’iniquité.')],
 'ch15:19': [('C’est la vie matérielle', 'faisait rage.')],
 'ch15:29': [('L’aptitude des hommes à choisir', 'qui lui est divinement donnée')],
 'ch15:37': [('Le libre arbitre humain', 'volonté personnelle de l’homme.')],
 'ch15:49': [('le péché d’un être quelconque', 'de l’intéressé lui-même.')],
 'ch16:8': [('Lorsque cette lignée', 'luttes antérieures.')],
 'ch16:18': [('Mais cela demanderait', 'pendant sa vie.')],
 'ch16:27': [('Adam n’aimait pas la guerre', 'aux Nodites.')],
 'ch16:33': [('Peu après leur réduction', 'de les habiter.')],
 'ch16:35': [('Ils avaient quitté Jérusem', 'fils de l’homme.')],
 'ch16:49': [('c’est plutôt parce que le mal', 'Père du Paradis.')],
}
out = {}
for k, v in todo.items():
    verse = FR[v['cit']]
    parts = []
    for s, e in C[k]:
        i = verse.index(s)
        j = verse.index(e, i) + len(e)
        parts.append(verse[i:j])
    out[k] = ' … '.join(parts)
assert set(out) == set(todo), set(todo) ^ set(out)
json.dump(out, open('fr/quotes_c03.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k in out:
    print(k, len(out[k]) / len(todo[k]['en']))
