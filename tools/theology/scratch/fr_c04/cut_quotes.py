import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
TH = os.path.normpath(os.path.join(HERE, "..", ".."))
V = json.load(open(os.path.join(TH, "..", "data", "fr.json"), encoding="utf-8"))
todo = json.load(open(os.path.join(TH, "work", "todo_fr_c04.json"), encoding="utf-8"))

S = {
 "ch19.s1.u1.q1#0": ("111:1.4", [("L’évolution matérielle", "vivez ou mourez.")]),
 "ch19.s3.u3.q1#0": ("112:5.5", [("C’est ce pouvoir", "responsabilité cosmique.")]),
 "ch19.s4.u2.q2#0": ("111:3.7", [("Dans la mesure", "devient indestructible."), ("Mais ceci est", "d’être achevé.")]),
 "ch20.s1.u2.q1#0": ("107:1.2", [("De même que leurs", "ils sont Dieu.")]),
 "ch20.s1.u3.q2#0": ("107:0.6", [("L’Ajusteur est la divine", "l’âme vers Dieu.")]),
 "ch20.s2.u1.q2#0": ("108:2.4", [("Même dans le cas", "d’une décision morale"), ("Il n’y a ni", "reliés directement.")]),
 "ch20.s3.u1.q1#0": ("110:2.1", [("Vous êtes tous des sujets", "programme des Ajusteurs de Pensée."), ("Les Ajusteurs respectent", "à votre volonté.")]),
 "ch20.s3.u1.q2#0": ("110:2.2", [("Nul être humain", "créatures du temps.")]),
 "ch20.s3.u2.q1#0": ("110:3.4", [("Le grand but", "dans votre mental."), ("La coopération avec", "appréhension craintive.")]),
 "ch20.s4.u1.q1#0": ("111:1.5", [("Le mental mortel est", "aura prises.")]),
 "ch20.s4.u2.q2#0": ("111:3.1", [("Même après avoir survécu", "faire la volonté du Père.")]),
 "ch20.s4.u3.q1#0": ("111:7.2", [("L’habitant divin", "avec vous et pour vous.")]),
 "ch21.s4.u3.q1#0": ("48:5.7", [("Les choses que vous", "atteindre le Paradis.")]),
 "ch22.s2.u1.q1#0": ("84:6.6", [("Les hommes et les femmes", "montée au Paradis.")]),
 "ch23.s2.u3.q1#0": ("71:3.12", [("Dans les États", "fonctionnaires civils et sociaux.")]),
 "ch23.s2.u3.q2#0": ("70:12.5", [("Les mortels d’Urantia", "procédure administrative."), ("Ils ne devraient élire", "responsabilités sacrées")]),
 "ch23.s4.u2.q2#0": ("178:1.8", [("Vous devriez devenir", "royaume des cieux.")]),
 "ch24.s1.u1.q2#0": ("54:0.2", [("Ce ne sont pas", "concernant la perfection."), ("Le choix délibéré", "constitue l’iniquité.")]),
 "ch24.s4.u2.q1#0": ("89:10.4", [("La possibilité de", "toujours ascendante.")]),
 "ch24.s4.u3.q1#0": ("2:6.8", [("Dieu aime les pécheurs", "n’est pas une personne."), ("L’amour de Dieu sauve", "détruit le péché.")]),
 "ch25.s3.u1.q1#0": ("75:8.1", [("Adam et Ève furent", "la race humaine fut élevée.")]),
 "ch25.s3.u1.q2#0": ("75:8.2", [("Il n’y a pas eu", "biologique antérieure.")]),
 "ch25.s4.u1.q2#0": ("76:5.2", [("En tant que citoyens", "de les habiter.")]),
 "ch25.s4.u2.q1#0": ("76:5.3", [("Parmi d’autres expressions", "chercher auparavant. »")]),
 "ch25.s4.u3.q2#0": ("76:6.3", [("Adam et Ève passèrent", "personnalités de l’univers."), ("Ils furent immédiatement", "contrôle consultatif d’Urantia.")]),
}

keys = list(todo) if isinstance(todo, (list, dict)) else []
out = {}
for k in keys:
    ref, pieces = S[k]
    v = V[ref]
    parts = []
    pos = 0
    for a, b in pieces:
        i = v.index(a, pos)
        j = v.index(b, i) + len(b)
        parts.append(v[i:j])
        pos = j
    out[k] = " … ".join(parts)
missing = [k for k in S if k not in out]
print("todo", len(keys), "cut", len(out), "unused specs", missing)
json.dump(out, open(os.path.join(TH, "fr", "quotes_c04.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
