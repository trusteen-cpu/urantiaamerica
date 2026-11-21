import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
todo = json.load(open(os.path.join(BASE, "work", "todo_fr_c17.json"), encoding="utf-8"))
# key: (verse, start, end)  -> slice of official verse from start through end (inclusive)
spec = {
"128.b4.q": ("128:7.2", "Indépendamment de qui je suis", "Père du Paradis."),
"128.b10.q": ("128:1.5", "Nous avons un Souverain", "sans toutefois pécher."),
"129.b5.q": ("129:4.7", "Jésus est le chemin nouveau", "à l’éternité."),
"129.b25.q": ("129:4.7", "Vous ne pouvez pas aspirer", "par les mêmes moyens."),
"130.b5.q": ("130:2.6", "nul homme n’est un étranger", "connait Dieu."),
"130.b17.q": ("130:2.10", "La volonté est la manifestation", "semblable à Dieu."),
"130.b21.q": ("130:3.7", "Le vrai maitre maintient", "toujours un élève."),
"130.b38.q": ("130:8.2", "Ton problème n’est pas", "le Père t’a déjà trouvé"),
"131.b38.q": ("131:8.5", "Dieu récompense les hommes", "pour ce qu’ils font"),
"131.b47.q": ("131:10.8", "Enfin, j’ai une religion", "salut éternel."),
"133.b14.q": ("133:2.2", "La considération et les soins", "créative et spirituelle."),
"133.b32.q": ("133:7.12", "Le mental suprêmement heureux", "qui est aux cieux."),
"134.b5.q": ("134:8.8", "Que la volonté de mon Père", "soit faite"),
"134.b39.q": ("134:8.9", "Un après-midi de fin d’été", "de son univers."),
}
out = {}
for k in todo:
    v, a, b = spec[k]
    t = todo[k]["verses"][v]
    i = t.index(a)
    j = t.index(b, i) + len(b)
    out[k] = t[i:j]
json.dump(out, open(os.path.join(BASE, "fr", "quotes_c17.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k, v in out.items():
    print(k, v)
