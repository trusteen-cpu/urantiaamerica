# -*- coding: utf-8 -*-
from save import save, saveq

T = {
"ch03.t": "La Trinité du Paradis",
"ch03.sub": "L’union éternelle de la Déité indivise",
"ch03.sum": "La Déité est une, et pourtant il y a trois personnalisations positives et divines de la Déité. La Trinité du Paradis jaillit de la nature aimante du Père Universel, qui se partage lui-même, et elle existe en tant qu’union éternelle de Déité du Père, du Fils et de l’Esprit. La Trinité n’est pas simplement la somme de trois personnes, mais la Déité indivise, et elle accomplit des fonctions collectives, telles que la justice, le jugement et l’administration de la totalité, qui n’appartiennent à aucune personne isolée. Ce chapitre se demande pourquoi la Trinité est inévitable, ce que signifie l’union des trois personnes, comment la justice et la miséricorde vont de pair, et comment l’humanité a reçu cette vérité.",
"ch03.s1": "Le Dieu qui se partage",
"ch03.s1.u1.k": "La personnalité divine n’est pas centrée sur elle-même ; depuis l’éternité, le Père s’est distribué lui-même.",
"ch03.s1.u1.p": "Le point de départ pour comprendre la Trinité n’est pas l’arithmétique, mais le caractère. Le Père Universel ne garde que ce qui ne peut être délégué et donne tout le reste, car l’amour ne demeure pas seul. De même que les créatures cherchent à s’associer avec d’autres personnes, l’Infini partage la réalité d’être et l’égalité du moi avec deux personnes coordonnées. La Trinité est la forme qu’a prise dans l’éternité l’amour qui se donne.",
"ch03.s1.u2.k": "Le Fils est indispensable à la paternité de Dieu, l’Esprit à la fraternité du Fils et de l’Esprit.",
"ch03.s1.u2.p": "Pour être père, il faut un fils, et pour être frère, il faut un autre compagnon. La relation divine tient ainsi ensemble la paternité et la fraternité. Le texte remarque que trois personnes forment un groupe social minimum, mais ajoute que c’est la moindre des raisons. Le pluriel de « Faisons l’homme à notre image » désigne cette relation au sein de l’unique Déité.",
"ch03.s1.u3.k": "Les Fils sont le Verbe de Dieu ; les enfants de l’Esprit sont les Actes de Dieu.",
"ch03.s1.u3.p": "Les trois personnes sont égales en nature et coordonnées en existence, mais leur œuvre universelle est nettement distincte. Dieu parle par le Fils et, avec le Fils, agit par l’Esprit. Le Fils et l’Esprit travaillent comme deux frères qui partagent un même Père honoré. Que la vie intérieure de la Déité ne soit pas rivalité, mais admiration et amour, voilà un modèle pour toute relation entre créatures.",
"ch03.s2": "Trois personnes, une seule Déité",
"ch03.s2.u1.k": "La Déité éternelle est parfaitement unifiée, et pourtant elle existe en trois personnes parfaitement individualisées.",
"ch03.s2.u1.p": "La Trinité rend possibles à la fois la diversité et l’unité. Les trois personnes ont chacune leur propre caractère et leurs propres pouvoirs et peuvent collaborer comme elles le veulent, mais une telle collaboration n’est pas la Trinité. La Trinité est réelle en tant qu’union de Déité des trois, et le Père, le Fils ou l’Esprit peuvent chacun entretenir une relation avec elle. L’union n’efface pas la personnalité.",
"ch03.s2.u2.k": "La Trinité n’est pas une unanimité fonctionnelle, mais une Déité indivise et indivisible.",
"ch03.s2.u2.p": "Trois personnes travaillant dans un même esprit, ce n’est pas la même chose que trois personnes étant une seule Déité. Le texte appelle l’union fonctionnelle des trois personnes une triunité et dit que la Trinité est autre chose : la Déité indivise. Cette distinction protège à la fois contre deux malentendus : la Trinité comme un comité de trois Dieux, et la Trinité comme trois masques d’un seul Dieu.",
"ch03.s2.u3.k": "Les mortels envisagent la Trinité selon leurs propres lumières et en découvrent davantage au cours de leur ascension.",
"ch03.s2.u3.p": "La Trinité n’est pas une question d’examen à maitriser dès maintenant. Le texte conseille aux mortels dans la chair de l’envisager selon leurs propres lumières et les réactions de leur mental et de leur âme. Nous savons peu de choses maintenant, mais sur le chemin du Paradis viendront des découvertes répétées et étonnantes. L’humilité devant le mystère et l’attente de la découverte vont de pair.",
"ch03.s3": "La justice, fonction de la Trinité",
"ch03.s3.u1.k": "La justice n’est jamais l’attitude d’une seule personne ; elle est toujours une fonction plurale.",
"ch03.s3.u1.p": "Le Père, le Fils et l’Esprit sont des personnes d’amour, de miséricorde et de ministère, et aucun d’eux n’administre seul la justice. La justice n’apparait que comme une fonction collective, lorsque les trois s’unissent en tant que Trinité. L’enseignement de Jésus selon lequel la justice est une fonction de groupe, et jamais un acte personnel, repose sur le même principe. C’est pourquoi les communautés humaines instituent un jugement public à la place de la vengeance privée.",
"ch03.s3.u2.k": "La justice est l’idée collective de la droiture ; la miséricorde en est l’expression personnelle.",
"ch03.s3.u2.p": "On a facilement l’impression que la justice et la miséricorde s’opposent. Le texte dit que, pleinement comprises, la juste équité de la Trinité et l’amour miséricordieux du Père coïncident. Parce que l’homme n’a pas cette compréhension, les trois personnes s’ajustent, dans les univers du temps, pour coordonner le ministère de l’amour et de la loi. La justice ne s’oppose pas à l’amour ; elle garde l’ordre de l’amour.",
"ch03.s3.u3.k": "Même les vicissitudes inexplicables de la vie peuvent être tissées en un motif significatif sous le supercontrôle de la Trinité.",
"ch03.s3.u3.p": "Devant les désastres, les maladies et les accidents, les gens s’interrogent sur la volonté de Dieu. Au lieu d’une réponse ferme, le texte offre une possibilité : les vicissitudes inexplicables de la vie peuvent être tissées en un motif significatif de haute valeur par la fonction du Suprême et le supercontrôle de la Trinité. Nous pouvons discerner l’amour personnel dans les actes du Père, mais la pleine signification des actes de la Trinité ne se révèle que dans l’éternité.",
"ch03.s4": "La vérité de la Trinité et l’humanité",
"ch03.s4.u1.k": "Jésus enseigna la vérité de la Trinité, mais ses apôtres n’y entendirent qu’une figure de style.",
"ch03.s4.u1.p": "L’humanité est familière depuis longtemps avec le nombre trois ; les idées de triades sont nées d’expériences naturelles comme les phalanges des doigts ou les pieds d’un siège. Pourtant, la Trinité révélée est différente de ces croyances aux triades. Lorsque Jésus enseigna cette vérité, ses apôtres, attachés au monothéisme hébreu, ne la reçurent que comme un symbole. La vérité ne se transmet que dans la mesure du mental qui la reçoit.",
"ch03.s4.u2.k": "Par le concept de la Trinité, l’homme peut saisir comment l’amour et la loi vont de pair dans l’univers.",
"ch03.s4.u2.p": "La foi donne la clairvoyance sur l’amour de Dieu, mais cette foi ne modifie pas les lois de l’univers matériel, et la rencontre de ce fait peut être déroutante. Le texte offre le concept de la Trinité comme clé. Grâce à lui, l’homme peut commencer à saisir les relations réciproques entre l’amour et la loi dans les créations de l’espace-temps. L’amour et la loi sont deux faces de la même Déité.",
"ch03.qs1": "Qu’est-ce que le caractère de Dieu, qui se partage lui-même, demande à mes relations et à ma manière de donner ?",
"ch03.qs2": "Si la justice est une fonction de groupe plutôt qu’une attitude personnelle, comment pourrais-je traiter autrement le ressentiment et la colère ?",
"ch03.qs3": "De quoi ai-je besoin pour continuer à faire confiance tout en reconnaissant que je ne comprends pas encore certaines souffrances ?",
}

E = " … "
Q = {
"ch03.s3.u2.q1#0": "La justice est l’idée collective de la droiture ; la miséricorde en est l’expression personnelle." + E + "Quand l’équité de la Trinité et l’amour miséricordieux du Père Universel sont complètement perçus et pleinement compris, ils coïncident. Toutefois, les hommes n’ont pas cette pleine compréhension de la justice divine. C’est ainsi que, dans la Trinité telle que les hommes la conçoivent, les personnalités du Père, du Fils et de l’Esprit s’ajustent pour coordonner le ministère d’amour et la loi dans les univers expérientiels du temps.",
"ch03.s4.u2.q1#0": "En reconnaissant le concept de la Trinité, le mental humain peut espérer saisir un aperçu des relations réciproques entre l’amour et la loi dans les créations de l’espace-temps. Par la foi spirituelle, l’homme acquiert la clairvoyance sur l’amour de Dieu, mais il ne tarde pas à découvrir que cette foi spirituelle n’a pas d’influence sur les lois ordonnées de l’univers matériel.",
}
save(T)
saveq(Q)
