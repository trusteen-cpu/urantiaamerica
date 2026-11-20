# -*- coding: utf-8 -*-
import json, os, sys
H = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(H, ".."))
import amq
src = json.load(open(os.path.join(H, "src", "c06.json"), encoding="utf-8"))
Q = {
"ch28:12": "L’adoration se suffit à elle-même. La prière incorpore un élément d’intérêt pour soi ou pour une autre créature. Telle est la grande différence entre l’adoration et la prière. La vraie adoration ne comporte absolument aucune requête pour soi ni aucun autre élément d’intérêt personnel.",
"ch28:14": "Nous n’adorons pas le Père parce que nous pouvons tirer quelque chose de cette vénération. Nous lui rendons cette dévotion et nous nous engageons dans cette adoration par une réaction naturelle et spontanée, en reconnaissant la personnalité incomparable du Père, et à cause de sa nature digne d’être aimée et de ses attributs adorables.",
"ch28:32": "L’expérience de l’adoration réside dans la tentative sublime de l’Ajusteur fiancé pour communiquer au Père divin les désirs inexprimables et les aspirations indicibles de l’âme humaine",
"ch28:52": "Quelle fructification du plan et du dessein éternels des Dieux quand l’amour intelligent de l’enfant créé donne pleine satisfaction à l’amour infini du Père Créateur !",
"ch29:1": "La prière est le souffle de l’âme et devrait vous inciter à persévérer dans vos tentatives pour mieux connaitre la volonté du Père.",
"ch29:8": "Dieu répond à la prière de l’homme en lui donnant une révélation accrue de la vérité, une appréciation rehaussée de la beauté et un concept élargi de la bonté. La prière est un geste subjectif, mais elle établit le contact avec de puissantes réalités objectives sur les niveaux spirituels de l’expérience humaine",
"ch29:18": "de sorte que l’homme peut ainsi parler, pour ainsi dire, face à face, avec un divin alter ego réel et authentique qui l’habite et qui est l’essence et la présence même du Dieu vivant, le Père Universel.",
"ch29:27": "Cependant, votre persistance n’est pas destinée à gagner la faveur de Dieu, mais à changer votre attitude terrestre et à accroitre la capacité de votre âme à recevoir l’esprit.",
"ch29:51": "Toutes les suppliques authentiquement nées d’esprit sont certaines de recevoir une réponse. Demandez, et vous recevrez, mais n’oubliez pas que vous êtes des créatures qui progressent dans le temps et l’espace.",
"ch29:56": "Il n’existe aucune autre technique permettant à chaque homme, indépendamment de tous autres accomplissements terrestres, d’approcher si efficacement et si immédiatement du seuil du royaume où il peut communiquer avec son Auteur",
"ch30:13": "Les hommes souffrent, en premier lieu, des accidents du temps et des imperfections du mal attachés à une existence physique encore dépourvue de maturité. En second lieu, ils souffrent des conséquences inexorables du péché — de la transgression des lois de la lumière et de la vie.",
"ch30:15": "Vous pouvez toutefois être certains d’une chose, c’est que le Père n’envoie pas d’affliction à titre de châtiment arbitraire pour de mauvaises actions. Les imperfections et les handicaps du mal sont inhérents au mal lui-même ; la punition des péchés est inévitable ; les conséquences destructrices de l’iniquité sont inexorables.",
"ch30:20": "Mais Jésus savait bien qu’il ne pourrait jamais créer un mouvement spirituel durable en s’appuyant sur des prodiges purement matériels. Il avait poursuivi avec persévérance la ligne de conduite consistant à ne pas faire valoir ses prérogatives de créateur.",
"ch30:29": "C’était sa foi et non le contact qui l’avait guérie. Ce cas est un bon exemple des guérisons apparemment miraculeuses qui émaillèrent la carrière terrestre de Jésus",
"ch30:35": "Mais nous avons été informés qu’elles étaient simplement des transformations de mental et d’esprit, comme il peut s’en produire, dans l’expérience de personnes expectantes et dominées par la foi, quand elles se trouvent sous l’influence immédiate et inspirante d’une forte personnalité, positive et bienveillante, dont le ministère bannit la peur et supprime l’anxiété.",
"ch30:37": "Il était tellement victime du sentiment de sa propre impuissance qu’il n’avait pas eu une seule fois l’idée de s’aider lui-même ; or, c’était la seule chose qu’il avait à faire pour se remettre —ramasser son lit et marcher.",
"ch30:41": "il désirait l’utiliser pour apprendre, à ses disciples de l’époque et de tous les siècles ultérieurs, à ne pas mépriser ou négliger les moyens matériels pour guérir les malades. Il voulait leur enseigner qu’ils devaient cesser de considérer les miracles comme la seule méthode de cure pour les maladies humaines.",
"ch30:48": "Si vous pouviez tous être guéris de vos afflictions physiques, vous vous émerveilleriez certainement, mais il est encore plus important que vous soyez purifiés de toute maladie spirituelle et que vous vous trouviez guéris de toutes les infirmités morales.",
"ch30:54": "Donc, même par des souffrances incomprises, Job s’éleva au niveau surhumain de compréhension morale et de clairvoyance spirituelle. Quand le serviteur souffrant obtient une vision de Dieu, il s’ensuit une paix qui surpasse toute compréhension humaine.",
"ch31:8": "Ils commirent la grande erreur d’utiliser le commentaire vivant et illustré de l’évangile du royaume au lieu de cet évangile lui-même, mais même cela représentait la plus grande religion que l’humanité ait connue jusqu’alors.",
"ch31:10": "Dans l’enthousiasme de la Pentecôte, Pierre inaugura involontairement une nouvelle religion, la religion du Christ ressuscité et glorifié. L’apôtre Paul transforma plus tard ce nouvel évangile en christianisme, religion où il incorpora ses propres vues théologiques et décrivit sa propre expérience personnelle avec le Jésus de la route de Damas.",
"ch31:16": "Le christianisme eut l’ambition d’embrasser un programme trop étendu pour qu’un peuple quelconque puisse l’assimiler dans l’espace d’une ou deux générations. Ce programme n’était pas un simple appel spirituel tel que Jésus l’avait présenté à l’âme des hommes. De bonne heure, le christianisme prit nettement position sur les rituels religieux, l’éducation, la magie, la médecine, l’art, la littérature, la loi, le gouvernement, la morale, la règlementation sexuelle, la polygamie et même, dans une mesure limitée, sur l’esclavage.",
"ch31:39": "Toutefois, le christianisme, même celui du vingtième siècle, ne doit pas être méprisé. Il est le produit du génie moral conjugué des hommes connaissant Dieu, venant de multiples races et de nombreux âges ; il a vraiment été l’une des plus grandes puissances bénéfiques sur terre.",
"ch32:3": "La révélation est évolutionnaire, mais toujours progressive. Au long des âges de l’histoire d’un monde, les révélations successives de la religion sont toujours en expansion et plus éclairantes.",
"ch32:7": "Christ Micaël présenta, pour la quatrième fois à Urantia, le concept de Dieu en tant que Père Universel, et en général cet enseignement a toujours subsisté depuis lors. L’essence de son enseignement était l’amour et le service",
"ch32:26": "Le christianisme de Paul assura l’adoration du divin Christ, mais perdit à peu près complètement de vue le Jésus humain de Galilée luttant vaillamment et qui, par la valeur de sa foi religieuse personnelle et l’héroïsme de son Ajusteur intérieur, s’éleva des humbles niveaux de l’humanité pour devenir un avec la divinité",
"ch32:32": "Bien que le concept chrétien de la Trinité fût erroné en fait, il était pratiquement vrai sous le rapport des relations spirituelles.",
"ch32:36": "Toute l’idée de rançon et d’expiation est incompatible avec le concept de Dieu tel qu’il fut enseigné et donné en exemple par Jésus de Nazareth. L’amour infini de Dieu tient la première place dans la nature divine.",
"ch32:38": "Tôt ou tard, un Jean le Baptiste nouveau et plus grand se dressera en proclamant que « le royaume de Dieu est à portée de la main » — signifiant un retour au concept supérieur de Jésus qui proclamait que le royaume est la volonté de son Père céleste, dominante et transcendante, dans le cœur des croyants.",
"ch32:42": "mais vous devriez comprendre que cette Église est seulement l’état larvaire du royaume spirituel contrecarré ; elle fera traverser au royaume le présent âge matériel et le conduira jusqu’à une dispensation plus spirituelle où les enseignements du Maitre trouveront l’occasion de se développer plus pleinement.",
"ch32:44": "Le concept de Jésus est encore vivant dans les religions évoluées du monde. L’Église chrétienne de Paul est l’ombre socialisée et humanisée du royaume des cieux projeté par Jésus — et tel que cependant il deviendra très certainement.",
"ch32:48": "Jésus vivant représente le seul espoir possible d’unifier le christianisme. La véritable Église — la fraternité de Jésus — est invisible, spirituelle et caractérisée par l’unité, mais non nécessairement par l’uniformité.",
"ch32:53": "Le fait de la vie terrestre de Jésus fournit un point d’appui pour l’ancre du temps, tandis que l’effusion de l’Esprit de Vérité assure l’expansion perpétuelle et la croissance indéfinie de la religion que Jésus a vécue et de l’évangile qu’il a proclamé.",
}
todo = json.load(open(os.path.join(H, "work", "todo_fr_c06.json"), encoding="utf-8"))
keys = list(todo) if isinstance(todo, dict) else todo
out = {}
for k in keys:
    v = Q[k]
    ok = amq.check("fr", src[k]["cit"], v)
    if not ok: print("NOT OK", k)
    out[k] = v
json.dump(out, open(os.path.join(H, "fr", "quotes_c06.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "quotes written")
