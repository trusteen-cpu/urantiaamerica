# -*- coding: utf-8 -*-
from save import save, saveq

T = {
"ch02.t": "Le Fils Éternel et l’Esprit Infini",
"ch02.sub": "Dieu le Verbe et le Dieu d’Action",
"ch02.sum": "Le Père Universel n’est pas seul. Le Fils Éternel est l’expression parfaite de la première pensée du Père, et l’Esprit Infini est la pensée et la parole conjointes du Père et du Fils manifestées dans l’action. Le Fils est le Verbe de Dieu et la miséricorde de Dieu, et par la gravité d’esprit il attire toute réalité spirituelle vers le Paradis. L’Esprit Infini est le Dieu d’Action et la source du mental ; il porte à chaque créature, sous forme de ministère, l’amour du Père et la miséricorde du Fils. Ce chapitre examine la nature et le ministère de la Source-Centre Deuxième et de la Source-Centre Troisième, et se demande comment ce ministère atteint la prière humaine, le mental humain et la longue ascension.",
"ch02.s1": "Le Fils Éternel, Verbe du Père",
"ch02.s1.u1.k": "Le Fils Éternel est la Source-Centre Deuxième, la révélation personnelle de l’esprit du Père.",
"ch02.s1.u1.p": "Si le Père est volonté infinie, le Fils Éternel est cette volonté exprimée en personne ; c’est pourquoi le Fils est appelé l’Absolu de Personnalité, à côté de l’Absolu Volitif. De même que le Père est d’abord créateur et ensuite contrôleur, le Fils est d’abord cocréateur et ensuite administrateur spirituel. Le Fils Éternel n’est pas un second Dieu rival à côté du Père, mais la révélation personnelle de l’esprit même du Père.",
"ch02.s1.u2.k": "Celui qui a vu le Fils a vu le Père, et le Père vient à nous en tant que personne par les Fils.",
"ch02.s1.u2.p": "Puisque le Fils Éternel est entièrement semblable au Père, connaitre le Fils, c’est connaitre le Père. Cette vérité s’applique non seulement au Fils Éternel, mais aussi aux Fils Créateurs qui viennent dans les univers locaux. L’homme reçoit directement sa personnalité du Père, comme un don, mais le chemin qui monte vers le Père est le chemin vivant que les Fils ont parcouru et montré.",
"ch02.s1.u3.k": "De même que Dieu est amour, le Fils est miséricorde, et la miséricorde est l’amour du Père en action.",
"ch02.s1.u3.p": "La miséricorde du Fils n’est rien d’autre que l’amour du Père. Le Fils ne persuade pas un Père sévère d’accorder sa miséricorde ; c’est plutôt l’amour du Père qui se répand dans le Fils sous forme de soins concrets. Le texte compare cette différence à l’amour d’un père et à l’affection d’une mère : le même amour apparait dans le Père comme un amour de père, et dans le Fils comme quelque chose de plus proche de l’affection d’une mère.",
"ch02.s2": "La gravité d’esprit et le chemin de l’ascension",
"ch02.s2.u1.k": "La gravité d’esprit du Fils Éternel tire littéralement l’âme des hommes vers le Paradis.",
"ch02.s2.u1.p": "De même que la matière est retenue par la gravité de l’Ile du Paradis, les vraies valeurs spirituelles sont retenues par la gravité d’esprit du Fils Éternel. Cette attraction est le secret même de l’ascension au Paradis des âmes humaines qui survivent. L’ascension n’est pas seulement l’escalade solitaire de l’homme ; elle est la réponse à une force d’attraction exercée sans relâche du côté de Dieu.",
"ch02.s2.u2.k": "La prière qui porte une vraie valeur spirituelle parvient immédiatement à la Déité par le circuit de gravité d’esprit.",
"ch02.s2.u2.p": "Le circuit de gravité d’esprit est aussi le chenal de la prière. Pourtant, il ne répond pas à la quantité ni à la forme des mots, mais à la valeur spirituelle de leur contenu. Une pétition spirituelle venant d’un cœur sincère atteint immédiatement toutes les personnalités divines intéressées, tandis que les requêtes purement égoïstes et matérielles ne trouvent aucune place dans ce circuit. La puissance de la prière réside dans son motif.",
"ch02.s2.u3.k": "Le Fils Éternel infini peut être approché par les Fils du Paradis et par le ministère de l’Esprit Infini.",
"ch02.s2.u3.p": "La distance entre l’Infini et l’homme fini ne peut être franchie par les seules forces de l’homme ; aussi les Déités ont-elles construit un pont. Les Fils descendent en effusion, et les enfants de l’Esprit restent tout proches dans un patient ministère. Sans cette effusion et ce ministère, les êtres d’origine matérielle n’auraient guère l’espoir d’atteindre le Fils Éternel.",
"ch02.s3": "L’Esprit Infini, le Dieu d’Action",
"ch02.s3.u1.k": "Avec la personnalisation de l’Esprit Infini, le divin cycle de personnalité est complet et la scène de la création est prête.",
"ch02.s3.u1.p": "Pour que la pensée du Père et la parole du Fils deviennent un univers effectif, il faut l’action. C’est seulement lorsque la Troisième Personne est personnalisée que le cycle de la Déité est complet et que l’espace est préparé comme scène pour le drame de la création. L’Esprit Infini coordonne toute énergie, tout esprit et tout intellect en tant qu’unificateur universel.",
"ch02.s3.u2.k": "Dieu est amour, le Fils est miséricorde, l’Esprit est ministère.",
"ch02.s3.u2.p": "La relation des trois tient dans cette courte phrase. L’amour est la source ; la miséricorde est cet amour tourné vers des êtres imparfaits ; le ministère est la manière dont la miséricorde devient un contact effectif avec la créature. L’Esprit Infini ne représente pas seulement le Père et le Fils ; il exerce aussi son ministère en son propre nom. Toute aide que nous recevons exprime cet amour conjugué.",
"ch02.s3.u3.k": "L’Esprit Infini n’est pas une force impersonnelle, mais une personne divine qui aime et s’attriste.",
"ch02.s3.u3.p": "Parce que l’Esprit pénètre toutes choses, on l’imagine facilement comme une influence ou une énergie impersonnelle. Le texte corrige ce malentendu. L’amour de l’Esprit est réel, et ses chagrins le sont aussi. L’Esprit nous parle et intercède pour nous. Le conseil de ne pas attrister l’Esprit n’a de sens qu’entre des personnes.",
"ch02.s4": "La source du mental",
"ch02.s4.u1.k": "L’Esprit Infini est la source du mental, et sa réalité se dévoile imparfaitement dans le mental humain.",
"ch02.s4.u1.p": "Le Père attire la personnalité, le Fils la réalité spirituelle, et l’Esprit le mental. L’homme trouve la Troisième Personne relativement facile à concevoir, parce que le mental même avec lequel il pense vient de lui. Toutes les pensées vraies et les idées parfaites sont attirées dans le circuit absolu du mental. Un intellect qui aime la vérité répond déjà à l’attraction de l’Esprit.",
"ch02.s4.u2.k": "Bien que la source du mental soit divine, l’intellect immature de l’homme devrait susciter l’humilité.",
"ch02.s4.u2.p": "Que le mental vienne de l’Esprit Infini ne rend pas divine chaque pensée humaine. Le texte dit franchement avec quelle facilité le défaut de sincérité, le manque de droiture, la peur animale et l’anxiété inutile gâchent le mental. Le mental transforme les valeurs de l’esprit en significations, et la volonté fait fructifier ces significations. Prendre soin du mental, c’est préparer le chemin de l’ascension.",
"ch02.qs1": "Quand ai-je fait l’expérience de l’amour de Dieu sous les formes concrètes de la miséricorde et du ministère ?",
"ch02.qs2": "Quelle part de mes prières porte le genre de valeur spirituelle que reçoit le circuit de gravité d’esprit ?",
"ch02.qs3": "Que puis-je faire aujourd’hui pour préserver mon mental, qui vient de l’Esprit Infini, du défaut de sincérité et de l’anxiété ?",
}

E = " … "
Q = {
"ch02.s1.u1.q2#0": "Le Père Universel est d’abord un créateur et ensuite un contrôleur. Le Fils Éternel est d’abord un cocréateur et ensuite un administrateur spirituel. « Dieu est esprit », et le Fils est une révélation personnelle de cet esprit. La Source-Centre Première est l’Absolu Volitif. La Source-Centre Deuxième est l’Absolu de Personnalité.",
"ch02.s2.u2.q2#0": "Le contenu de toute pétition non « dictée par l’esprit » ne peut trouver aucune place dans le circuit spirituel universel. Ces requêtes purement égoïstes et matérielles tombent mortes. Elles ne s’élèvent pas dans le circuit des vraies valeurs d’esprit. De telles paroles sont comme « des cuivres qui résonnent et des cymbales qui retentissent. »",
"ch02.s2.u3.q1#0": "Le Fils Éternel est infini, mais on peut l’approcher par les personnes de ses Fils du Paradis et par le patient ministère de l’Esprit Infini. Sans le service d’effusion des Fils du Paradis et le ministère aimant des créatures de l’Esprit Infini, les êtres d’origine matérielle n’auraient guère l’espoir d’atteindre le Fils Éternel.",
"ch02.s3.u3.q1#0": "« L’amour de l’Esprit » est réel ainsi d’ailleurs que ses chagrins ; donc « n’attristez pas l’Esprit de Dieu ». Lorsque nous observons l’Esprit Infini soit comme une Déité du Paradis, soit comme l’Esprit Créatif d’un univers local, nous constatons que le Créateur Conjoint n’est pas seulement la Source-Centre Troisième, mais aussi une personne divine." + E + "L’Esprit vous dit : « Que celui qui a des oreilles écoute ce que dit l’Esprit. » « L’Esprit lui-même intercède pour vous. »",
"ch02.s4.u2.q2#0": "Le mental transmue les valeurs de l’esprit en significations de l’intellect. La volition a le pouvoir de faire fructifier les significations du mental à la fois dans les domaines matériel et spirituel.",
}
save(T)
saveq(Q)
