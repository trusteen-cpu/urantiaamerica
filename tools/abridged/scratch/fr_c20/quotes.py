import json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
Q = {
 "150.b11.q": "dans le royaume des cieux, il n’y a ni riche ni pauvre, ni homme libre ni esclave, ni homme ni femme, mais tous sont également les fils et les filles de Dieu",
 "151.b5.q": "Ne pensez pas seulement aux foules et à la manière dont elles entendent la vérité ; prêtez attention à la manière dont vous-mêmes vous entendez.",
 "151.b26.q": "Pourquoi êtes-vous si effrayés ? Où est votre foi ? Paix, restez tranquilles.",
 "152.b5.q": "S’il vous faut un roi, que le Père des lumières siège sur un trône dans le cœur de chacun de vous en tant que Souverain spirituel de toutes choses.",
 "153.b5.q": "c’est l’esprit qui vivifie ; la chair, et tout ce qui s’y rapporte, est de peu de profit. Les paroles que je vous ai dites sont esprit et vie.",
 "153.b15.q": "Je suis ce pain de vie. Quiconque vient vers moi n’aura pas faim, et quiconque me croit n’aura jamais soif.",
 "153.b26.q": "vous finirez par être ce que vous choisissez maintenant.",
 "153.b31.q": "Tu nous as enseigné les paroles de la vie éternelle. Nous avons cru en toi et nous t’avons toujours suivi.",
 "154.b5.q": "Car quiconque fait la volonté de mon Père qui est aux cieux, celui-là est ma mère, mon frère et ma sœur.",
 "154.b13.q": "Les situations problématiques, associées aux impulsions à l’action, font naitre les activités mentales, psychiques et spirituelles",
 "154.b23.q": "Ce monde n’a jamais essayé de mettre sérieusement en pratique, sur une grande échelle, les leçons de Jésus",
 "154.b31.q": "Non, béni soit plutôt celui qui entend la parole de Dieu et ose lui obéir.",
 "155.b5.q": "La religion du mental vous attache irrémédiablement au passé. La religion de l’esprit consiste en une révélation progressive",
 "155.b16.q": "la véritable religion d’un homme est la fidélité qu’il ressent dans son cœur envers ses convictions les plus élevées et les plus sincères.",
 "155.b25.q": "La religion de l’esprit signifie effort, lutte, conflit, foi, détermination, amour, loyauté et progrès.",
 "156.b5.q": "Ce monde n’est qu’un pont. On peut le traverser, mais il ne faudrait pas songer à bâtir une demeure dessus.",
 "157.b5.q": "Sur ce roc de réalité spirituelle, je bâtirai le temple vivant de communauté spirituelle dans les réalités éternelles du royaume de mon Père.",
 "158.b5.q": "Celui-ci est mon Fils bienaimé ; écoutez-le.",
 "158.b11.q": "Levez-vous et n’ayez aucune crainte ; vous verrez des choses plus grandes que cela.",
}
json.dump(Q, open('fr/quotes_c20.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(Q))
