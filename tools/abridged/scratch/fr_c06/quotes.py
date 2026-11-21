import json
Q = {
 "41.b5.q": "Le dernier est parfois le premier, mais en vérité le moindre est devenu le plus grand.",
 "41.b40.q": "Votre monde comptait vraiment parmi les moins importants de toute la création avant que l’effusion de Micaël ait élevé votre planète à une position d’honneur et de grand intérêt pour l’univers.",
 "43.b5.q": "Quand nulle porte n’est ouverte pour recevoir le mal, il n’existe aucune occasion d’entretenir le péché.",
 "43.b21.q": "Les portes des cœurs de tout Édentia se fermèrent devant Satan. Il fut unanimement rejeté par les Souverains de Système assemblés",
 "44.b37.q": "l’âme véritable de l’expression est absente tant que les réalités de la vérité, les significations de la beauté et les valeurs de la bonté ne sont pas unifiées dans l’expérience vivante de l’artisan, du savant ou du philosophe.",
 "45.b5.q": "Un gouvernement représentatif est l’idéal divin de l’autonomie pour les êtres imparfaits.",
 "46.b5.q": "Et Jérusem n’est que le premier pas sur le chemin vers la perfection céleste de la beauté du Paradis.",
 "46.b14.q": "Arrêtez-vous pour considérer que, dans le voyage vers le Paradis, ce premier monde où l’on vous retient est beaucoup plus matériel que spirituel.",
 "48.b31.q": "nulle bonne action n’est jamais entièrement perdue",
}
json.dump(Q, open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged\fr\quotes_c06.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(Q))
