import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
Q = {
 "w06.081": "Et il semblerait aussi que l’inconditionné soit aussi illimité, du moins d’un point de vue qualitatif, bien que nous n’en soyons pas aussi surs en ce qui concerne les relations quantitatives.",
 "w06.108": "La déformation de la vérité sera probablement réduite au minimum si le troisième membre de la Trinité des Trinités est conçu comme l’Absolu Universel …",
 "w06.135": "… Ces deux types de personnalité sont donc destinés à la superpersonnalité éternelle future du ministère transcendantal dans les royaumes absonites de l’Ultime et du Suprême-Ultime, allant même jusqu’aux niveaux de l’Ultime-Absolu.",
 "w06.150": "L’improbabilité d’atteindre une destinée infinie n’empêche nullement de se former des idées sur cette destinée …",
 "w06.154": "L’infinité est remplie par l’Infini ; l’Infini englobe l’infinité. C’est le moment statique hypothétique de l’éternité …",
 "w06.163": "Nous ne comprenons pas comment la valeur d’une chose infinie et divine pourrait être accrue, mais nous découvrons que les significations peuvent être modifiées, sinon accrues, même dans les relations de la Déité infinie.",
 "w07.017": "Avec l’Esprit, le cycle existentiel de personnalisation de la Déité est accompli. Les personnalités primaires issues de la Source-Centre Troisième sont expérientielles, et au nombre de sept.",
 "w07.036": "Avec l’apparition de la Déité personnelle coexistante, le Fils Éternel et l’Esprit Infini, le Père échappa, en tant que personnalité, à sa diffusion dans l’ensemble du potentiel de la Déité Totale, ce qui autrement aurait été inévitable.",
 "w07.050": "C’est le moment statique hypothétique de l’éternité ; les actuels sont encore inclus dans leurs potentiels, et les potentiels ne sont pas encore apparus dans l’infinité du JE SUIS. Toutefois, même dans cette situation hypothétique, il nous faut admettre que la possibilité de volonté autonome existe.",
 "w07.062": "Nous décrivons les origines de la réalité et les différenciations de l’infinité par un exposé séquentiel, mais en fait les sept Absolus sont tous éternels d’une manière non qualifiée et coordonnée.",
 "w07.074": "Le Paradis ne représente rien et rien ne représente le Paradis. Il n’est ni une force ni une présence ; il est simplement le Paradis.",
 "w07.077": "Le Paradis est le centre géographique de l’infinité. Il n’est pas une partie de la création universelle, ni même une véritable partie de l’éternel univers de Havona.",
 "w07.084": "mais le fait que ceux-ci en dérivent cosmiquement est un évènement d’éternité ; en aucun temps — passé, présent ou futur —ni l’espace ni le cosmos matériel ne sont issus de l’Ile nucléaire de Lumière.",
 "w07.090": "En gros, il semble que l’espace prenne son origine juste au-dessous du bas Paradis et le temps juste au-dessus du haut Paradis.",
 "w07.094": "Mille de ces unités constituent une division. Cent-mille divisions égalent une congrégation. Dix millions de congrégations constituent une assemblée. Un milliard d’assemblées forment une grande unité.",
 "w07.118": "C’est un don du Paradis. Nous croyons que l’espace du grand univers et celui de toutes les régions extérieures sont effectivement pénétrés par la puissance d’espace ancestrale de l’Absolu Non Qualifié.",
 "w07.124": "Un niveau d’espace fonctionne donc comme une région elliptique de mouvement entourée de tous côtés par une immobilité relative.",
}
todo = json.load(open(os.path.join(BASE, "work", "todo_fr_c04.json"), encoding="utf-8"))
assert set(todo) == set(Q), set(todo) ^ set(Q)
out = {k: Q[k] for k in todo}
json.dump(out, open(os.path.join(BASE, "fr", "quotes_c04.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
