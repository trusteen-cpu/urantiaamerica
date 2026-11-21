# -*- coding: utf-8 -*-
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
T = json.load(open(os.path.join(H, "work", "todo_fr_c01.json"), encoding="utf-8"))
A = lambda s: s.replace("'", "\u2019")
P = {
 "w01:78": [("Nous sommes pleinement", "significations de l'univers.")],
 "w01:174": [("5. Les Fascicules", "faire ces franches déclarations")],
 "w01:182": [("Toute cosmologie", "qui y sont présentées.")],
 "w01:239": [("pour chacun de vous", "la voie est ouverte.")],
 "w02:27": [("Le nom qu'on lui donne", "semblable à lui.")],
 "w02:33": [("Ne permettez pas", "summum de la personnalité divine.")],
 "w02:57": [("Premièrement, la personnalité", "un avec vous."), ("Et deuxièmement", "ni explication.")],
 "w02:78": [("L'aptitude du Père", "multitude d'endroits.")],
 "w02:82": [("Les fluctuations", "leur propre âme.")],
 "w02:90": [("Et tout être humain", "le lui demandiez. »")],
 "w02:106": [("Aucune chose n'est nouvelle", "présente à tout instant.")],
 "w02:110": [("Et Dieu peut modifier", "il est volonté.")],
 "w02:156": [("Le concept de Dieu en tant que roi-juge", "Père de chaque être humain."), ("Dieu n'aime pas comme un père", "en tant que père.")],
 "w02:160": [("Lorsque vous méditez", "à un parent terrestre.")],
 "w02:168": [("Mais l'amour de Dieu", "l'amour n'est pas Dieu.")],
 "w02:186": [("Dieu n'est jamais", "rejet de sa miséricorde.")],
 "w02:196": [("Le Père céleste plein", "le pardon du Père."), ("Dieu en tant que père transcende", "en tant que juge.")],
 "w02:200": [("Dieu aime le pécheur parce que", "(potentiellement éternelle)"), ("L'amour de Dieu sauve", "détruit le péché.")],
 "w02:223": [("C'est ainsi, en vérité", "qui sont faites ».")],
 "w02:245": [("Dans la science, Dieu", "existe par soi-même"), ("La révélation est toutefois", "ses enfants terrestres.")],
 "w02:258": [("Ceux qui connaissent Dieu", "offrir à un autre.")],
 "w02:299": [("Notre Père ne se cache pas", "domaines universels.")],
 "w02:307": [("L'adoration se suffit", "de ce qu'il est.")],
 "w02:323": [("Dieu assure la souveraineté", "Dieu du libre arbitre.")],
 "w02:327": [("La consécration aimante", "au Père du Paradis.")],
 "w03:52": [("Et de même que le fragment", "élévation spirituelle.")],
 "w03:74": [("Les Fils divins sont", "agit par l'Esprit Infini")],
 "w03:78": [("dans l'administration des univers", "distinguer entre eux."), ("Rappelez-vous simplement", "le verbe expressif.")],
 "w03:82": [("La Trinité du Paradis est réelle.", "du Fils et de l'Esprit"), ("Le Père, le Fils et l'Esprit peuvent", "n'est pas la Trinité.")],
 "w03:135": [("La Déité peut être la cause", "n'est pas une Déité")],
 "w03:148": [("C'est l'unique et le seul", "des Fils de Dieu Créateurs")],
 "w03:152": [("Le milliard de mondes", "circuits des satellites du Paradis."), ("Chaque circuit est différent", "des sept Esprits des Circuits.")],
 "w03:160": [("Bien que leur vitesse", "veille dans la nuit ».")],
 "w03:227": [("Votre monde s'appelle Urantia", "système de Satania"),
             ("Satania porte le numéro 24", "appelé Jérusem."),
             ("L'univers local de Nébadon est composé", "secteur mineur d'Ensa."),
             ("Ce secteur mineur porte", "majeur de Splandon."),
             ("Il est le cinquième secteur", "l'univers des univers.")],
 "w03:266": [("La personnalité répond aussi", "circuit exclusif du Père"), ("Le Père Universel est infini", "cosmique de l'Ile du Paradis.")],
 "w03:274": [("Les réalités d'esprit", "sont réelles.")],
 "w03:278": [("La gravité d'esprit n'est jamais", "création matérielle.")],
 "w04:37": [("Au cours de l'expérience", "son superunivers natal.")],
 "w04:104": [("En tant que Père d'un univers local", "personnalité éducatrice de l'Esprit Infini.")],
 "w04:122": [("L'ordre de Micaël connait", "la plus humble.")],
 "w04:152": [("Les anges sont les esprits", "hautement individualisées."), ("Ils possèdent une nature", "êtres humains.")],
 "w04:170": [("ce sont les supernaphins", "par le Fils Éternel.")],
 "w04:174": [("Le premier acte", "carrière de filiation.")],
 "w04:209": [("L'exposé suivant", "habité par un Ajusteur."), ("nous avons choisi", "races humaines d'Urantia.")],
 "w04:227": [("Sur terre, vous étiez", "esprit rendu parfait.")],
 "w04:241": [("Lorsque, grâce au ministère", "est devenue sublime.")],
 "w04:280": [("Il y a en permanence", "en service sur Urantia.")],
 "w04:296": [("Nous pensons connaitre", "conjecture sur Uversa.")],
 "w04:300": [("Les finalitaires mortels ont pleinement", "statut spirituel ultime.")],
}
out = {}
for k in T:
    v = T[k]["verse"]; pieces = []; pos = 0
    for a, b in P[k]:
        a, b = A(a), A(b)
        i = v.find(a, pos)
        assert i >= 0, (k, a)
        j = v.find(b, i)
        assert j >= 0, (k, b)
        pieces.append(v[i:j + len(b)]); pos = j + len(b)
    out[k] = " … ".join(pieces)
assert set(out) == set(T)
json.dump(out, open(os.path.join(H, "fr", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k, q in out.items(): print(k, "|", q[:70], "…", q[-50:])
