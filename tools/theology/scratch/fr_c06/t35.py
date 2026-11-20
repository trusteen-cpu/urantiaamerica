# -*- coding: utf-8 -*-
from lib import save_units, save_quotes, cut

T = {
"ch35.t": "Les Fils ascendants",
"ch35.sub": "De l’origine animale au Paradis",
"ch35.sum": "Si les Fils descendants viennent d’en haut pour servir, les fils ascendants partent d’en bas et s’élèvent vers Dieu. Leur plus grande armée est formée des mortels d’origine animale, mais les gardiens séraphiques, les Fils Matériels et les médians suivent aussi ce chemin. Les mortels sont le dernier anneau de la chaine des êtres appelés fils de Dieu ; ils sont dès maintenant fils par la foi, et ils deviennent fils ascendants au moment de la fusion avec un esprit. Ce chapitre examine les classes de fils ascendants, la filiation des mortels, les sept stades qui mènent de la planète au Paradis et les destinées qui diffèrent selon le type de fusion, en affirmant que toutes ces destinées reposent sous le même amour du Père. Même le plus faible désir de trouver Dieu suffit pour que toute âme se mette en route sur ce chemin.",
"ch35.s1": "Les Fils Ascendants de Dieu",
"ch35.s1.u1.k": "L’histoire des fils ascendants est le récit de l’amour divin et d’une gracieuse condescendance.",
"ch35.s1.u1.p": "Le Livre d’Urantia répartit les êtres, dans les grandes lignes, en fils descendants et en fils ascendants. Les fils ascendants sont révélés en sept classes : les mortels fusionnés avec le Père, avec le Fils et avec l’Esprit, les séraphins évolutionnaires, les Fils Matériels ascendants, les médians transférés et les Ajusteurs Personnalisés. Cette liste n’est pas un simple tableau de catégories. Le fait même que des êtres de la plus humble origine animale puissent s’élever témoigne de l’amour que les Déités répandent sans compter sur tous les univers du temps et de l’espace.",
"ch35.s1.u2.k": "Non seulement les mortels, mais aussi les anges et les médians partagent la chance de l’ascension vers le Paradis.",
"ch35.s1.u2.p": "Le chemin de l’ascension n’est pas ouvert aux seuls humains. Les gardiens séraphiques parviennent à la filiation ascendante par leur expérience et leur service auprès des mortels ascendants, et beaucoup d’entre eux sont enrôlés dans le Corps des Mortels de la Finalité. Les médians aussi, bien que leur ascension vers le Paradis soit longtemps différée, sont libérés de leurs devoirs planétaires dès que leur monde atteint l’ère de lumière et de vie. L’ascension est une route que parcourent ensemble des êtres très différents, et le service est la clé qui l’ouvre.",
"ch35.s2": "La filiation des mortels",
"ch35.s2.u1.k": "Les mortels sont le dernier anneau de la chaine des fils, et le Père s’approche le plus près par l’Ajusteur intérieur.",
"ch35.s2.u1.p": "L’empreinte personnelle du Fils Éternel se transmet à travers une série de fils de moins en moins divins et de plus en plus humains, jusqu’à un être que l’homme peut voir et toucher. Au bout de cette chaine se trouvent les mortels. Dieu le Père n’apparait pas sous une forme personnelle directe à ses innombrables créatures, mais cela ne le rend pas lointain. Celui qui est le plus éloigné de nous en personnalité s’approche le plus près de nous dans l’Ajusteur de Pensée intérieur, en communion avec l’âme même.",
"ch35.s2.u2.k": "Les mortels n’appartiennent pas encore à l’ordre divin, mais ils sont dès maintenant fils de Dieu par la foi.",
"ch35.s2.u2.p": "Les mortels ne sont pas encore divins par nature ; ils ne deviennent fils ascendants qu’au moment de la fusion avec un esprit éternel. Pourtant, même avant cela, l’homme est déjà un fils. Le Père lui a donné la personnalité, ainsi qu’une mesure de la divine spontanéité du libre arbitre que Dieu partage avec ses fils, et un fragment du Père lui-même l’habite. L’homme est donc dès maintenant directement relié au divin Père de tous les Fils de Dieu.",
"ch35.s2.u3.k": "Toute âme qui a ne serait-ce que le plus faible désir de trouver Dieu survivra.",
"ch35.s2.u3.p": "Le secret de la survie réside dans l’identification à l’esprit. Pourtant, le texte place le seuil de la survie remarquablement bas. Il suffit d’une bonne volonté à coopérer avec l’Ajusteur et d’un désir de trouver Dieu et d’atteindre la perfection, même si ce désir n’est que la première et la plus faible lueur d’une compréhension primitive de la vraie lumière. La survie n’est pas une récompense pour le savoir ou les accomplissements ; elle dépend de l’orientation de la volonté vers Dieu.",
"ch35.s3": "Les sept stades de la carrière ascendante",
"ch35.s3.u1.k": "Les pèlerins ascendants traversent sept stades, depuis les mortels planétaires jusqu’aux arrivants au Paradis.",
"ch35.s3.u1.p": "La carrière universelle d’un mortel est organisée en stades bien définis. On nait et l’on vit sur une planète, on se repose après la mort comme survivant endormi, on s’éveille et l’on étudie sur les mondes des maisons, on s’élève comme progresseur morontiel, on devient pupille du superunivers, on traverse Havona comme pèlerin et l’on arrive au Paradis. Le point de départ est le même pour tous : les mortels de tous les mondes sont des êtres évolutionnaires d’origine animale, et, après la mort, ils fraternisent comme une seule famille morontielle sur les mondes des maisons.",
"ch35.s3.u2.k": "Dans le passage du morontiel à l’esprit, le mental, la personnalité et le caractère restent inchangés.",
"ch35.s3.u2.p": "Chaque stade de l’ascension est une continuation et non une rupture. Les progresseurs morontiels qui s’élèvent des mondes des maisons jusqu’au siège de l’univers local apprennent en servant dans d’innombrables affectations auprès de leurs éducateurs et de leurs frères ainés. Vers le moment où ils quittent l’univers local, ils acquièrent une véritable identité spirituelle, mais ce n’est qu’une légère transition. La forme change, mais le mental, la personnalité et le caractère se maintiennent sans changement. L’ascendeur reste la même personne jusqu’au bout.",
"ch35.s3.u3.k": "Résider au Paradis signifie que l’on a trouvé Dieu.",
"ch35.s3.u3.p": "Celui qui était sur terre une créature de chair et de sang devient un être morontiel dans l’univers local, un esprit évoluant dans le superunivers, et reçoit véritablement et sérieusement son éducation spirituelle à Havona. Il se tient enfin au Paradis en tant qu’esprit rendu parfait. Y résider signifie que l’on a trouvé Dieu, et ceux qui ont fusionné avec le Père sont enrôlés dans le Corps des Mortels de la Finalité. Pourtant, cette arrivée n’est pas une fin, mais le commencement d’un nouvel apprentissage en divinité et en absonité.",
"ch35.s4": "Fusion et destinée",
"ch35.s4.u1.k": "Parce que le Père s’est effusé lui-même, il exige de l’homme une perfection ultime.",
"ch35.s4.u1.p": "Le commandement d’être parfait découle du don du Père. Parce que le Père a placé son propre esprit dans l’homme, il peut demander la perfection qui consiste à devenir un avec cet esprit. Les mortels fusionnés avec l’Ajusteur sont la seule classe d’êtres humains dont la totalité traverse les circuits de Havona et trouve Dieu au Paradis, et devant eux la carrière de service universel est grande ouverte. Le texte déclare que cette dignité de la destinée et cette gloire de l’aboutissement attendent chacun.",
"ch35.s4.u2.k": "Les destinées mortelles diffèrent, mais aucune n’est plus grande ou moindre qu’une autre.",
"ch35.s4.u2.p": "La destinée diffère selon le type de fusion. Les mortels fusionnés avec l’Esprit restent en général dans l’univers local, les survivants fusionnés avec le Fils dans le superunivers, tandis que les mortels fusionnés avec l’Ajusteur vont jusqu’à pénétrer l’univers des univers, parce que l’esprit fusionné retourne à son niveau d’origine. Mais le texte dit clairement de ne pas lire ces différences comme un classement. Les destinées sont simplement différentes, et il n’y a ni favoritisme ni arbitraire dans le fonctionnement du plan de survie.",
"ch35.s4.u3.k": "La filiation est la relation suprême entre la créature et le Créateur.",
"ch35.s4.u3.p": "L’histoire des fils ascendants revient finalement à l’amour du Père. Le Père aime chaque fils individuellement, personnellement et de manière irremplaçable, et cet amour éclipse tous les autres faits, y compris les différences de destinée. Ainsi, l’homme peut reconnaitre sa place dans la famille de filiation divine et commencer à sentir l’obligation de se prévaloir de toute l’aide que le plan de survie offre si libéralement, un plan illuminé par la vie d’un Fils d’effusion.",
"ch35.qs1": "En quoi le fait que mon point de départ soit humble change-t-il ma compréhension de l’amour de Dieu ?",
"ch35.qs2": "En quoi l’enseignement selon lequel même un faible désir de trouver Dieu suffit pour survivre change-t-il ma manière de voir les autres ?",
"ch35.qs3": "Si ma personnalité et mon caractère se maintiennent après la mort, quel caractère suis-je en train de cultiver maintenant ?",
}

Q = {
"ch35.s1.u2.q2#0": cut("40:3.1", "Peu après qu’une planète", "longtemps différée."),
"ch35.s2.u3.q1#0": cut("40:5.4", "L’identification à l’esprit", "ces dons divins."),
"ch35.s3.u3.q1#0": cut("30:4.26", "Sur terre, vous étiez", "esprit rendu parfait."),
"ch35.s4.u1.q1#0": cut("40:7.4", "Nous parlons ici", "perfection ultime."),
"ch35.s4.u3.q1#0": cut("40:10.13", "Le Père aime chacun", "et le Créateur."),
}

save_units(T)
save_quotes(Q)
