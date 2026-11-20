# -*- coding: utf-8 -*-
from lib import save_units, save_quotes, cut

T = {
"ch34.t": "La prière et l’adoration",
"ch34.sub": "Deux manières de communier avec le Père",
"ch34.sum": "La prière et l’adoration sont deux manières dont l’homme communie personnellement avec Dieu. La prière n’est pas une magie qui cherche à adapter Dieu aux désirs de l’homme, mais un processus qui adapte la volonté humaine à la volonté divine, et Dieu répond à la prière en donnant une compréhension élargie de la vérité, de la beauté et de la bonté. La prière de celui qui est entièrement consacré à faire la volonté du Père ne peut rester sans réponse. L’adoration va un pas plus loin : elle ne demande rien et s’offre à Dieu simplement pour ce qu’il est, dans une adoration où l’on s’oublie soi-même. Ce chapitre examine la nature et les conditions de la prière, le caractère de l’adoration et la manière dont la prière grandit jusqu’à devenir adoration. La prière enrichit la vie, tandis que l’adoration illumine la destinée et nous rend de plus en plus semblables à Celui que nous adorons.",
"ch34.s1": "La nature de la prière",
"ch34.s1.u1.k": "La prière est le regard sincère et plein de désir jeté par l’enfant sur son Père spirituel.",
"ch34.s1.u1.p": "Jésus n’enseigna pas la prière comme une formule fixe, mais comme une attitude de l’âme. La prière est l’expression spontanée de l’âme envers l’esprit, la communion entre un fils et son Père. Elle est l’attitude sincère d’un élan vers le ciel pour atteindre ses idéaux, un processus psychologique consistant à échanger la volonté humaine contre la volonté divine. La prière a ainsi sa place dans le plan de Dieu pour remodeler ce qui existe en ce qui devrait exister.",
"ch34.s1.u2.k": "La magie cherche à adapter la Déité aux circonstances ; la prière adapte la personnalité à la volonté de la Déité.",
"ch34.s1.u2.p": "La prière et la magie peuvent se ressembler, mais elles vont dans des directions opposées. La magie cherche à mettre en mouvement une puissance surnaturelle pour obtenir un résultat désiré ; la prière cherche à se mettre soi-même en accord avec la volonté de Dieu. Ainsi, la prière ne change pas Dieu, mais elle change celui qui prie. Chez ceux qui ont prié avec foi et dans une expectative confiante, la paix mentale, l’allégresse, le courage, la maitrise de soi et l’équité ont grandi.",
"ch34.s1.u3.k": "La prière n’est pas une manière d’échapper au conflit, mais un stimulant pour croitre en face du conflit.",
"ch34.s1.u3.p": "La prière ne remplace pas l’action. Une prière qui remet à Dieu le problème que l’on devrait résoudre soi-même peut devenir une forme de paresse. Mais une prière qui demande la sagesse et la force pour éclairer et soutenir son chemin pendant que l’on s’attaque au problème est toujours juste. C’est pourquoi le texte nous conseille de prier pour des valeurs plutôt que pour des choses, pour la croissance plutôt que pour la satisfaction. La prière n’est pas un moyen de contourner la difficulté, mais une manière de grandir en la traversant.",
"ch34.s2": "La prière qui reçoit une réponse",
"ch34.s2.u1.k": "Dieu répond à la prière par une compréhension élargie de la vérité, de la beauté et de la bonté.",
"ch34.s2.u1.p": "La réponse à la prière n’est pas la même chose que recevoir exactement ce que l’on a demandé. De même qu’un parent sage n’accède pas à une demande inconsidérée, mais donne à l’enfant ce dont il a vraiment besoin, de même le Père céleste donne l’esprit et bien d’autres bénédictions à ceux qui les lui demandent. La réponse de Dieu vient sous la forme d’une révélation plus large de la vérité, d’une appréciation plus profonde de la beauté et d’un concept plus élevé de la bonté. C’est pourquoi la prière est le plus puissant stimulant de la croissance spirituelle.",
"ch34.s2.u2.k": "La prière de celui qui est entièrement consacré à faire la volonté du Père ne peut rester sans réponse.",
"ch34.s2.u2.p": "Il n’y a qu’un seul moyen pour que toute prière soit exaucée : que ce que nous demandons soit pleinement conforme à la volonté du Père. Quand ce que le vrai fils désire et ce que le Père Infini veut deviennent une même chose, cela est déjà. Les cinq conditions de la prière efficace que Jésus enseigna — désintéressement, foi, sincérité, intelligence et confiance en la volonté infiniment sage du Père — tendent toutes vers cette harmonie.",
"ch34.s2.u3.k": "Soyez équitables dans la prière ; ne vous attendez pas à ce que Dieu vous aime plus que ses autres enfants.",
"ch34.s2.u3.p": "La prière exige l’équité. Une prière qui demande à Dieu du favoritisme, qu’il m’aime plus que mes amis, mes voisins ou mes ennemis, n’est pas éthique. La prière devient plus éthique quand elle recherche le pardon et la sagesse pour la maitrise de soi. De plus, héberger délibérément l’iniquité dans son cœur coupe progressivement la communion personnelle avec Dieu.",
"ch34.s2.u4.k": "La prière commence par la demande matérielle et grandit jusqu’à devenir prière pour ses compagnons.",
"ch34.s2.u4.p": "Les prières de l’enfance, qu’il s’agisse d’un individu ou d’une race, sont égoïstes et matérielles. Même de telles prières ont de la valeur dans la mesure où elles suscitent l’effort ; aussi les personnes mûres doivent-elles prendre garde à ne pas décourager les prières de ceux qui manquent de maturité. Pourtant, la prière doit grandir. La prière de Jésus était un remède contre l’introspection nuisible, et il priait en général au pluriel, pour ses compagnons plutôt que pour lui-même.",
"ch34.s3": "Le caractère de l’adoration",
"ch34.s3.u1.k": "L’adoration se suffit à elle-même ; elle ne demande rien et n’espère rien.",
"ch34.s3.u1.p": "La grande différence entre la prière et l’adoration tient à la présence ou à l’absence d’intérêt personnel. La prière contient un élément de demande, mais la vraie adoration n’en contient aucun. La vraie adoration ne demande rien pour l’adorateur et n’espère rien en retour. L’adoration est la réponse spontanée du cœur devant Celui qu’il aime.",
"ch34.s3.u2.k": "La prière est une pensée qui rappelle le moi ; l’adoration est une pensée qui oublie le moi.",
"ch34.s3.u2.p": "Dans la prière, la personne est encore consciente d’elle-même et de ses besoins ; dans l’adoration, elle s’oublie elle-même. L’adoration est donc une attention sans effort, une forme reposante d’exercice spirituel. Dans l’adoration, la fraction s’identifie avec le Tout, le fini avec l’Infini, le fils avec le Père, le temps avec l’éternité. L’adoration est la communion personnelle du fils avec le Père ; elle repose l’âme et la rend créative.",
"ch34.s3.u3.k": "L’expérience de l’adoration est la tentative de l’Ajusteur pour communiquer au Père les désirs indicibles de l’âme.",
"ch34.s3.u3.p": "L’adoration n’est pas une chose que la personne accomplit seule. L’Ajusteur intérieur cherche à communiquer au Père les désirs inexprimables de l’âme, et cette âme est la création conjointe du mental humain et de l’Ajusteur. C’est pourquoi un mental sujet aux limitations matérielles ne peut être pleinement conscient du sens profond de l’adoration. La mesure dans laquelle on réalise la réalité de l’expérience de l’adoration ne dépend pas du niveau intellectuel, mais de la croissance de l’âme immortelle en évolution.",
"ch34.s4": "De la prière à l’adoration",
"ch34.s4.u1.k": "La prière peut enrichir la vie, mais l’adoration illumine la destinée.",
"ch34.s4.u1.p": "Le texte fait remarquer que les religions modernes ont trop mis l’accent sur la prière et négligé la communion d’adoration, qui est plus essentielle. Il ne s’agit pas d’abandonner la prière ; elle est un escalier qui mène à l’adoration. La prière éleva l’âme de Jésus à une profonde communion avec les Dirigeants Suprêmes de l’univers, et elle élèvera les mortels à la communion de la véritable adoration. La quantité de bénédictions célestes qu’une personne reçoit dépend de la capacité de réception spirituelle de son âme.",
"ch34.s4.u2.k": "L’adoration nous rend de plus en plus semblables à Celui que nous adorons ; elle se tourne vers l’Un pour servir la multitude.",
"ch34.s4.u2.p": "L’esprit intérieur parle le mieux quand le mental humain est dans une attitude de sincère adoration. L’adoration est une expérience transformatrice qui nous rend de plus en plus semblables à Celui que nous adorons, le chemin par lequel le fini s’approche graduellement de la présence de l’Infini. Pourtant, l’adoration n’est pas une fuite hors du monde. Nous nous tournons vers l’Un afin de recevoir l’inspiration pour servir la multitude.",
"ch34.qs1": "Ma prière est-elle plus proche d’un effort pour adapter Dieu à ma volonté, ou pour adapter ma volonté à celle de Dieu ?",
"ch34.qs2": "Ai-je fait l’expérience d’une adoration qui ne demande rien et s’offre à Dieu simplement pour ce qu’il est ?",
"ch34.qs3": "Comment puis-je faire place, dans ma vie quotidienne, à un temps d’attente silencieuse après la prière ?",
}

Q = {
"ch34.s2.u3.q1#0": cut("91:4.3", "Dans toutes vos prières", "même vos ennemis.") + " … " + cut("91:4.3", "La prière est un peu plus éthique", "maitrise de soi."),
"ch34.s3.u1.q1#0": cut("5:3.3", "L’adoration se suffit", "et la prière.") + " … " + cut("5:3.3", "L’adoration ne demande rien", "pour l’adorateur."),
}

save_units(T)
save_quotes(Q)
