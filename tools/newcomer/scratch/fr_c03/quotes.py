import json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
T = json.load(open('work/todo_fr_c03.json', encoding='utf-8'))
# each value: list of (start, end) substrings; piece = verse[start .. end inclusive]
P = {
 'w10:27': [("La religion n’est pas le produit", "entièrement logique.")],
 'w10:29': [("L’esprit divin établit", "vers Dieu.")],
 'w10:37': [("La croyance a atteint", "simple croyance.")],
 'w10:61': [("Il y a un but réel", "de la bonté ;"), ("d’amplifier le service", "culte en commun.")],
 'w10:65': [("Mais, à mesure que", "cristallisation des sentiments ;"), ("religion détournée du service", "au lieu de ministres ;"), ("et elle perd graduellement", "de salut éternel.")],
 'w10:95': [("Ayant commandé à l’homme", "avec cet Ajusteur divin")],
 'w10:99': [("tout le monde est d’accord", "présence factuelle du Dieu infini."), ("Ils sont de Dieu", "ils sont Dieu.")],
 'w10:103': [("L’Ajusteur est une essence absolue", "créature finie."), ("L’Ajusteur est la divine réalité", "vers Dieu.")],
 'w10:107': [("Les anges et d’autres", "sept groupes.")],
 'w10:127': [("Le grand but de l’existence", "l’Ajusteur intérieur."), ("Mais un effort dévoué", "honorable et réussie."), ("La vie idéale", "appréhension craintive.")],
 'w10:168': [("Les Ajusteurs manipulent", "est suprême.")],
 'w10:174': [("La création évolutionnaire", "habite ce mental humain"), ("3. La relation entre", "C’est l’âme.")],
 'w10:186': [("Ce qui assure la survie", "identification à l’esprit."), ("Ce que vous êtes aujourd’hui", "dans l’éternité.")],
 'w10:190': [("Mais ceci est éternellement vrai", "mérite d’être achevé.")],
 'w10:196': [("Urantia est votre point de départ", "doté d’un guide parfait ;"), ("Pendant tous ces âges", "en présence du changement.")],
 'w10:200': [("L’Ajusteur de Pensée ne vous rappellera", "carrière universelle."), ("Mais la personnalité et les relations", "et persistera.")],
 'w10:220': [("La perplexité est inévitable", "agitation spirituelle.")],
 'w10:224': [("Jésus dépeignit la sécurité", "absolument inexpugnable")],
 'w10:250': [("Dieu répond à la prière", "expérience humaine")],
 'w10:268': [("Ce choix ne consiste pas", "volonté soit faite ».")],
 'w10:311': [("L’homme peut découvrir", "autres hommes")],
 'w10:315': [("Sa Déité est le large canal", "qui est amour.")],
 'w11:24': [("Le but de ces incarnations", "et d’une nouvelle manière.")],
 'w11:34': [("Dans son effusion Melchizédek", "chair et de sang.")],
 'w11:59': [("Tout au long de ton effusion", "Père Universel de tous.")],
 'w11:63': [("Il n’était pas Dieu en association", "cet être composé.")],
 'w11:81': [("Lorsque Micaël s’incarna", "par la suite.")],
 'w11:95': [("Le plan de Micaël", "parents d’effusion.")],
 'w11:109': [("Ce fut l’un des jours", "affaires de ton Père. »")],
 'w11:119': [("Le jeune charpentier", "un autre enfant attendu.")],
 'w11:155': [("La substance de son message", "converser avec lui."), ("En règle générale", "surmenés, anxieux et déprimés")],
 'w11:175': [("Jésus n’a pas vécu sa vie sur terre", "tous les autres êtres humains."), ("Vous ne pouvez pas aspirer", "par les mêmes moyens."), ("Jésus est le chemin nouveau", "du temps à l’éternité.")],
 'w11:183': [("À tous les expédients", "soit faite ».")],
 'w11:185': [("Un après-midi de fin d’été", "temps et de l’espace.")],
 'w11:204': [("Il est donc évident", "rémission des péchés.")],
 'w11:206': [("Il s’agissait d’un baptême", "s’occuper des affaires de son Père")],
 'w11:212': [("beaucoup d’observateurs suprahumains", "j’ai trouvé mon plaisir. »")],
 'w11:242': [("le royaume de mon Père ne concerne", "le royaume des cieux.")],
 'w11:258': [("Jésus dit : « Les gens", "la filiation avec Dieu. »")],
 'w11:280': [("Les religions d’autorité exigent", "diversité des croyances."), ("Les religions d’autorité se cristallisent", "des soins miséricordieux.")],
 'w11:295': [("Nous ne voudrions pas minimiser", "fraternité des hommes.")],
 'w11:303': [("Jésus ne demande pas", "avec le Père céleste.")],
 'w12:31': [("Abaissant son regard", "l’évangile du salut.")],
 'w12:57': [("Souvenez-vous que c’est la fidélité", "que Jésus demande."), ("L’impulsion de l’amitié", "par un ami.")],
 'w12:67': [("Avant l’arrivée de Judas", "d’une manière satisfaisante.")],
 'w12:77': [("Jésus mourut royalement", "la journée tragique."), ("Après une telle vie", "« C’est fini. »")],
 'w12:89': [("Bien que Jésus n’ait pas enduré", "la voie du salut ;")],
 'w12:93': [("Toute l’idée de rançon", "la nature divine.")],
 'w12:97': [("Il n’est guère approprié", "(de la survie) ;")],
 'w12:115': [("La croix est le grand symbole", "dévotion même de leur amour.")],
 'w12:148': [("Le tombeau de Joseph était vide", "spéciale et exceptionnelle,")],
 'w12:160': [("Tandis qu’elles méditaient", "et mon Maitre ! »")],
 'w12:224': [("les apôtres ne furent pas les seuls", "du monde entier."), ("Enfin, la vraie religion", "individuelle des hommes.")],
 'w12:258': [("On peut prêcher une religion", "ressuscité et glorifié.")],
 'w12:283': [("Jésus ne demande pas", "avec le Père céleste.")],
}
out = {}
for k, v in T.items():
    verse = v['verse']
    pieces = []
    pos = 0
    for s, e in P[k]:
        i = verse.index(s, pos)
        j = verse.index(e, i) + len(e)
        pieces.append(verse[i:j].strip().rstrip(',;').strip() if False else verse[i:j].strip())
        pos = j
    out[k] = ' … '.join(pieces)
assert set(out) == set(T)
json.dump(out, open('fr/quotes_c03.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out))
