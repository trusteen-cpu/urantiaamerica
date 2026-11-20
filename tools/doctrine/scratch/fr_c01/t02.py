# -*- coding: utf-8 -*-
import json
from common import save, OUT

cur = json.load(open(OUT, encoding="utf-8"))
t = cur["ch00:7"]
fix = {
 "07, 10, 14, 17": "07, 10, 14 et 17",
 "20, 29, 13, 26": "20, 29, 13 et 26",
 "06, 28, 08, 12": "06, 28, 08 et 12",
 "22, 24, 27, 25, —": "22, 24, 27, 25 et —",
 "19, 09, —, 23, 21": "19, 09, —, 23 et 21",
 "03, 02, 04, 01, 18, 15, 16, 05": "03, 02, 04, 01, 18, 15, 16 et 05",
}
for r in t["rows"]:
    r[3] = fix.get(r[3], r[3])

U = {
 "ch00:7": t,
 "ch02:label": "Chapitre 2",
 "ch02:title": "La Trinité",
 "ch02:sub": "Pourquoi Dieu est trois et pourtant un",
 "ch02:0": "Comme nous l’avons vu au chapitre 1, la première relation du JE SUIS fut celle du Père et du Fils, et, en présence du Père et du Fils, apparut l’Esprit Infini. Comment ces trois sont-ils un ? Le Livre d’Urantia répond à cette question par la doctrine de la Trinité du Paradis. Ce chapitre définit ce qu’est la Trinité, examine pourquoi les révélateurs appellent la Trinité la seule inévitabilité de l’univers, demande comment les trois personnes se distinguent de l’unique Trinité, et considère enfin ce que cette doctrine signifie pour la foi et la vie humaines.",
 "ch02:1": "1. Définition : la Déité indivise de trois personnes",
 "ch02:2": "Dès son ouverture, le fascicule 10, « La Trinité du Paradis », définit la Trinité en une seule phrase. Dieu n’est pas divisé en trois, et les trois personnes ne se dissolvent pas pour disparaitre dans l’un.",
 "ch02:4": "Cette définition a deux axes. L’un est que les trois personnes sont toutes originelles, coordonnées et coexistantes ; l’autre est que les trois forment une unicité divine. Les trois personnes ne sont pas des copies les unes des autres : « aucune n’est une copie, chacune est originale, toutes les trois sont unies » (10:2.6). La relation des trois personnes est décrite selon une séquence, mais cette séquence n’est pas un avant et un après dans le temps ; c’est une structure de relation. Le Père donne au Fils la plénitude de lui-même, et le Père et le Fils constituent ensemble la troisième personne.",
 "ch02:6": "Le Fils procède de l’effusion de soi du Père, et l’Esprit de l’effusion conjointe du Père et du Fils, et pourtant aucun des deux n’est venu à l’existence plus tard. Tous trois sont éternels, et c’est précisément cette relation d’effusion qui détermine la place unique de chacun. L’Introduction distingue au moyen de titres qui est chacune des trois personnes.",
 "ch02:7": {"cap": "Tableau 2.1  Les titres et la place unique des trois Déités", "rows": [
   ["Déité", "Titre dans l’Introduction", "Description dans le fascicule 10", "Source"],
   ["Dieu le Père", "Créateur, Contrôleur et Soutien ; la Première Personne de la Déité", "L’infinie personnalité-père, la source illimitée de personnalité", "0:2.12, 10:2.4"],
   ["Dieu le Fils", "Créateur Coordonné, Contrôleur d’Esprit et Administrateur Spirituel ; la Deuxième Personne de la Déité", "L’absolu de personnalité non qualifié, la parfaite révélation de la nature personnelle de Dieu", "0:2.13, 10:2.4"],
   ["Dieu l’Esprit", "Acteur Conjoint, Intégrateur Universel, Dispensateur du Mental ; la Troisième Personne de la Déité", "La personnalité conjointe, l’unique conséquence personnelle de l’union perpétuelle du Père-Fils", "0:2.14, 10:2.4"]]},
 "ch02:8": "La Trinité elle-même est-elle alors une quatrième personne ? Le fascicule 104, « Croissance du concept de Trinité », répond clairement que non. La Trinité est une réalité de Déité unique, réelle bien que n’étant pas une personnalité.",
 "ch02:10": "2. Fondements : pourquoi il doit y en avoir trois",
 "ch02:11": "Les révélateurs ne considèrent pas la Trinité comme une possibilité parmi d’autres. Tout le reste dans l’univers, disent-ils, aurait pu être autrement, mais non la Trinité.",
 "ch02:13": "Pourquoi est-elle inévitable ? Le premier fondement se trouve dans la paternité elle-même. Une Source-Centre Première dépourvue d’un Fils « ne pouvait en aucun sens du terme être considérée comme le Père Universel » (10:3.5). Le même paragraphe le dit brièvement : « la paternité n’est pas réelle sans filiation » (10:3.5). Pour que Dieu soit Père, il doit éternellement y avoir un Fils. Et, de fait, il n’y a jamais eu de moment où le Père était seul.",
 "ch02:15": "Le deuxième fondement se trouve dans la nature de la personnalité divine. La personnalité n’est pas enfermée en elle-même ; elle se partage.",
 "ch02:17": "Le partage n’est pas un défaut de la personnalité divine, mais sa nature même. Le fait que le Père partage la réalité de l’être avec le Fils et l’Esprit est la première expression de cette nature, et toute délégation et toute effusion qui ont lieu dans l’univers en sont le prolongement. Le troisième fondement est la libération des limites de l’absoluité. Si le Père avait existé seul en tant que personnalité absolue, cette absoluité serait devenue une entrave. L’ouverture du fascicule 10 décrit ainsi cette libération.",
 "ch02:19": "Ce qui est absolu n’a pas de marge de mouvement, et une volonté infinie doit trouver un lieu où s’exprimer. La Trinité sauvegarde les deux à la fois. L’absoluité de la Déité est pleinement préservée dans la Trinité, et la volonté personnelle du Père s’exprime sans limite par le Fils et l’Esprit et par leurs enfants. En conférant l’absoluité de personnalité au Fils, le Père échappe à cette entrave.",
 "ch02:21": "Quatrièmement, les révélateurs notent aussi qu’il faut un minimum de trois personnes pour former un groupe social, mais ils ajoutent que « c’est la moindre des raisons pour croire à l’inévitabilité de l’Acteur Conjoint » (10:2.3). Le cinquième fondement vient du côté de la philosophie. Dans la pensée humaine, un Dieu solitaire finit par être réduit à un Absolu impersonnel. « La personnalité chez la Déité exige que cette Déité existe en relation avec d’autres Déités personnelles égales. » (104:2.2) Rassemblés, ces fondements sont les suivants.",
 "ch02:22": {"cap": "Tableau 2.2  Cinq fondements de l’inévitabilité de la Trinité", "rows": [
   ["Fondement", "Logique", "Source"],
   ["La paternité", "Une source sans Fils n’est pas un Père ; la paternité n’est pas réelle sans filiation", "10:3.5"],
   ["La nature de la personnalité", "La personnalité divine n’est pas centrée sur elle-même, mais se partage", "10:1.3"],
   ["La libération de l’absoluité", "En conférant l’absoluité de personnalité au Fils, le Père échappe aux entraves de l’absolutisme de personnalité", "10:0.1, 10:3.7"],
   ["Le groupe social minimal", "Trois personnes forment un groupe social minimal (la moindre des raisons)", "10:2.3"],
   ["La préservation du concept de personnalité", "Sans relation avec d’autres personnalités égales, Dieu est réduit à un Absolu panthéiste", "104:2.2"]]},
 "ch02:23": "3. Structure : trois personnes et une union",
 "ch02:24": "Comment les trois personnes et l’unique Trinité existent-elles ensemble ? Tout en admettant que ce mystère ne peut être entièrement résolu, les révélateurs offrent une comparaison grossière que l’homme peut saisir.",
 "ch02:26": "Le sens de cette comparaison est que les trois personnes travaillant ensemble en tant qu’individus diffèrent de leur action en tant que Trinité. Les révélateurs disent : « En tant que personnes, ils peuvent collaborer comme ils le veulent, mais cela n’est pas la Trinité. » (10:4.4) Et les fonctions de la Trinité sont davantage que la somme des attributs des trois. De même qu’une famille ou une communauté humaine est davantage que la somme de ses membres, « Le potentiel du groupe dépasse toujours de beaucoup la simple somme des attributs des individus qui le composent. » (10:5.2) Cette distinction devient plus claire lorsqu’on compare les Déités personnelles avec la Trinité.",
 "ch02:27": {"cap": "Tableau 2.3  Les Déités personnelles comparées à la Trinité", "rows": [
   ["Point de comparaison", "Le Père, le Fils et l’Esprit (en tant que personnes)", "La Trinité du Paradis", "Source"],
   ["Ce qu’ils possèdent", "Ils ont des attributs", "Des fonctions plutôt que des attributs (administration de la justice, attitudes de totalité, action coordonnée, supercontrôle cosmique)", "10:5.1"],
   ["La justice", "La justice n’est l’attitude personnelle d’aucun d’entre eux", "La justice est l’attitude trinitaire de ces trois personnalités d’amour, de miséricorde et de ministère", "10:6.2"],
   ["Objet d’intérêt", "Le Père manifeste l’attitude personnelle d’amour dans tous ses actes", "S’intéresse à la planète totale, à l’univers total, au grand univers total", "10:7.6, 10:7.2"],
   ["Manière de collaborer", "En tant que personnes, ils peuvent collaborer comme ils le veulent", "En tant que trois Déités, ils ne peuvent collaborer d’une manière non trinitaire", "10:4.4"]]},
 "ch02:28": "Cette structure apparait aussi dans la manière dont le Père agit dans l’univers. Le Père fait beaucoup de choses par les Fils et par l’Esprit, mais ce qu’il fait en tant que Déité totale, il ne le fait que dans la Trinité. Le fascicule 10, section 3, expose ainsi ces sept manières.",
 "ch02:29": {"cap": "Tableau 2.4  Comment la Source-Centre Première fonctionne hors de Havona", "rows": [
   ["Fonction", "Canal", "Source"],
   ["Comme créateur", "Par les Fils Créateurs, ses petits-fils", "10:3.10"],
   ["Comme contrôleur", "Par le centre de gravité du Paradis", "10:3.11"],
   ["Comme esprit", "Par le Fils Éternel", "10:3.12"],
   ["Comme mental", "Par le Créateur Conjoint", "10:3.13"],
   ["Comme Père", "Contact parental avec toutes les créatures par son circuit de personnalité", "10:3.14"],
   ["Comme personne", "Par ses fragments exclusifs ; chez les hommes, par les Ajusteurs de Pensée", "10:3.15"],
   ["Comme Déité totale", "Seulement dans la Trinité du Paradis", "10:3.16"]]},
 "ch02:30": "4. L’œuvre de la Trinité : la justice et le total",
 "ch02:31": "La fonction représentative de la Trinité dans l’univers est la justice. C’est là que la doctrine de la Trinité touche la vie morale de l’homme. L’origine de la loi, son administration, sa révélation et son application ont chacune une place différente, et l’application de la loi, la justice, appartient à la Trinité (10:6.1).",
 "ch02:33": "Cet enseignement dit deux choses à l’homme. Premièrement, lorsque l’homme rencontre Dieu en tant que personne, il rencontre toujours l’amour et la miséricorde. Deuxièmement, la justice n’est pas l’humeur ou la représaille d’une seule personne, mais un jugement collectif et total. L’enseignement de Jésus selon lequel la justice n’est jamais un acte personnel, mais toujours une fonction de groupe, repose sur ce principe (104:2.5). Les révélateurs disent que la justice et la miséricorde ne sont pas finalement en conflit : « Quand l’équité de la Trinité et l’amour miséricordieux du Père Universel sont complètement perçus et pleinement compris, ils coïncident. » (10:6.18)",
 "ch02:34": "Pourtant, l’homme dans le temps ne voit pas toujours cette coïncidence, car la Trinité s’occupe du tout, tandis que l’homme vit à l’intérieur d’une partie. Les révélateurs reconnaissent franchement cet écart.",
 "ch02:36": "Cet aveu établit un ordre important pour la foi. L’homme peut être certain de l’amour personnel du Père. Mais les actes de la Trinité dirigés vers le tout ne sont pas maintenant pleinement compris ; cette compréhension est donnée dans le progrès de l’éternité. Même devant ce qu’il ne comprend pas, l’homme n’a donc aucune raison de douter de l’amour.",
 "ch02:37": "5. Les malentendus sur la Trinité et les réponses du texte",
 "ch02:38": "Dans la pensée humaine, la Trinité a souvent été confondue avec d’autres idées. Revenant sur la manière dont ce concept a grandi sur Urantia, le fascicule 104 distingue la Trinité révélée des croyances aux triades de la religion évolutionnaire (104:0.1). Les triades de la religion évolutionnaire sont nées d’associations d’expérience, comme les trois phalanges des doigts ou les trois pieds d’un siège, mais la Trinité révélée est une vérité sur la réalité de Dieu. Le texte donne des réponses claires à plusieurs malentendus.",
 "ch02:39": {"cap": "Tableau 2.5  Les malentendus sur la Trinité et les réponses du texte", "rows": [
   ["Malentendu", "La réponse du texte", "Source"],
   ["La Trinité est un assemblage de trois dieux", "« Une vraie conception trinitaire ne consiste pas simplement à grouper ensemble trois dieux séparés. » (104:1.7)", "104:1.7"],
   ["La Trinité est le produit d’un mental qui aime les triades", "Il ne faut pas confondre le concept de Trinité de la religion révélée avec les croyances aux triades des religions évolutionnaires", "104:0.1"],
   ["La Trinité est une quatrième personne", "Elle n’est pas une personnalité, mais une réalité véritable et absolue, compatible avec les trois personnes", "104:2.4"],
   ["La Trinité n’est qu’une union fonctionnelle", "La Trinité n’est pas une triunité ; elle est une Déité indivise et indivisible", "104:3.15"],
   ["Celui qui vint sur Urantia était la Deuxième Personne de la Déité elle-même", "C’est vrai en esprit, mais ce n’est pas exact en fait ; les Micaëls Créateurs ne sont pas la personnalité absolue", "104:1.13"]]},
 "ch02:40": "Beaucoup de ces malentendus proviennent d’une histoire où la vérité de la Trinité n’a jamais été pleinement transmise à l’homme. Cette vérité a été révélée bien des fois et obscurcie bien des fois. Jésus lui-même l’enseigna, mais ses disciples ne la reçurent pas correctement.",
 "ch02:42": "Mais les révélateurs ajoutent que la compréhension d’aucune époque n’atteint la Trinité telle qu’elle est. La Trinité fonctionne à tous les niveaux, tandis que l’homme demeure au niveau fini.",
 "ch02:44": "Le dernier point concerne la compréhension chrétienne de la Trinité. Les révélateurs jugent que, bien que ce concept « fût erroné en fait, il était pratiquement vrai sous le rapport des relations spirituelles » (104:1.13). Cette question est reprise aux chapitres 19 et 32.",
 "ch02:45": "6. Conséquences : l’amour et la loi, et la Trinité qui grandit",
 "ch02:46": "Qu’ajoute la doctrine de la Trinité à la foi humaine ? Par la foi, l’homme réalise l’amour de Dieu, et pourtant l’univers se meut selon des lois ordonnées. Comment comprendre l’écart entre un Père aimant et des lois apparemment impassibles ?",
 "ch02:48": "Si l’homme ne connait que l’amour du Père et non la souveraineté de la Trinité, sa foi est ébranlée devant les lois de l’univers. Inversement, s’il ne voit que la loi et ne connait pas le Père, l’univers devient une froide machine. La Trinité révèle que les deux sont un dans la même Déité. La Trinité n’est pas non plus enfermée dans l’éternité. L’Introduction dit que la Trinité originelle est existentielle et qu’elle était inévitable (0:12.1), et elle ajoute que les Déités expérientielles qui étaient potentielles en elle apparaissent dans le temps.",
 "ch02:50": "La Trinité originelle est complète, mais la manifestation de cette Trinité dans les univers du temps et de l’espace est encore en cours. Son premier fruit est Dieu le Suprême, et l’homme prend part à cette manifestation par sa propre expérience. La Trinité n’est donc pas la doctrine d’une éternité lointaine, mais une doctrine liée aux choix que l’homme fait aujourd’hui. Le chapitre 4 examine ce lien en détail.",
 "ch02:51": "Pour conclure : Dieu qui est trois et un",
 "ch02:52": "Dieu est trois, parce que la paternité n’est pas réelle sans filiation, parce que la personnalité divine se partage, et parce que le Père, en conférant l’absoluité de personnalité au Fils, échappe aux entraves de l’absoluité. Dieu est un, parce que les trois personnes constituent une seule Déité indivisible, la Trinité du Paradis, qui est réelle bien que n’étant pas une personnalité et qui gouverne la justice et le total. Dans les personnes, l’homme rencontre l’amour du Père ; dans la Trinité, il rencontre l’ordre de l’univers. Le dessein que ce Dieu nourrit envers l’univers, la volonté de Dieu, est le thème du chapitre suivant.",
 "ch02:53": {"title": "Questions pour la réflexion", "items": [
   "1. Quel fondement l’affirmation « la paternité n’est pas réelle sans filiation » (10:3.5) donne-t-elle à ma foi lorsque j’appelle Dieu Père ?",
   "2. Que demande, à ma manière de juger les autres, l’enseignement selon lequel la justice n’est pas une attitude personnelle, mais une fonction de la Trinité (10:6.2) ?",
   "3. Rappelez-vous un moment où votre foi a été ébranlée entre un Père aimant et les lois ordonnées de l’univers. Comment le concept de Trinité (104:2.3) vous aide-t-il à voir cette expérience d’un œil nouveau ?"]},
}
save(U)
