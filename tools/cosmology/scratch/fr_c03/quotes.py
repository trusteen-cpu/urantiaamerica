import json
Q = {
 "w04.011": "Cet évènement conduira certainement au fonctionnement parachevé de la première Trinité expérientielle —l’union des Créateurs Suprêmes, de l’Être Suprême et des Architectes du Maitre Univers. Cette Trinité est destinée à effectuer la suite de l’intégration évolutionnaire du maitre univers créé.",
 "w04.027": "Ils sont arrivés à la limite présentement accessible de perfection des créatures, mais non à la finalité de service des créatures. Ils ont fait l’expérience de l’adoration de la Déité dans sa plénitude, mais non de la finalité d’aboutissement de la Déité expérientielle.",
 "w04.042": "Certainement, surement et inexorablement, l’énigme de la Déité émergente de Dieu l’Ultime mettra au défi les citoyens devenus parfaits des univers établis, exactement comme leurs ancêtres évolutionnaires, qui se débattaient, furent jadis mis au défi par la recherche de Dieu le Suprême.",
 "w04.046": "…où nous pouvons déjà identifier le groupement d’au moins soixante-dix-mille agrégats de matière dont chacun est plus grand que n’importe quel superunivers du temps présent.",
 "w04.107": "En d’autres termes : à l’heure actuelle, environ quatre-vingt-quinze pour cent de l’action active de gravité cosmique de l’Ile du Paradis, évaluée d’après cette théorie de totalité, est occupée à contrôler des systèmes matériels situés au-delà des frontières des univers présentement organisés.",
 "w04.134": "…nous considérons le maitre univers … comme ayant des limitations, comme étant nettement délimité et borné à ses lisières extérieures par l’espace ouvert.",
 "w04.166": "L’Ultime et le Suprême sont comparables, mais non identiques, et l’Ultime n’est pas simplement une amplification du Suprême.",
 "w05.025": "…mais nos concepts concernant la pleine fonction de cette deuxième Trinité expérientielle paraissent impliquer quelque chose qui déborde même le domaine immensément étendu du maitre univers.",
 "w05.029": "Celle-ci est l’Absolu Trinité, l’union de Dieu le Suprême, de Dieu l’Ultime et du Consommateur non révélé de la Destinée de l’Univers.",
 "w05.040": "…la destinée est probablement consommée par l’acte du Consommateur de la Destinée de l’Univers, et cet acte fait probablement intervenir le Suprême et l’Ultime, dans l’Absolu Trinité.",
 "w05.042": "La Trinité Ultime, évoluant présentement, sera finalement constituée de l’Être Suprême, des Personnalités Créatrices Suprêmes et des Architectes absonites du Maitre Univers…",
 "w05.045": "Nous sommes toutefois certains de ceci : la Trinité du Paradis existentielle est infinie et l’Ultime Trinité expérientielle est subinfinie, mais l’Absolu Trinité n’est pas aussi facile à classifier.",
 "w05.052": "Certainement, surement et inexorablement, l’énigme de la Déité émergente de Dieu l’Ultime mettra au défi les citoyens devenus parfaits des univers établis, exactement comme leurs ancêtres évolutionnaires, qui se débattaient, furent jadis mis au défi par la recherche de Dieu le Suprême.",
 "w05.086": "Parmi tous ceux qui s’élèvent à l’Ile éternelle, seuls ceux qui arrivent ainsi sont les enfants de l’éternité…",
 "w05.099": "…Mais, à mesure que l’homme s’élève, qu’il progresse intérieurement, le panorama de cette procession d’évènements s’agrandit de sorte qu’il en discerne de mieux en mieux l’ensemble.",
 "w05.115": "Et il semblerait aussi que l’inconditionné soit aussi illimité, du moins d’un point de vue qualitatif, bien que nous n’en soyons pas aussi surs en ce qui concerne les relations quantitatives.",
 "w05.120": "Si nous admettons l’hypothèse d’un cosmos-infini — une sorte de cosmos illimité dépassant le maitre univers — et si nous concevons que les développements finals de la Trinité Absolue auront lieu à un tel stade superultime d’action, …",
 "w05.158": "Par rapport à toute la réalité actualisée, non spirituelle, impersonnelle et non volitive, le Paradis est l’absolu des archétypes.",
 "w05.164": "Ces trois Déités expérientielles étaient potentielles dans la Trinité existentielle, la Trinité du Paradis. Mais leur émergence dans l’univers comme personnalités de pouvoir dépend, pour une part, de leur propre fonctionnement expérientiel dans les univers de pouvoir et de personnalité…",
 "w05.166": "…La synthèse personnalité-pouvoir qui se produit actuellement en liaison avec l’évolution de l’Être Suprême en est l’illustration.",
 "w05.175": "À ce niveau supercréateur, la Déité fait l’expérience de l’épuisement du potentiel personnalisable, rencontre la complétude de la divinité…",
 "w05.179": "La Trinité Ultime s’unifie expérientiellement en se parachevant, mais nous doutons vraiment qu’une telle unification, aussi complète, soit possible pour la Trinité Absolue. Toutefois, notre concept de la Trinité éternelle du Paradis nous remet constamment en mémoire que la trinitisation de la Déité peut accomplir ce qui autrement est irréalisable…",
 "w05.184": "Dans la Trinité des Trinités, l’infini expérientiel parvient à s’identifier à l’infini existentiel, et tous deux ne font qu’un dans le JE SUIS préexpérientiel et préexistentiel.",
 "w05.200": "Nous ne le savons pas, mais nous sommes convaincus que cela conduirait directement à la réalisation du JE SUIS comme susceptible d’être atteint par expérience.",
}
t = json.load(open('work/todo_fr_c03.json', encoding='utf-8'))
assert list(t) == list(Q), set(t) ^ set(Q)
json.dump(Q, open('fr/quotes_c03.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
