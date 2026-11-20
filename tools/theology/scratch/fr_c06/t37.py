# -*- coding: utf-8 -*-
from lib import save_units, save_quotes, cut

T = {
"ch37.t": "Le Corps de la Finalité",
"ch37.sub": "La destinée paradisiaque des mortels ascendants",
"ch37.sum": "Les mortels ascendants qui atteignent le Paradis et trouvent Dieu sont enrôlés dans le Corps des Finalitaires Mortels. Autour du noyau formé par les mortels fusionnés avec le Père, le corps comprend des séraphins glorifiés, des natifs de Havona, des médians, des Fils Matériels et des Messagers de Gravité, tous reçus à égalité sans perdre leur individualité. Pourtant, l’arrivée n’est pas la fin. Les finalitaires retournent maintenant servir dans les univers du temps, en recevant ce que l’on pourrait appeler une formation supérieure en administration universelle. Ce chapitre examine la composition du corps, sa mission présente, la mobilisation des sept corps de la finalité et ce que peut impliquer leur destinée non révélée dans les univers de l’espace extérieur.",
"ch37.s1": "La composition du corps",
"ch37.s1.u1.k": "Le Corps des Finalitaires Mortels est la destination présentement connue des mortels fusionnés avec leur Ajusteur.",
"ch37.s1.u1.p": "Au terme de la longue ascension, les mortels arrivent au Corps de la Finalité. Le corps se compose de six groupes : les natifs de Havona, les Messagers de Gravité, les mortels glorifiés, les séraphins adoptés, ainsi que les Fils Matériels et les créatures médianes glorifiés. Ils apportent maintenant leur ministère aux univers de l’espace et administrent les mondes ancrés dans la lumière et la vie, mais le texte conjecture prudemment que leur destination future est constituée par les univers de l’espace extérieur qui s’organisent actuellement.",
"ch37.s1.u2.k": "Les finalitaires embrassent à la fois les parfaits et ceux qui ont été rendus parfaits.",
"ch37.s1.u2.p": "La beauté de ce corps tient à la rencontre d’êtres très différents. Les natifs de Havona, êtres parfaits de création directe, apportent au corps le point de vue de ceux qui sont nés dans la perfection. Beaucoup de gardiens séraphiques qui ont veillé sur des mortels s’élèvent avec leurs pupilles, prêtent le serment finalitaire et acceptent pour toujours la destinée de leurs compagnons mortels. Ceux qui sont parfaits dès le commencement et ceux qui ont été rendus parfaits par l’expérience forment un seul corps.",
"ch37.s1.u3.k": "Tous les finalitaires sont reçus à égalité, mais cette égalité n’efface jamais l’individualité.",
"ch37.s1.u3.p": "Le corps est organisé selon les associations de travail des mondes de l’espace et selon l’expérience accumulée durant la longue carrière ascendante. La plupart de ses membres sont des mortels ascendants, et chaque compagnie de mille n’a de places que pour dix êtres qui ne sont ni mortels ni séraphiques. Tous sont reçus à égalité, mais cette égalité élevée n’abroge jamais l’individualité ni l’identité personnelle. Le principe selon lequel l’unité n’est pas l’uniformité vaut même au Paradis.",
"ch37.s2": "La mission présente des mortels rendus parfaits",
"ch37.s2.u1.k": "Les finalitaires mortels ont trouvé Dieu, mais ils n’ont pas atteint leur destinée finale.",
"ch37.s2.u1.p": "Les finalitaires sont ceux qui ont pleinement obtempéré à l’injonction des âges : « Soyez parfaits ». Ils ont trouvé Dieu et atteint la limite présente de la perfection des créatures. Mais le texte ajoute avec soin que ce n’est pas la finalité du statut spirituel ultime ni du service. Les finalitaires se tiennent seulement à la limite présentement accessible ; la route plus lointaine de l’aboutissement spirituel, du service et de l’expérience de la Déité reste encore ouverte devant eux.",
"ch37.s2.u2.k": "Les finalitaires retournent servir dans les univers du temps, et certains sont toujours présents sur Urantia.",
"ch37.s2.u2.p": "Les ascendeurs qui atteignent le Paradis ne s’y installent pas pour se reposer. Les finalitaires retournent dans les univers du temps, servant dans un superunivers après l’autre et ne recevant d’affectation dans leur superunivers natal qu’après avoir servi dans les six autres. Ils acquièrent ainsi une compréhension septuple de l’Être Suprême. Le texte dit que des compagnies de finalitaires mortels sont toujours en service sur Urantia. Ceux qui nous ont précédés sont dès maintenant à l’œuvre aux côtés de ceux qui les suivent.",
"ch37.s2.u3.k": "Pourquoi les Dieux s’intéressent-ils tant à entrainer aussi minutieusement les mortels survivants à la gestion de l’univers ?",
"ch37.s2.u3.p": "Les affectations présentes des finalitaires ressemblent à des études supérieures sur la compréhension universelle et l’administration superuniverselle. Une question naturelle en découle : à quoi sert toute cette formation ? Le texte ajoute que, même sans aucune destinée future, l’affectation présente justifierait pleinement le plan d’ascension, mais il prévoit que les âges futurs de l’espace extérieur révèleront plus complètement encore la sagesse et la bienveillance affectueuse des Dieux.",
"ch37.s3": "Les sept corps de la finalité et les univers extérieurs",
"ch37.s3.u1.k": "La mobilisation des sept corps finalitaires est la réaction de divinité du grand univers envers l’espace extérieur.",
"ch37.s3.u1.p": "Le Corps des Finalitaires Mortels n’est pas seul. Sept corps de la finalité se rassemblent au Paradis, dont le Corps des Fils Non Révélés de la Destinée. Le texte voit dans cette mobilisation l’activité de la Trinité Ultime qui se prépare à des développements inconcevables dans l’espace extérieur. L’univers se prépare dès maintenant à l’âge suivant.",
"ch37.s3.u2.k": "Les finalitaires en voie de rassemblement sont destinés à un service futur dans les univers de l’espace extérieur.",
"ch37.s3.u2.p": "Les révélateurs admettent franchement qu’ils ne connaissent pas les plans concernant les créations extérieures. Pourtant, ils sont certains de quelques choses : d’immenses univers nouveaux s’organisent dans l’espace extérieur, et la mystérieuse mobilisation des ascendeurs rendus parfaits se poursuit depuis des âges et des âges. En plaçant ces deux mouvements côte à côte, il est naturel de conjecturer que les finalitaires serviront dans les univers extérieurs, où se rassemblent des agrégats de matière plus grands que n’importe quel superunivers actuel.",
"ch37.s3.u3.k": "Nous évoluons dans le Suprême, et il évolue en nous.",
"ch37.s3.u3.p": "Les univers extérieurs seront magnifiques, mais il leur manquera une chose : la participation des êtres ascendants, par l’expérience finie, à l’évolution de l’Être Suprême. Nous subissons maintenant beaucoup de difficultés parce que la souveraineté de Dieu le Suprême n’est pas encore complète, mais c’est précisément pour cette raison que nous participons à l’expérience unique de son évolution. L’inachèvement de l’âge présent est une privation, et en même temps un privilège qui ne reviendra pas.",
"ch37.s4": "La destinée non révélée",
"ch37.s4.u1.k": "La septième place du corps de la finalité est encore vacante.",
"ch37.s4.u1.p": "Chaque compagnie de finalitaires a une place qui n’est pas encore occupée. Il n’existe actuellement que six classes de membres permanents, et même les finalitaires ne savent pas qui sera leur septième camarade. Ce pourrait être un être originaire des univers extérieurs, ou une personnalité du Paradis non encore créée. Cette place vacante est le signe que la théologie n’explique pas tout. Même au terme de l’ascension, il reste un avenir ouvert et une attente.",
"ch37.s4.u2.k": "Les associations du Créateur et de la créature deviendront les dirigeants compatissants des univers futurs.",
"ch37.s4.u2.p": "L’Ajusteur, la plus haute manifestation connue de la Source-Centre Première, et l’homme, la forme la plus humble de vie intelligente capable de connaitre le Père, fusionnent en un seul être. Le texte qualifie cette union mystérieuse de merveilleuse aventure et d’histoire romanesque. Il prévoit que ces enfants du Suprême, ainsi unis, administreront une gigantesque création. Étant partis de la place la plus humble et ayant traversé chaque stade par l’expérience, ils peuvent comprendre ceux qu’ils gouvernent et compatir avec eux. Une origine humble se révèle être une qualification.",
"ch37.s4.u3.k": "Quelle glorieuse destinée pour les enfants temporels d’origine animale !",
"ch37.s4.u3.p": "Naitre sur une planète, passer par les mondes morontiels, gravir les univers spirituels, traverser Havona, trouver Dieu et atteindre le Paradis : le texte appelle cela une glorieuse destinée pour les enfants temporels d’origine animale. Le corps de l’homme est poussière, mais, s’il le veut vraiment et le désire réellement, l’héritage des âges est à lui. La théologie du Corps de la Finalité est, en fin de compte, l’invitation de Dieu adressée à la volonté humaine.",
"ch37.qs1": "En quoi l’enseignement selon lequel un service sans fin nous attend même après avoir trouvé Dieu change-t-il mon idée du salut ?",
"ch37.qs2": "Quel réconfort et quelle responsabilité me donne le fait que ceux qui nous ont précédés servent encore dans ce monde ?",
"ch37.qs3": "Si mes humbles commencements et mes difficultés présentes peuvent un jour me qualifier pour comprendre et servir les autres, comment dois-je considérer les épreuves d’aujourd’hui ?",
}

Q = {
"ch37.s1.u1.q2#0": cut("31:0.8", "Le Corps de la Finalité des Mortels est en cours"),
"ch37.s1.u3.q2#0": cut("31:3.1", "Les mortels ascendants fusionnés", "Corps primaire de la Finalité.") + " … " + cut("31:3.1", "Les natifs de Havona"),
"ch37.s2.u1.q1#0": cut("31:3.6", "Les finalitaires mortels ont pleinement", "statut spirituel ultime."),
"ch37.s2.u3.q1#0": cut("31:3.8", "Il nous semble évident"),
"ch37.s4.u1.q2#0": cut("31:7.5", "L’un de nous estime", "ou trinitisé."),
}

save_units(T)
save_quotes(Q)
