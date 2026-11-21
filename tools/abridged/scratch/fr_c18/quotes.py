import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
todo = json.load(open(os.path.join(BASE, "work", "todo_fr_c18.json"), encoding="utf-8"))
Q = {
 "135.b35.q": ("135:8.6", "Celui-ci est mon fils bienaimé en qui j’ai trouvé mon plaisir."),
 "136.b5.q": ("136:10.1", "Pour toutes les autres questions, comme pour celles dont la décision est maintenant enregistrée, je m’engage envers toi à me soumettre à la volonté de mon Père."),
 "136.b33.q": ("136:6.8", "Il venait révéler son Père céleste à ses enfants terrestres, tout en cherchant à amener ses enfants terrestres à se joindre à lui dans un effort sincère pour vivre selon la volonté du Père qui est aux cieux."),
 "138.b5.q": ("138:8.9", "Rien ne semblait jamais aussi important à Jésus que l’humain individuel qui pouvait se trouver en sa présence immédiate."),
 "138.b17.q": ("138:3.6", "les bienportants n’ont pas besoin d’un médecin, mais plutôt les malades ? Je suis venu non pour appeler les justes, mais les pécheurs."),
 "139.b19.q": ("139:4.6", "Mes petits enfants, aimez-vous les uns les autres."),
 "140.b5.q": ("140:1.5", "le royaume que vous prêchez est Dieu en vous."),
 "140.b45.q": ("140:10.7", "Oui, Simon, tous les hommes sont fils de Dieu, et c’est la bonne nouvelle que vous allez proclamer."),
 "141.b5.q": ("141:2.2", "quand la volonté du Père devient vraiment votre volonté, alors vous êtes en toute vérité dans le royaume"),
}
assert set(Q) == set(todo), set(todo) ^ set(Q)
out = {}
for k in todo:
    v, t = Q[k]
    assert t in todo[k]["verses"][v], k
    out[k] = t
json.dump(out, open(os.path.join(BASE, "fr", "quotes_c18.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(out))
