import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
Q = {
 "w12.009": "Ces investigateurs aboutissent à la conclusion étonnante que l’univers central et les sept superunivers qui l’entourent n’emploient présentement que cinq pour cent du fonctionnement actif de l’emprise de gravité absolue du Paradis.",
 "w12.010": "dans les univers de l’espace extérieur où nous pouvons déjà identifier le groupement d’au moins soixante-dix-mille agrégats de matière dont chacun est plus grand que n’importe quel superunivers du temps présent.",
 "w12.072": "Un superunivers est ancré dans la lumière et la vie dès que tous les univers locaux qui le composent sont ainsi rendus parfaits, mais aucun des sept superunivers n’a encore atteint un niveau de progrès qui s’en approche, même de loin.",
 "w12.111": "et le finalitaire fait maintenant face au défi de Dieu l’Ultime.",
 "w12.125": "L’Ultime consiste en une unité de nombreuses qualités considérées diversement. Sa conception par les hommes devrait bien inclure au moins les phases d’ultimité qui gèrent l’autorité, qui sont personnellement expérimentables et qui unifient par des tensions, mais la Déité extériorisée comporte beaucoup d’autres aspects non révélés.",
 "w12.132": "Le mental infini ignore le temps, le mental ultime transcende le temps, le mental cosmique est conditionné par le temps.",
 "w12.150": "Ils sont omnipersonnels — ils sont avant la personnalité, ils sont la personnalité et ils sont après la personnalité.",
 "w12.155": "Le Suprême est l’unification de la Trinité comprise par les êtres finis. L’Ultime est l’unification de la Trinité du Paradis comprise par les êtres absonites.",
 "w12.169": "Les Trinités postérieures à Havona sont expérientielles. Elles sont inhérentes à la création dans le maitre univers de deux niveaux subabsolus et évolutionnaires de manifestations de personnalité-pouvoir.",
 "w12.194": "la Trinité du Paradis existentielle est infinie et l’Ultime Trinité expérientielle est subinfinie, mais l’Absolu Trinité n’est pas aussi facile à classifier.",
 "w12.206": "Et il semblerait aussi que l’inconditionné soit aussi illimité, du moins d’un point de vue qualitatif, bien que nous n’en soyons pas aussi surs en ce qui concerne les relations quantitatives.",
 "w12.210": "la destinée est probablement consommée par l’acte du Consommateur de la Destinée de l’Univers, et cet acte fait probablement intervenir le Suprême et l’Ultime, dans l’Absolu Trinité.",
 "w13.027": "autant que nous le sachions, ces mondes ancrés dans la lumière et la vie sont destinés à poursuivre leur course dans tous les âges éternels des temps futurs.",
 "w13.036": "mais nos concepts concernant la pleine fonction de cette deuxième Trinité expérientielle paraissent impliquer quelque chose qui déborde même le domaine immensément étendu du maitre univers.",
 "w13.054": "À ce niveau supercréateur, la Déité fait l’expérience de l’épuisement du potentiel personnalisable, rencontre la complétude de la divinité",
 "w13.057": "En dernière analyse, les fragments du Père doivent être le don du Dieu absolu aux créatures dont la destinée englobe la possibilité d’atteindre Dieu en tant qu’absolu.",
 "w13.072": "Cet espace pénétré s’étend horizontalement vers l’extérieur, depuis la proximité du Paradis périphérique à travers le quatrième niveau d’espace extérieur et au-delà de la périphérie du maitre univers ; mais de combien au-delà, nous ne le savons pas.",
 "w13.077": "Ils postulent donc une création additionnelle et non révélée au-delà du quatrième et extrême niveau de l’espace extérieur, la possibilité d’un univers d’infinité, toujours croissant et ne finissant jamais.",
 "w13.126": "Sous l’impulsion directrice de l’Être Suprême évoluant, toute la réalité finie de l’espace-temps est engagée dans une mobilisation toujours ascendante et une unification en voie de perfectionnement (synthèse personnalité-pouvoir) de toutes les phases et valeurs de la réalité finie",
 "w13.141": "Ces trois Déités expérientielles étaient potentielles dans la Trinité existentielle, la Trinité du Paradis. Mais leur émergence dans l’univers comme personnalités de pouvoir dépend, pour une part, de leur propre fonctionnement expérientiel dans les univers de pouvoir et de personnalité, et, pour une autre part, des accomplissements expérientiels des Créateurs et des Trinités postérieurs à Havona.",
 "w13.147": "L’évolution du Tout-Puissant pouvoir de Suprématie par diverses synthèses de divinité dans les univers évoluants se traduisit par une nouvelle présence de pouvoir de la Déité, qui se coordonna avec la personne spirituelle du Suprême dans Havona au moyen du Mental Suprême.",
 "w13.157": "Dieu le Suprême est lui-même un participant volitif et créateur de l’actualisation de sa propre déité.",
 "w13.162": "Le Suprême est l’unification de la Trinité comprise par les êtres finis. L’Ultime est l’unification de la Trinité du Paradis comprise par les êtres absonites.",
 "w13.164": "Les Moniteurs de Mystère sont, pour les êtres humains, ce qu’est la Trinité du Paradis pour l’Être Suprême.",
 "w13.179": "L’Ultime et le Suprême sont comparables, mais non identiques, et l’Ultime n’est pas simplement une amplification du Suprême.",
 "w13.184": "Enfin, sur le niveau absolu, l’Absolu de Déité et l’Absolu Non Qualifié sont inséparables et indiscernables en présence de l’Absolu Universel.",
 "w13.205": "Les philosophes des univers postulent une Trinité des Trinités, une Trinité Infinie existentielle-expérientielle, mais ils sont incapables d’envisager sa personnalisation",
 "w13.216": "Le premier niveau consiste en trois Trinités. Le deuxième niveau existe comme l’association de personnalité comprenant des personnalités de Déité d’évolution expérientielle, d’extériorisation expérientielle et expérientielles-existentielles.",
 "w13.219": "Toutefois, notre concept de la Trinité éternelle du Paradis nous remet constamment en mémoire que la trinitisation de la Déité peut accomplir ce qui autrement est irréalisable. Nous posons donc en postulat l’apparition en son temps du Suprême-Ultime et la possible factualisation-trinitisation de Dieu l’Absolu.",
 "w13.226": "En effet, nous percevons que les relations cosmiques de l’Absolu Universel deviendront de plus en plus insondables dans la proportion où les univers matériels et leur administration spirituelle continueront leur expansion.",
 "w13.231": "C’est le moment statique hypothétique de l’éternité ; les actuels sont encore inclus dans leurs potentiels, et les potentiels ne sont pas encore apparus dans l’infinité du JE SUIS.",
}
todo = json.load(open(os.path.join(H, "work", "todo_fr_c07.json"), encoding="utf-8"))
assert set(todo) == set(Q), set(todo) ^ set(Q)
Q = {k: Q[k] for k in todo}
json.dump(Q, open(os.path.join(H, "fr", "quotes_c07.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(Q))
