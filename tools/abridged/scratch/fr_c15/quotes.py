import json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
data = json.load(open('../data/fr.json', encoding='utf-8'))
Q = {
 "110.b5.q": ("110:2.1", "Les Ajusteurs respectent la souveraineté de votre personnalité ; ils se soumettent toujours à votre volonté."),
 "110.b37.q": ("110:7.10", "Pour atteindre la personnalité, nous dépendons de la volonté humaine."),
 "111.b18.q": ("111:3.7", "ce que vous commencez dans le temps, vous l’achèverez surement dans l’éternité — si cela mérite d’être achevé."),
 "112.b39.q": ("112:7.19", "si vous le désirez réellement, à coup sûr, l’héritage des âges est à vous"),
 "114.b5.q": ("114:7.17", "le Père lui-même vous aime"),
 "114.b33.q": ("114:7.17", "Urantia n’est pas une orpheline cosmique stigmatisée par le péché et coupée, par la rébellion, de la vigilante protection divine."),
 "114.b38.q": ("114:7.17", "Vous autres mortels habitant présentement Urantia, vous êtes tout aussi affectueusement chéris et fidèlement gardés, et même davantage, que si votre sphère n’avait jamais été trahie par un Prince Planétaire sans foi."),
 "115.b18.q": ("115:3.16", "non seulement chaque décision humaine actualise une nouvelle réalité dans l’expérience humaine, mais elle ouvre aussi une nouvelle capacité de croissance humaine."),
 "116.b23.q": ("116:4.11", "L’univers local est le point de départ pour les personnalités qui sont les plus éloignées de Dieu et qui peuvent donc faire l’expérience, au plus haut degré, de l’ascension spirituelle dans l’univers"),
 "116.b33.q": ("116:6.8", "Tous font leur possible, leur meilleur effort personnel pour aboutir. Tous, personnellement, participent à la destinée."),
 "117.b23.q": ("117:4.6", "tandis que nous cherchons à exprimer notre moi, le Suprême s’efforce en nous et avec nous d’exprimer la déité."),
 "117.b47.q": ("117:6.27", "nul mortel connaissant Dieu ne peut jamais être solitaire dans son voyage à travers le cosmos, car il sait que le Père fait, à ses côtés, chaque pas du chemin, tandis que la route même qu’il poursuit est la présence du Suprême."),
 "118.b32.q": ("118:6.5", "Ce qu’un fils désire et que le Père veut arrivera en toute certitude."),
 "118.b49.q": ("118:10.17", "Le royaume de Dieu est dans le cœur des hommes"),
}
todo = json.load(open('work/todo_fr_c15.json', encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
out = {}
for k in todo:
    v, s = Q[k]
    assert s in data[v], k
    out[k] = s
json.dump(out, open('fr/quotes_c15.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(out))
