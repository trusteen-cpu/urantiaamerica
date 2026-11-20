# -*- coding: utf-8 -*-
import json, os, sys
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools"
sys.path.insert(0, H)
import amq
D = os.path.join(H, "doctrine")
todo = json.load(open(os.path.join(D, "work", "todo_fr_c05.json"), encoding="utf-8"))
S = json.load(open(os.path.join(D, "src", "c05.json"), encoding="utf-8"))
C = {
 "ch23:9": ("Et tout l’agencement", "confiné en soi"),
 "ch23:18": ("Jésus n’ait pas enduré", "offensé et implacable"),
 "ch23:29": ("L’esprit du Père qui est aux cieux", "ton Père qui est aux cieux."),
 "ch23:31": ("Le salut vient", "renoncement à la chair"),
 "ch23:38": ("La possibilité de reconnaitre", "toujours ascendante."),
 "ch24:3": ("La croyance a atteint", "domine effectivement la manière de vivre."),
 "ch24:34": ("La foi correspondante", "progressif à la Déité."),
 "ch24:46": ("Mais les doutes honnêtes", "l’homme accompli."),
 "ch25:16": ("Le grand effort", "faire la volonté de Dieu."),
 "ch25:23": ("Mais je vous le dis", "d’aucune façon."),
 "ch26:3": ("Le chemin allant", "il ne périra jamais."),
 "ch26:7": ("Je vous ai apporté", "royaume spirituel de notre Père."),
 "ch26:12": ("Vous survivrez", "le don de la vie éternelle."),
 "ch26:14": ("La matrice mentale", "survivants endormis."),
 "ch26:21": ("Sur les mondes des maisons", "d’un autre corps"),
 "ch26:26": ("le système énergétique doit continuer", "libre arbitre."),
 "ch26:29": ("Cela ne signifie pas", "et définitif."),
 "ch26:36": ("Sur terre, vous étiez", "esprit rendu parfait."),
 "ch27:3": ("La religion est l’expérimentation", "durant l’incarnation."),
 "ch27:7": ("Toutes les activités humaines", "humains et suprahumains."),
 "ch27:14": ("L’esprit divin établit", "qui vous conduisent vers Dieu."),
 "ch27:16": ("Quand un être moral", "faire un tel choix"),
 "ch27:27": ("La religion de l’esprit signifie", "que peu ou aucun de ces efforts."),
 "ch27:29": ("La religion du mental vous attache", "les réalités éternelles."),
 "ch27:32": ("Les religions d’autorité exigent", "diversité des croyances."),
 "ch27:40": ("La raison est la preuve", "la philosophie apporte l’unité"),
 "ch27:50": ("La religion authentique", "de zèle et de courage"),
 "ch27:52": ("l’expérience divine de trouver Dieu", "votre expérience personnelle"),
}
out = {}
keys = list(todo.keys()) if isinstance(todo, dict) else list(todo)
for k in keys:
    r = S[k]["cit"]
    q = amq.cut("fr", r, *C[k])
    assert amq.check("fr", r, q), k
    out[k] = q
    print(k, r, round(len(q) / len(S[k]["q"]), 2))
missing = [k for k in C if k not in out]
print("extra:", missing, "n=", len(out))
json.dump(out, open(os.path.join(D, "fr", "quotes_c05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
