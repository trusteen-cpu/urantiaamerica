import json, re, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
FR = json.load(open("../data/fr.json", encoding="utf-8"))
todo = json.load(open("work/todo_fr_c22.json", encoding="utf-8"))
Q = {
 "168.b5.q": ("168:0.7", "Je suis la résurrection et la vie ; quiconque croit en moi vivra, même s’il meurt."),
 "168.b25.q": ("168:4.5", "Aucune prière sincère ne reste sans réponse"),
 "169.b12.q": ("169:1.10", "mon fils que voici était mort et vit de nouveau. Il était perdu et il est retrouvé."),
 "169.b30.q": ("169:4.12", "Le Dieu des univers règne sur l’immense création, mais c’est le Père céleste qui envoie son esprit habiter votre mental."),
 "169.b36.q": ("169:1.2", "pendant que vous essayez de trouver Dieu, lui cherche également à vous trouver."),
 "170.b5.q": ("170:1.13", "Ses derniers mots, au sujet du royaume, étaient toujours : « Le royaume est en vous. »"),
 "170.b32.q": ("170:5.21", "L’Église dite chrétienne devient de cette manière la chrysalide où sommeille maintenant le concept du royaume selon Jésus."),
 "170.b38.q": ("170:5.19", "le royaume est la volonté de son Père céleste, dominante et transcendante, dans le cœur des croyants"),
 "171.b5.q": ("171:0.6", "le Fils de l’Homme n’est pas venu pour être servi, mais pour servir."),
 "171.b22.q": ("171:4.7", "Que de fois j’aurais voulu rassembler tes enfants comme une poule rassemble ses poussins sous ses ailes, mais vous n’avez pas voulu me laisser faire !"),
 "172.b5.q": ("172:1.3", "je voudrais provoquer l’effondrement des remparts de préjugés, de pharisaïsme et de haine devant la proclamation de l’amour du Père pour tous les hommes."),
 "172.b24.q": ("172:4.2", "Cette pauvre veuve a donné plus que tous les autres"),
 "173.b5.q": ("173:2.6", "L’autorité de Jésus résidait en lui-même et dans la suprématie éternelle de son Père."),
 "173.b12.q": ("173:1.7", "Ma maison sera appelée une maison de prières pour toutes les nations, mais vous en avez fait un repaire de voleurs."),
 "173.b35.q": ("173:5.3", "Je ne veux avoir personne ici en dehors de ceux qui se réjouissent d’accepter mon invitation, et qui me font l’honneur de porter les habits de noces que j’ai si libéralement mis à la disposition de tout le monde."),
 "174.b5.q": ("174:1.4", "Le péché est une expérience de la conscience des créatures ; il ne fait pas partie de la conscience de Dieu."),
 "174.b12.q": ("174:1.4", "quand vous aimez votre frère, vous lui avez déjà pardonné."),
 "174.b21.q": ("174:3.2", "mon Père n’est pas le Dieu des morts, mais celui des vivants."),
 "174.b35.q": ("174:1.3", "Le pardon divin est inévitable ; il est inaliénable et inhérent à la compréhension infinie de Dieu"),
 "175.b5.q": ("175:2.3", "Le Père et son Fils Créateur n’ont jamais cessé d’aimer les Juifs."),
 "175.b11.q": ("175:1.10", "celui qui veut être le plus grand parmi vous doit se faire le serviteur de tous."),
 "175.b31.q": ("175:2.3", "Dieu ne fait pas acception de personnes, et le salut est destiné aux Juifs aussi bien qu’aux Gentils."),
 "176.b5.q": ("176:3.10", "Vous avez reçu libéralement la vérité du ciel ; vous devriez donc la donner libéralement"),
 "176.b17.q": ("176:2.4", "Les yeux de la chair voient le Fils de l’Homme dans la chair, mais seul l’œil de l’esprit verra le Fils de l’Homme glorifié par le Père"),
 "176.b24.q": ("176:3.7", "La vérité est vivante. L’Esprit de Vérité conduit toujours les enfants de lumière dans de nouveaux domaines de réalité spirituelle et de service divin."),
 "176.b29.q": ("176:4.7", "Soyez donc toujours prêts à l’accueillir sur terre, de même qu’il se tient prêt à vous accueillir au ciel."),
}
ws = lambda s: re.sub(r"\s+", "", s)
out = {}
for k in todo:
    v, t = Q[k]
    assert ws(t) in ws(FR[v]), (k, t)
    out[k] = t
assert set(out) == set(todo)
json.dump(out, open("fr/quotes_c22.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(out))
