# -*- coding: utf-8 -*-
from lib import save_units, save_quotes, cut

T = {
"ch33.t": "L’expérience religieuse",
"ch33.sub": "L’expérience vivante de connaitre Dieu",
"ch33.sum": "La religion, telle que la présente le Livre d’Urantia, n’est ni un système de doctrines ni une extase mystique. C’est l’expérience vivante d’une personne qui connait Dieu comme Père et l’homme comme frère. L’esprit divin rejoint l’homme moins dans les sentiments que dans sa pensée la plus élevée, et cette rencontre devient clairvoyance spirituelle. L’expérience religieuse ne peut être ni conférée ni empruntée ; elle grandit proportionnellement à la recherche des valeurs finales, et sa force motrice est une foi vivante qui gouverne la manière de vivre. Ce chapitre examine tour à tour la nature de l’expérience religieuse, sa croissance, le caractère de la foi et les fruits que porte l’expérience dans le service et dans la paix. La réalité de la religion se montre davantage dans la manière de vivre que dans l’explication, et celui qui a trouvé Dieu vit comme s’il était déjà en présence de l’Éternel.",
"ch33.s1": "La nature de l’expérience religieuse",
"ch33.s1.u1.k": "La vraie religion consiste à connaitre Dieu comme Père et l’homme comme frère.",
"ch33.s1.u1.p": "La définition de la religion est simple : l’expérience personnelle de connaitre Dieu comme Père, et la réalisation qui en découle naturellement, connaitre l’homme comme frère. La première est entièrement intérieure, mais la seconde exige un ajustement social du « moi » à d’autres « moi ». La religion commence donc à l’intérieur et se dirige vers l’extérieur. Une croyance qui s’appuie sur des menaces de punition ou des promesses de récompenses mystiques est loin de cette définition.",
"ch33.s1.u2.k": "La religion n’est pas le produit de la raison, mais, vue de l’intérieur, elle est entièrement raisonnable.",
"ch33.s1.u2.p": "La religion rejette deux malentendus opposés. L’un la voit comme un système philosophique à déduire par raisonnement et à démontrer par des preuves ; l’autre la voit comme une extase indescriptible dont seuls quelques mystiques peuvent bénéficier. La religion n’est pas le produit de la raison, mais, vue de l’intérieur, elle est entièrement raisonnable ; elle n’est pas un assentiment intellectuel à une doctrine, mais une pénétration dans la réalité.",
"ch33.s1.u3.k": "Ce sont nos pensées, et non nos sentiments, qui nous conduisent vers Dieu.",
"ch33.s1.u3.p": "Contrairement à l’opinion courante selon laquelle la religion appartient au domaine de l’émotion, le texte dit que l’esprit divin établit le contact avec l’homme dans sa pensée la plus élevée et la plus spiritualisée. Cela ne rabaisse pas les sentiments. Cela signifie que l’œil qui discerne Dieu est l’œil du mental, et que ce mental doit être pur.",
"ch33.s2": "La croissance de l’expérience religieuse",
"ch33.s2.u1.k": "La religion ne peut être ni conférée ni empruntée ; elle grandit à mesure que grandit la recherche des valeurs finales.",
"ch33.s2.u1.p": "La religion n’est pas un bien que l’on peut hériter ou transmettre par l’instruction. Comme toute croissance du corps, du mental et de l’esprit, la croissance religieuse se fait inconsciemment, et personne ne peut la forcer. Mais on peut lui fournir des conditions favorables. L’unique contribution de l’homme à la croissance est la mobilisation de tous les pouvoirs de sa personnalité, c’est-à-dire la foi vivante.",
"ch33.s2.u2.k": "La croissance spirituelle va de l’éveil aux besoins au discernement des significations, puis à la découverte des valeurs.",
"ch33.s2.u2.p": "La croissance spirituelle suit un ordre. On s’éveille d’abord à ce qui manque, puis on discerne les significations des choses, et enfin on découvre ce qui a vraiment de la valeur. La preuve d’une telle croissance n’est pas la quantité de connaissances théologiques, mais des mobiles nés de l’amour, un service désintéressé et l’adoration sincère des idéaux de la divinité. La spiritualité devient ainsi la mesure à la fois de notre proximité de Dieu et de notre utilité pour les autres.",
"ch33.s2.u3.k": "L’émotion seule est une fausse conversion, et les états mystiques ne doivent pas être confondus avec la communion spirituelle.",
"ch33.s2.u3.p": "On prend facilement les expériences de conversion spectaculaires et les extases mystiques pour le sommet de la religion. Le texte fait calmement remarquer que les facteurs mêmes qui provoquent de tels états en révèlent le danger. Les états produits par la fatigue, le jeûne, la peur et les émotions violentes peuvent être dangereux. Le sentiment doit être accompagné de la foi. La communion de Jésus avec son Ajusteur était tout autre chose que ces états mystiques.",
"ch33.s3": "La foi vivante",
"ch33.s3.u1.k": "La croyance attache, la foi affranchit.",
"ch33.s3.u1.p": "Accepter un enseignement comme vrai n’est encore qu’une croyance. Celle-ci devient foi quand elle met la vie en mouvement et gouverne effectivement la manière de vivre. Les croyances peuvent être partagées par un groupe, mais la foi ne grandit que dans le cœur de l’individu. Et la foi honore la vérité, la beauté et la bonté sans les adorer ; elle se tourne vers Dieu seul, qui les personnifie toutes.",
"ch33.s3.u2.k": "La foi spirituelle authentique se démontre par la manière dont elle réagit dans l’épreuve et l’adversité.",
"ch33.s3.u2.p": "La réalité de la foi se montre moins dans les jours calmes que dans les jours difficiles. Le texte énumère les réactions d’une âme qui possède la foi : elle fait progresser la morale malgré les tendances animales, se fie à la bonté de Dieu dans les déceptions amères, trouve du courage face aux calamités et garde son équilibre dans la maladie et la souffrance. Ces réactions, qui surgissent là où la vie ressemble à une défaite, révèlent la divinité potentielle de l’âme émergente.",
"ch33.s3.u3.k": "Les religionistes vivent comme s’ils étaient déjà en présence de l’Éternel.",
"ch33.s3.u3.p": "Les facteurs de l’expérience religieuse sont difficiles à analyser, mais ses résultats ne sont pas difficiles à observer. Les croyants vivent aujourd’hui comme si l’immortalité était déjà à portée de leur main. La religion n’écarte pas les ennuis humains, mais elle les dissout, les illumine et les transcende. Et la foi jette un pont sur l’abime entre la logique de l’intellect, qui connait la Cause Première comme étant Cela, et l’affirmation de l’âme selon laquelle la Cause Première est Lui, le Père céleste.",
"ch33.s4": "Les fruits de l’expérience religieuse",
"ch33.s4.u1.k": "La religion n’est pas une technique pour obtenir la paix mentale, mais une impulsion qui organise l’âme pour le service.",
"ch33.s4.u1.p": "Traiter la religion uniquement comme un refuge privé, c’est passer à côté de son essence. La vraie religion enrôle tout le « moi » dans le service loyal qui consiste à aimer Dieu et à servir les hommes. Elle n’enlève rien à la vie, mais ajoute de nouvelles significations à toutes choses et engendre un enthousiasme et un courage nouveaux. Pourtant, si ce zèle n’est pas gouverné par la clairvoyance spirituelle et par la fidélité aux obligations sociales ordinaires, il peut se transformer en un dangereux esprit de croisade.",
"ch33.s4.u2.k": "Celui qui trouve Dieu est poussé à un service affectueux pour réconforter ses compagnons.",
"ch33.s4.u2.p": "Le désir religieux est une faim de réalité divine, et l’expérience religieuse est la conscience d’avoir trouvé Dieu. Celui qui a trouvé Dieu ne cherche pas à s’en vanter. Il cherche simplement un contact affectueux avec les autres, afin que la bonté qui surgit dans son âme déborde pour les réconforter. Cet intérêt altruiste pour autrui nait parce que le même fragment de Dieu habite chaque personne. L’uniformité philosophique est hors d’atteinte, mais l’unité spirituelle est possible.",
"ch33.s4.u3.k": "Un signe remarquable de la vie religieuse est une paix dynamique qui dépasse toute compréhension.",
"ch33.s4.u3.p": "La paix que donne la religion n’est pas un calme immobile. C’est un équilibre cosmique maintenu au milieu du service et de l’aventure, une stabilité qui s’installe là où le doute et l’agitation ont disparu. Cette paix est immunisée contre les déceptions. Celui qui a saisi la réalité du Suprême et poursuit le but de l’Ultime jouit à la fois de la gloire du triomphe et d’un profond sentiment de sécurité.",
"ch33.qs1": "Ma foi reste-t-elle une croyance qui m’a été transmise, ou est-elle une foi qui change effectivement ma manière de vivre ?",
"ch33.qs2": "Quand je subis une déception ou une injustice, comment ma foi se manifeste-t-elle dans ma réaction ?",
"ch33.qs3": "Si l’expérience de connaitre Dieu m’a déjà conduit à servir les autres, à quoi cela ressemblait-il ?",
}

Q = {
"ch33.s1.u1.q1#0": cut("99:5.1", "La religion est exclusivement", "ajustement à un groupe."),
"ch33.s1.u2.q1#0": cut("101:1.1", "La vraie religion n’est pas", "entièrement raisonnable."),
"ch33.s1.u3.q1#0": cut("101:1.3", "L’esprit divin établit", "est le mental pur."),
"ch33.s3.u1.q1#0": cut("101:8.1", "La croyance a atteint", "une simple croyance.") + " … " + cut("101:8.1", "On croit la vérité", "infiniment plus encore."),
"ch33.s3.u3.q1#0": cut("102:2.3", "Il est difficile d’identifier", "à portée de leur main."),
"ch33.s4.u1.q1#0": cut("100:3.1", "La religion n’est pas une technique", "servir les hommes."),
"ch33.s4.u2.q2#0": cut("103:1.1", "L’unité de l’expérience religieuse", "des autres hommes.") + " … " + cut("103:1.1", "Les membres d’un groupe", "uniformité philosophique."),
}

save_units(T)
save_quotes(Q)
