# -*- coding: utf-8 -*-
# 「유란시아서 소개」 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/intro/index.html
#   극동판 build_intro.py(영어 원본)의 CSS·FONTS·EN 구조를 읽어 오기만 한다(그 파일은 고치지 않음).
#   본문: 영어판(EN) 소개글을 각 언어로 옮긴 것.
#   인용: tools/data/<l>.json(Urantia Foundation 공식 번역)에서 amq.cut 으로 글자 그대로 잘라 오고 amq.check 로 검사.
import html, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(HERE)
SITE = os.path.join(TOOLS, "..", "site")
sys.path.insert(0, TOOLS)
import amq

FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\build_intro.py"
src = open(FE, encoding="utf-8").read()
ns = {"__file__": FE}
exec(src.split("names, links = menu()")[0], ns)          # Q·EN·CSS·FONTS·page 만 읽어 옴(쓰기 없음)
CSS, EN, QEN = ns["CSS"], ns["EN"], ns["Q"]
FONT = ns["FONTS"]["en"]                                   # 라틴 글꼴(악센트 포함)
esc = html.escape

# ── 인용 토막: 영어 토막과 같은 범위를 공식 번역에서 (시작, 끝) 문구로 잘라 온다. None = 절 전체 ──
QL = {
 "es": {
  "fifth": [("Los documentos, de los cuales", "presentaciones de muchos seres.")],
  "god": [("EL Padre Universal", "todas las cosas y todos los seres.")],
  "person": [("Dios es infinito y personal", "una personalidad infinita.")],
  "adj": [("El gran Dios", "la aventura eterna con el hombre.")],
  "plan": None, "death": None,
  "jesus": [("Jesús vivió en la tierra", "hijo de Dios por la fe.")],
  "of": [("Podéis predicar", "debéis vivir la religión de Jesús.")],
  "doubt": [("Las dudas honestas", "hacia el logro de la perfección.")],
  "science": [("No tenemos libertad", "de mil años."), ("dentro de pocos años", "y de nuevos descubrimientos.")],
  "star": [("Jesús nació al mediodía", "5 de diciembre del mismo año.")],
 },
 "fr": {
  "fifth": [("Ces exposés, dont", "par de nombreux êtres.")],
  "god": [("LE Père Universel", "et de tous les êtres.")],
  "person": [("Dieu est à la fois infini", "une personnalité infinie.")],
  "adj": [("Le grand Dieu", "l’aventure éternelle avec l’homme.")],
  "plan": None, "death": None,
  "jesus": [("Jésus vécut et enseigna", "fils de Dieu par la foi.")],
  "of": [("On peut prêcher", "on doit vivre la religion de Jésus.")],
  "doubt": [("Mais les doutes honnêtes", "d’accession à la perfection.")],
  "science": [("Nous ne sommes pas libres", "d’un millénaire."), ("d’ici peu d’années", "et de découvertes nouvelles.")],
  "star": [("Jésus était né le 21", "5 décembre de la même année.")],
 },
 "pt": {
  "fifth": [("Os documentos, dos quais", "efetuadas por muitos seres.")],
  "god": [("O PAI Universal", "todas as coisas e todos os seres.")],
  "person": [("Deus é tanto infinito", "uma personalidade infinita.")],
  "adj": [("O grande Deus", "na aventura eterna.")],
  "plan": None, "death": None,
  "jesus": [("Jesus viveu na Terra", "filho de Deus pela fé.")],
  "of": [("Vós podeis pregar", "deveis viver a religião de Jesus.")],
  "doubt": [("No entanto, as dúvidas honestas","no sentido de alcançar a perfeição.")],
  "science": [("Não temos liberdade", "daqui a mil anos."), ("dentro de uns poucos curtos anos", "e de novas descobertas.")],
  "star": [("Jesus nasceu aos 21", "5 de dezembro do mesmo ano.")],
 },
}


def quote(l, key):
    ref = QEN[key][0]
    segs = QL[l][key]
    if segs is None:
        t = amq.text(l, ref)
    else:
        t = " … ".join(amq.cut(l, ref, a, b) for a, b in segs)
    assert amq.check(l, ref, t), f"[{l}] quote check failed: {key} {ref}"
    return ref, t


def fr_typo(s):
    # 프랑스식 문장부호: « » 안쪽, ; : ! ? 앞에 줄바꿈 없는 공백
    s = s.replace("« ", "«\u00a0").replace(" »", "\u00a0»")
    return re.sub(r" ([;:!?])", "\u00a0\\1", s)


# ── 본문 ──────────────────────────────────────────────
ES = dict(
 lang="es", title="Introducción a El libro de Urantia", eb="EL LIBRO DE URANTIA",
 sub="Qué clase de libro es, cómo llegó a existir y qué enseña",
 toc="En esta página", back="Volver al menú",
 note="Las citas se reproducen textualmente de la traducción oficial de la Fundación Urantia. Haga clic en una referencia para abrir el texto.",
 body=[
  ("h", "¿Qué clase de libro es?"),
  ("p", "«Urantia» es el nombre con que se conoce en el universo a nuestro mundo, la Tierra. El libro de Urantia (The Urantia Book) es un volumen de 2097 páginas compuesto por un Prólogo y 196 documentos, publicado por primera vez en 1955 por la Fundación Urantia en Chicago. Entre sus tapas reúne a Dios y el universo, el origen y la historia de la humanidad, y la vida y las enseñanzas de Jesús."),
  ("p", "En el libro no aparece el nombre de ningún autor humano. Al final de cada documento se identifica a quien lo escribió, y todos ellos son personalidades celestiales, no seres humanos. El libro se presenta como la quinta revelación de época dada a nuestro planeta: una revelación que reúne las grandes revelaciones anteriores y vuelve a exponer la verdad en términos que una persona moderna puede comprender."),
  ("q", "fifth"),
  ("p", "Sin embargo, el libro no afirma ser completo. En el mismo pasaje añade que ninguna revelación puede ser completa hasta que se llegue al Padre Universal. Esa humildad es una de las primeras cosas que advierte un lector nuevo."),

  ("h", "¿Cómo surgió el libro?"),
  ("p", "La historia comienza en Chicago, en el verano de 1911. Una mujer acudió a un vecino, el médico William S. Sadler, porque su marido se comportaba de manera extraña mientras dormía y por la mañana no recordaba nada. El Dr. Sadler era un pionero de la psiquiatría y era bien conocido por desenmascarar los trucos de médiums y espiritistas. Trató al hombre como a un paciente y se propuso encontrar la causa."),
  ("p", "Pero las palabras que llegaban a través del hombre dormido no eran ni su voz ni sus intereses. Quienes hablaban no se describían como espíritus de muertos, sino como «estudiantes visitantes» de otros mundos. Durante años el Dr. Sadler observó y puso a prueba el fenómeno, pero no logró explicar su origen. En el apéndice de su libro de 1929, <i>The Mind at Mischief</i>, escribió con cautela sobre un caso especial que no podía clasificar."),
  ("p", "A mediados de la década de 1920, un círculo de amigos que se reunía en la casa de los Sadler —conocido más tarde como el Foro— se sumó a la investigación. Cuando las preguntas escritas de los miembros, varios cientos, se ordenaron y se guardaron, algún tiempo después aparecieron respuestas manuscritas a esas mismas preguntas. La letra no coincidía ni con la del hombre dormido ni con la de su esposa. Mediante este intercambio de preguntas y respuestas, el material creció en amplitud y profundidad, y hacia 1935 todos los documentos, hasta el relato final de la vida de Jesús, estaban completos."),
  ("p", "La publicación todavía requirió años de preparación. La Fundación Urantia se estableció en 1950, y el libro apareció en octubre de 1955. Después de eso el contacto cesó, y la identidad del hombre dormido nunca se hizo pública. Cómo se escribió el libro sigue siendo un misterio hasta el día de hoy."),
  ("p", "El Dr. Sadler fue toda su vida un escéptico que no dejaba de indagar; sin embargo, llegó a creer que ninguna persona sola podría haber producido una obra así. Al final sostuvo que lo que dice el libro importa más que quién lo escribió: si una sinfonía es verdaderamente hermosa, ¿importa tanto quién la compuso? La mejor manera de acercarse al libro es la misma: leerlo y juzgarlo por su contenido."),

  ("h", "Las cuatro partes"),
  ("p", "En lugar de ascender de las cosas pequeñas a las grandes, El libro de Urantia comienza con el Dios infinito y desciende hasta nuestro propio planeta y la vida de Jesús."),
  ("t", [["Parte", "Documentos", "Contenido"],
         ["Parte I  El universo central y los superuniversos", "1–31", "La naturaleza de Dios, el Paraíso, el perfecto universo central de Havona, los siete superuniversos y sus seres"],
         ["Parte II  El universo local", "32–56", "La estructura y el gobierno de nuestro universo local, Nebadon; los ángeles y las numerosas órdenes de hijos; el camino de ascensión que continúa después de la muerte"],
         ["Parte III  La historia de Urantia", "57–119", "El origen del sistema solar y de la Tierra, la evolución de la vida, la historia de la humanidad, de la civilización y de la religión, y la mente y el alma del hombre en relación con Dios"],
         ["Parte IV  La vida y las enseñanzas de Jesús", "120–196", "Un relato día a día desde el nacimiento de Jesús, pasando por su infancia, los años desconocidos y su ministerio público, hasta la cruz y la resurrección"]]),
  ("p", "La Parte IV ocupa casi un tercio del libro. Describe con detalle años que los Evangelios pasan por alto: la infancia y la juventud de Jesús, los años como carpintero que sostenía a su familia y sus largos viajes por el extranjero."),

  ("h", "Enseñanzas centrales"),
  ("p", "<b>Dios es un Padre amoroso y una persona.</b> El primer documento presenta a Dios como la fuente de toda la creación y como un Padre que conoce y ama personalmente a cada uno de nosotros. Dios no es una fuerza ni una ley impersonal, sino una personalidad infinita a quien podemos conocer y de quien podemos ser amigos."),
  ("q", "god"), ("q", "person"),
  ("p", "<b>Dios vive dentro de cada persona.</b> Dios envía un fragmento de su propio espíritu, el Ajustador del Pensamiento, a morar en la mente de cada uno de nosotros. Este espíritu interior nos guía hacia la verdad y la bondad y nos ayuda a avanzar hacia la vida eterna."),
  ("q", "adj"),
  ("p", "<b>El universo tiene un propósito, y la vida no termina con la muerte.</b> El universo es la casa bien ordenada de Dios, y hay vida en innumerables mundos. Cuando termina esta vida terrenal, la persona puede comenzar el largo ascenso de universo en universo hasta encontrarse por fin ante Dios en el Paraíso. Tomar ese camino es una libre elección de cada persona."),
  ("q", "plan"), ("q", "death"),
  ("p", "<b>Todas las personas son hijos de Dios y hermanos y hermanas entre sí.</b> La verdad de que Dios es nuestro Padre no puede separarse de la verdad de que toda la humanidad es una sola familia. Una vida de amor a Dios se manifiesta naturalmente en el servicio a los demás."),
  ("p", "<b>Jesús es el Hijo Creador de nuestro universo.</b> El libro de Urantia presenta a Jesús de Nazaret como Micael, el Hijo de Dios que creó y gobierna nuestro universo local, viviendo como hombre entre nosotros. En esa vida Jesús mostró cómo es Dios y despertó a las personas a la verdad de que son hijos de Dios por la fe."),
  ("q", "jesus"),
  ("p", "<b>La ciencia, la filosofía y la religión se encuentran en una sola realidad.</b> El libro trata la ciencia, que se ocupa de los hechos, la filosofía, que busca los significados, y la religión, que experimenta los valores, no como rivales sino como tres ventanas abiertas a una sola realidad. También desarrolla conceptos nuevos que rara vez se encuentran en otra parte, como Dios el Supremo, que crece en el tiempo y el espacio."),

  ("h", "Relación con las religiones existentes y con la Biblia"),
  ("p", "Detrás de El libro de Urantia no hay ninguna iglesia ni denominación. El libro no pide a nadie que funde una nueva religión y no prescribe rituales ni ceremonias. Los lectores conservan su propia fe mientras leen, y estudian solos o en pequeños grupos de estudio. El libro considera la religión verdadera, ante todo, como la experiencia viva de una persona con Dios."),
  ("p", "El libro armoniza profundamente con las enseñanzas espirituales de la Biblia: la fe, la esperanza y el amor, la gracia y la vida eterna. Sin embargo, en algunos puntos difiere de la interpretación tradicional. No acepta la doctrina de que Dios exigió la sangre de su Hijo como expiación, ni la doctrina de que todas las personas heredan el pecado de Adán, ni la idea de que cada palabra de las Escrituras está libre de error. Dios nos ha amado desde el principio, y Jesús vivió y murió no para aplacar a Dios, sino para revelar su amor."),
  ("p", "Por eso el libro invita a volver de una religión sobre Jesús a la religión de Jesús: a vivir la misma fe que Jesús enseñó y vivió, confiando en Dios como Padre y amando a las personas como hermanos y hermanas."),
  ("q", "of"),

  ("h", "¿Cómo debemos juzgarlo?"),
  ("p", "Nadie puede decidir por otro si El libro de Urantia es una revelación. El propio libro no pide una creencia ciega y acoge las preguntas sinceras."),
  ("q", "doubt"),
  ("p", "Los lectores de muchos años suelen proponer algunas pruebas. ¿Forman más de dos mil páginas un todo coherente, sin contradicciones? ¿Resuena el libro como verdadero en lo profundo del corazón? ¿Glorifica a Dios en lugar de servir a los intereses de alguien? ¿Es respetuoso y abierto hacia otras creencias? Y, sobre todo, ¿mejora realmente la vida cuando se viven sus enseñanzas? Por sus frutos se conoce el árbol."),
  ("p", "Algunos lectores señalan detalles inesperados. El libro afirma, con fechas exactas, que en el año del nacimiento de Jesús Júpiter y Saturno estuvieron en conjunción tres veces, y explica que esto dio origen a la leyenda de la estrella de Belén, algo que el cálculo astronómico moderno puede confirmar."),
  ("q", "star"),
  ("p", "Al mismo tiempo, el libro dice abiertamente que sus afirmaciones científicas están sujetas al conocimiento de la época y necesitarán revisión; a los reveladores no se les permitió dar a conocer hechos que los seres humanos aún no habían descubierto. Vale la pena tener presente esa franqueza durante la lectura."),
  ("q", "science"),

  ("h", "Por dónde empezar"),
  ("p", "El libro puede leerse desde el principio, pero al comienzo puede parecer difícil. Muchos lectores empiezan por la Parte IV, la vida de Jesús, o por una guía más sencilla. Los siguientes recursos de este sitio pueden ayudar en los primeros pasos."),
  ("links", [("text", "El texto completo: lea los 196 documentos en el lector digital"),
             ("youth", "El libro de Urantia contado de forma sencilla para jóvenes lectores"),
             ("abridged", "El Prólogo y los 196 documentos en forma abreviada"),
             ("commentary", "Un comentario de cada documento"),
             ("lists", "376 listas clave del texto"),
             ("maps", "Mapas de la vida de Jesús"),
             ("glossary", "Un glosario de términos poco conocidos")]),
 ],
)

FR = dict(
 lang="fr", title="Introduction au Livre d’Urantia", eb="LE LIVRE D’URANTIA",
 sub="Quel genre de livre c’est, comment il a vu le jour et ce qu’il enseigne",
 toc="Sur cette page", back="Retour au menu",
 note="Les citations sont reproduites mot pour mot d’après la traduction officielle de la Fondation Urantia. Cliquez sur une référence pour ouvrir le texte.",
 body=[
  ("h", "Quel genre de livre est-ce ?"),
  ("p", "« Urantia » est le nom sous lequel notre monde, la terre, est connu dans l’univers. Le Livre d’Urantia (The Urantia Book) est un volume de 2\u00a0097 pages composé d’une Introduction et de 196 fascicules, publié pour la première fois en 1955 par la Fondation Urantia à Chicago. Il rassemble entre ses couvertures Dieu et l’univers, l’origine et l’histoire de l’humanité, ainsi que la vie et les enseignements de Jésus."),
  ("p", "Aucun nom d’auteur humain n’apparaît dans le livre. À la fin de chaque fascicule, l’auteur est identifié, et tous sont des personnalités célestes, non des êtres humains. Le livre se présente comme la cinquième révélation d’époque donnée à notre planète — une révélation qui rassemble les grandes révélations antérieures et expose à nouveau la vérité en des termes qu’une personne d’aujourd’hui peut saisir."),
  ("q", "fifth"),
  ("p", "Pourtant, le livre ne prétend pas être complet. Dans le même passage, il ajoute qu’aucune révélation ne peut jamais être complète avant d’atteindre le Père Universel. Cette humilité est l’une des premières choses que remarque un nouveau lecteur."),

  ("h", "Comment le livre a-t-il vu le jour ?"),
  ("p", "L’histoire commence à Chicago, à l’été 1911. Une femme vint trouver un voisin, le médecin William S. Sadler, parce que son mari se comportait étrangement pendant son sommeil et ne se souvenait de rien le matin. Le Dr Sadler était un pionnier de la psychiatrie et il était bien connu pour démasquer les supercheries des médiums et des spirites. Il traita l’homme comme un patient et entreprit d’en trouver la cause."),
  ("p", "Mais les paroles qui passaient par l’homme endormi n’étaient ni sa voix ni ses centres d’intérêt. Ceux qui parlaient se présentaient non comme des esprits de défunts, mais comme des « étudiants visiteurs » venus d’autres mondes. Pendant des années, le Dr Sadler observa et mit le phénomène à l’épreuve, sans pouvoir en expliquer la source. Dans l’appendice de son livre de 1929, <i>The Mind at Mischief</i>, il évoqua avec prudence un cas particulier qu’il était incapable de classer."),
  ("p", "Au milieu des années 1920, un cercle d’amis qui se réunissait chez les Sadler — connu plus tard sous le nom de Forum — se joignit à l’enquête. Lorsque les questions écrites des membres, plusieurs centaines, eurent été triées et rangées, des réponses manuscrites à ces mêmes questions apparurent quelque temps plus tard. L’écriture ne correspondait ni à celle de l’homme endormi ni à celle de sa femme. Grâce à cet échange de questions et de réponses, la matière gagna en ampleur et en profondeur, et vers 1935 tous les fascicules, jusqu’au récit final de la vie de Jésus, étaient achevés."),
  ("p", "La publication exigea encore des années de préparation. La Fondation Urantia fut créée en 1950, et le livre parut en octobre 1955. Après cela, le contact cessa, et l’identité de l’homme endormi ne fut jamais rendue publique. La manière dont le livre a été écrit reste un mystère aujourd’hui encore."),
  ("p", "Le Dr Sadler resta toute sa vie un sceptique en quête de réponses, mais il en vint à croire qu’aucune personne seule n’aurait pu produire une telle œuvre. Il estima finalement que ce que dit le livre importe davantage que l’identité de son auteur : si une symphonie est vraiment belle, importe-t-il tant de savoir qui l’a composée ? La meilleure manière d’aborder le livre est la même : le lire et le juger d’après son contenu."),

  ("h", "Les quatre parties"),
  ("p", "Plutôt que de s’élever des petites choses vers les grandes, le Livre d’Urantia commence par le Dieu infini et descend jusqu’à notre propre planète et à la vie de Jésus."),
  ("t", [["Partie", "Fascicules", "Contenu"],
         ["Partie I  L’univers central et les superunivers", "1–31", "La nature de Dieu, le Paradis, l’univers central parfait de Havona, les sept superunivers et leurs êtres"],
         ["Partie II  L’univers local", "32–56", "La structure et le gouvernement de notre univers local, Nébadon ; les anges et les nombreux ordres de fils ; le chemin d’ascension qui se poursuit après la mort"],
         ["Partie III  L’histoire d’Urantia", "57–119", "L’origine du système solaire et de la terre, l’évolution de la vie, l’histoire de l’humanité, de la civilisation et de la religion, ainsi que le mental et l’âme de l’homme dans leur relation avec Dieu"],
         ["Partie IV  La vie et les enseignements de Jésus", "120–196", "Un récit jour après jour, depuis la naissance de Jésus, à travers son enfance, les années inconnues et son ministère public, jusqu’à la croix et la résurrection"]]),
  ("p", "La Partie IV occupe près d’un tiers du livre. Elle décrit en détail des années que les Évangiles passent sous silence : l’enfance et la jeunesse de Jésus, ses années de charpentier subvenant aux besoins de sa famille, et ses longs voyages à l’étranger."),

  ("h", "Enseignements essentiels"),
  ("p", "<b>Dieu est un Père aimant et une personne.</b> Le premier fascicule présente Dieu comme la source de toute la création et comme un Père qui connaît et aime chacun de nous personnellement. Dieu n’est pas une force ou une loi impersonnelle, mais une personnalité infinie que nous pouvons connaître et dont nous pouvons devenir les amis."),
  ("q", "god"), ("q", "person"),
  ("p", "<b>Dieu vit en chaque personne.</b> Dieu envoie un fragment de son propre esprit, l’Ajusteur de Pensée, habiter le mental de chacun de nous. Cet esprit intérieur nous conduit vers la vérité et la bonté et nous aide à progresser vers la vie éternelle."),
  ("q", "adj"),
  ("p", "<b>L’univers a un dessein, et la vie ne s’arrête pas à la mort.</b> L’univers est la maison bien ordonnée de Dieu, et la vie existe sur d’innombrables mondes. Quand cette vie terrestre s’achève, une personne peut commencer la longue ascension d’univers en univers jusqu’à se tenir enfin devant Dieu au Paradis. Prendre ce chemin relève du libre choix de chacun."),
  ("q", "plan"), ("q", "death"),
  ("p", "<b>Tous les hommes sont enfants de Dieu, frères et sœurs les uns des autres.</b> La vérité que Dieu est notre Père ne peut être séparée de la vérité que toute l’humanité forme une seule famille. Une vie d’amour pour Dieu se manifeste naturellement dans le service des autres."),
  ("p", "<b>Jésus est le Fils Créateur de notre univers.</b> Le Livre d’Urantia présente Jésus de Nazareth comme Micaël, le Fils de Dieu qui a créé et qui gouverne notre univers local, vivant comme un homme parmi nous. Dans cette vie, Jésus a montré ce qu’est Dieu et a éveillé les hommes à la vérité qu’ils sont fils de Dieu par la foi."),
  ("q", "jesus"),
  ("p", "<b>La science, la philosophie et la religion se rejoignent dans une seule réalité.</b> Le livre considère la science, qui traite des faits, la philosophie, qui cherche les significations, et la religion, qui fait l’expérience des valeurs, non comme des rivales mais comme trois fenêtres ouvertes sur une seule réalité. Il expose aussi des concepts nouveaux que l’on trouve rarement ailleurs, comme Dieu le Suprême, qui croît dans le temps et l’espace."),

  ("h", "Rapport avec les religions existantes et la Bible"),
  ("p", "Aucune Église ni dénomination ne se tient derrière le Livre d’Urantia. Il ne demande à personne de fonder une nouvelle religion et ne prescrit ni rituels ni cérémonies. Les lecteurs gardent leur propre foi en le lisant et l’étudient seuls ou en petits groupes d’étude. Le livre considère la vraie religion avant tout comme l’expérience vivante d’une personne avec Dieu."),
  ("p", "Le livre s’harmonise profondément avec les enseignements spirituels de la Bible — la foi, l’espérance et l’amour, la grâce et la vie éternelle. Sur quelques points, toutefois, il diffère de l’interprétation traditionnelle. Il n’accepte ni la doctrine selon laquelle Dieu aurait exigé le sang de son Fils en expiation, ni la doctrine selon laquelle le péché d’Adam serait hérité par tous les hommes, ni l’idée que chaque mot de l’Écriture serait exempt d’erreur. Dieu nous a aimés depuis le commencement, et Jésus a vécu et est mort non pour apaiser Dieu, mais pour révéler son amour."),
  ("p", "Le livre invite donc à revenir d’une religion à propos de Jésus à la religion de Jésus : vivre la foi même que Jésus a enseignée et vécue, en se confiant en Dieu comme en un Père et en aimant les hommes comme des frères et des sœurs."),
  ("q", "of"),

  ("h", "Comment le juger ?"),
  ("p", "Nul ne peut décider à la place d’un autre si le Livre d’Urantia est une révélation. Le livre lui-même ne demande aucune croyance aveugle et accueille les questions honnêtes."),
  ("q", "doubt"),
  ("p", "Les lecteurs de longue date proposent souvent quelques critères. Plus de deux mille pages forment-elles un tout cohérent, sans contradiction ? Le livre sonne-t-il vrai au plus profond du cœur ? Glorifie-t-il Dieu plutôt que de servir les intérêts de quiconque ? Est-il respectueux et ouvert envers les autres croyances ? Et surtout, la vie devient-elle réellement meilleure lorsqu’on vit ses enseignements ? On reconnaît l’arbre à ses fruits."),
  ("p", "Certains lecteurs relèvent des détails inattendus. Le livre affirme, dates précises à l’appui, que l’année de la naissance de Jésus, Jupiter et Saturne furent trois fois en conjonction, et explique que ce fut là l’origine de la légende de l’étoile de Bethléem — ce que le calcul astronomique moderne peut confirmer."),
  ("q", "star"),
  ("p", "En même temps, le livre dit ouvertement que ses affirmations scientifiques sont liées aux connaissances de l’époque et devront être révisées ; les révélateurs n’étaient pas autorisés à dévoiler des faits que les hommes n’avaient pas encore découverts. Il vaut la peine de garder cette franchise à l’esprit en lisant."),
  ("q", "science"),

  ("h", "Par où commencer"),
  ("p", "On peut lire le livre depuis le début, mais il peut sembler difficile au premier abord. Beaucoup de lecteurs commencent par la Partie IV, la vie de Jésus, ou par un guide plus simple. Les ressources suivantes de ce site peuvent aider à faire les premiers pas."),
  ("links", [("text", "Le texte intégral — lisez les 196 fascicules dans la liseuse numérique"),
             ("youth", "Le Livre d’Urantia raconté simplement pour les jeunes lecteurs"),
             ("abridged", "L’Introduction et les 196 fascicules sous forme abrégée"),
             ("commentary", "Un commentaire de chaque fascicule"),
             ("lists", "376 listes clés tirées du texte"),
             ("maps", "Cartes de la vie de Jésus"),
             ("glossary", "Un glossaire des termes peu familiers")]),
 ],
)

PT = dict(
 lang="pt", title="Introdução a O Livro de Urântia", eb="O LIVRO DE URÂNTIA",
 sub="Que tipo de livro é, como surgiu e o que ensina",
 toc="Nesta página", back="Voltar ao menu",
 note="As citações foram transcritas literalmente da tradução oficial da Fundação Urantia. Clique numa referência para abrir o texto.",
 body=[
  ("h", "Que tipo de livro é este?"),
  ("p", "“Urântia” é o nome pelo qual o nosso mundo, a Terra, é conhecido no universo. O Livro de Urântia (The Urantia Book) é um volume de 2.097 páginas composto de uma Introdução e de 196 documentos, publicado pela primeira vez em 1955 pela Fundação Urantia, em Chicago. Entre as suas capas, reúne Deus e o universo, a origem e a história da humanidade, e a vida e os ensinamentos de Jesus."),
  ("p", "Nenhum nome de autor humano aparece no livro. Ao final de cada documento, o autor é identificado, e todos eles são personalidades celestes, e não seres humanos. O livro apresenta-se como a quinta revelação epocal dada ao nosso planeta — uma revelação que reúne as grandes revelações anteriores e reapresenta a verdade em termos que uma pessoa moderna pode compreender."),
  ("q", "fifth"),
  ("p", "Contudo, o livro não afirma ser completo. Na mesma passagem, acrescenta que nenhuma revelação pode jamais ser completa antes de se alcançar o Pai Universal. Essa humildade é uma das primeiras coisas que um novo leitor percebe."),

  ("h", "Como o livro surgiu?"),
  ("p", "A história começa em Chicago, no verão de 1911. Uma mulher procurou um vizinho, o médico William S. Sadler, porque o marido se comportava de modo estranho enquanto dormia e de manhã não se lembrava de nada. O Dr. Sadler era um pioneiro da psiquiatria e era bem conhecido por desmascarar os truques de médiuns e espíritas. Ele tratou o homem como paciente e procurou descobrir a causa."),
  ("p", "Mas as palavras que vinham por meio do homem adormecido não eram nem a sua voz nem os seus interesses. Os que falavam não se descreviam como espíritos de mortos, mas como “estudantes visitantes” de outros mundos. Durante anos, o Dr. Sadler observou e testou o fenômeno, mas não conseguiu explicar a sua origem. No apêndice do seu livro de 1929, <i>The Mind at Mischief</i>, escreveu com cautela sobre um caso especial que não conseguia classificar."),
  ("p", "Em meados da década de 1920, um círculo de amigos que se reunia na casa dos Sadler — mais tarde conhecido como o Fórum — juntou-se à investigação. Depois que as perguntas escritas dos membros, várias centenas delas, foram organizadas e guardadas, algum tempo depois apareceram respostas manuscritas a essas mesmas perguntas. A caligrafia não correspondia nem à do homem adormecido nem à da sua esposa. Por meio dessa troca de perguntas e respostas, o material cresceu em amplitude e profundidade, e por volta de 1935 todos os documentos, até o relato final da vida de Jesus, estavam completos."),
  ("p", "A publicação ainda exigiu anos de preparação. A Fundação Urantia foi criada em 1950, e o livro foi lançado em outubro de 1955. Depois disso, o contato cessou, e a identidade do homem adormecido nunca foi tornada pública. Como o livro foi escrito continua sendo um mistério até hoje."),
  ("p", "O Dr. Sadler foi a vida inteira um cético que não deixava de investigar, mas passou a crer que nenhuma pessoa sozinha poderia ter produzido uma obra como essa. Por fim, sustentou que o que o livro diz importa mais do que quem o escreveu: se uma sinfonia é verdadeiramente bela, importa tanto quem a compôs? A melhor maneira de abordar o livro é a mesma: lê-lo e julgá-lo pelo seu conteúdo."),

  ("h", "As quatro partes"),
  ("p", "Em vez de subir das coisas pequenas para as grandes, O Livro de Urântia começa com o Deus infinito e desce até o nosso próprio planeta e a vida de Jesus."),
  ("t", [["Parte", "Documentos", "Conteúdo"],
         ["Parte I  O universo central e os superuniversos", "1–31", "A natureza de Deus, o Paraíso, o perfeito universo central de Havona, os sete superuniversos e os seus seres"],
         ["Parte II  O universo local", "32–56", "A estrutura e o governo do nosso universo local, Nébadon; os anjos e as muitas ordens de filhos; o caminho de ascensão que continua após a morte"],
         ["Parte III  A história de Urântia", "57–119", "A origem do sistema solar e da Terra, a evolução da vida, a história da humanidade, da civilização e da religião, e a mente e a alma do homem em sua relação com Deus"],
         ["Parte IV  A vida e os ensinamentos de Jesus", "120–196", "Um relato dia a dia, desde o nascimento de Jesus, passando pela infância, pelos anos desconhecidos e pelo ministério público, até a cruz e a ressurreição"]]),
  ("p", "A Parte IV ocupa quase um terço do livro. Descreve em detalhes anos que os Evangelhos deixam de lado: a infância e a juventude de Jesus, os anos como carpinteiro que sustentava a família e as suas longas viagens ao exterior."),

  ("h", "Ensinamentos centrais"),
  ("p", "<b>Deus é um Pai amoroso e uma pessoa.</b> O primeiro documento apresenta Deus como a fonte de toda a criação e como um Pai que conhece e ama pessoalmente cada um de nós. Deus não é uma força ou uma lei impessoal, mas uma personalidade infinita que podemos conhecer e de quem podemos ser amigos."),
  ("q", "god"), ("q", "person"),
  ("p", "<b>Deus vive dentro de cada pessoa.</b> Deus envia um fragmento do Seu próprio espírito, o Ajustador do Pensamento, para residir na mente de cada um de nós. Esse espírito interior nos conduz à verdade e à bondade e nos ajuda a avançar rumo à vida eterna."),
  ("q", "adj"),
  ("p", "<b>O universo tem um propósito, e a vida não termina com a morte.</b> O universo é a casa bem ordenada de Deus, e há vida em incontáveis mundos. Quando esta vida terrena termina, a pessoa pode iniciar a longa ascensão de universo em universo, até estar por fim diante de Deus no Paraíso. Seguir esse caminho é uma livre escolha de cada um."),
  ("q", "plan"), ("q", "death"),
  ("p", "<b>Todas as pessoas são filhos de Deus e irmãos e irmãs umas das outras.</b> A verdade de que Deus é nosso Pai não pode ser separada da verdade de que toda a humanidade é uma só família. Uma vida de amor a Deus manifesta-se naturalmente no serviço aos outros."),
  ("p", "<b>Jesus é o Filho Criador do nosso universo.</b> O Livro de Urântia apresenta Jesus de Nazaré como Michael, o Filho de Deus que criou e governa o nosso universo local, vivendo como homem entre nós. Nessa vida, Jesus mostrou como Deus é e despertou as pessoas para a verdade de que são filhos de Deus pela fé."),
  ("q", "jesus"),
  ("p", "<b>Ciência, filosofia e religião encontram-se numa só realidade.</b> O livro trata a ciência, que lida com os fatos, a filosofia, que busca os significados, e a religião, que experiencia os valores, não como rivais, mas como três janelas abertas para uma só realidade. Também desenvolve conceitos novos raramente encontrados em outros lugares, como Deus, o Supremo, que cresce no tempo e no espaço."),

  ("h", "Relação com as religiões existentes e com a Bíblia"),
  ("p", "Não há igreja nem denominação por trás de O Livro de Urântia. O livro não pede a ninguém que funde uma nova religião e não prescreve rituais nem cerimônias. Os leitores mantêm a própria fé enquanto leem e estudam sozinhos ou em pequenos grupos de estudo. O livro considera a verdadeira religião, acima de tudo, como a experiência viva de uma pessoa com Deus."),
  ("p", "O livro harmoniza-se profundamente com os ensinamentos espirituais da Bíblia — a fé, a esperança e o amor, a graça e a vida eterna. Em alguns pontos, porém, difere da interpretação tradicional. Não aceita a doutrina de que Deus exigiu o sangue do Seu Filho como expiação, nem a doutrina de que o pecado de Adão é herdado por todas as pessoas, nem a ideia de que cada palavra das Escrituras está isenta de erro. Deus nos ama desde o princípio, e Jesus viveu e morreu não para aplacar a Deus, mas para revelar o Seu amor."),
  ("p", "Por isso, o livro convida a voltar de uma religião sobre Jesus para a religião de Jesus: viver a mesma fé que Jesus ensinou e viveu, confiando em Deus como Pai e amando as pessoas como irmãos e irmãs."),
  ("q", "of"),

  ("h", "Como devemos julgá-lo?"),
  ("p", "Ninguém pode decidir por outra pessoa se O Livro de Urântia é uma revelação. O próprio livro não pede crença cega e acolhe perguntas honestas."),
  ("q", "doubt"),
  ("p", "Leitores de longa data costumam sugerir alguns critérios. Mais de duas mil páginas formam um todo coerente, sem contradições? O livro soa verdadeiro no fundo do coração? Glorifica a Deus, em vez de servir aos interesses de alguém? É respeitoso e aberto para com outras crenças? E, acima de tudo, a vida realmente se torna melhor quando os seus ensinamentos são vividos? Pelos frutos se conhece a árvore."),
  ("p", "Alguns leitores apontam detalhes inesperados. O livro afirma, com datas exatas, que no ano do nascimento de Jesus Júpiter e Saturno entraram em conjunção três vezes, e explica que isso deu origem à lenda da estrela de Belém — algo que o cálculo astronômico moderno pode confirmar."),
  ("q", "star"),
  ("p", "Ao mesmo tempo, o livro diz abertamente que as suas afirmações científicas estão presas ao conhecimento da época e precisarão de revisão; os reveladores não tinham permissão para revelar fatos que os seres humanos ainda não haviam descoberto. Vale a pena ter em mente essa franqueza durante a leitura."),
  ("q", "science"),

  ("h", "Por onde começar"),
  ("p", "O livro pode ser lido desde o início, mas de começo pode parecer difícil. Muitos leitores começam pela Parte IV, a vida de Jesus, ou por um guia mais simples. Os recursos a seguir, neste site, podem ajudar nos primeiros passos."),
  ("links", [("text", "O texto integral — leia os 196 documentos no leitor digital"),
             ("youth", "O Livro de Urântia contado de forma simples para jovens leitores"),
             ("abridged", "A Introdução e os 196 documentos em forma resumida"),
             ("commentary", "Um comentário de cada documento"),
             ("lists", "376 listas-chave do texto"),
             ("maps", "Mapas da vida de Jesus"),
             ("glossary", "Um glossário de termos pouco conhecidos")]),
 ],
)


# ── i18n.js 에서 메뉴 이름·언어별 주소 ───────────────────
def site_menu():
    t = open(os.path.join(SITE, "i18n.js"), encoding="utf-8").read()
    names = {}
    for m in re.finditer(r'\{ id: "(\w+)",(.*?)\}', t[t.index("menu:"):t.index("links:")]):
        names[m.group(1)] = dict(re.findall(r'(\w+): "([^"]*)"', m.group(2)))
    links = {}
    for l in amq.LANGS:
        blk = re.search(r'\b' + l + r': \{(.*?)\}', t[t.index("links:"):], re.S).group(1)
        links[l] = dict(re.findall(r'(\w+): "([^"]+)"', blk))
    return names, links


def menu_href(l, mid, links):
    h = links[l].get(mid)
    if h:  # 예: "es/book/" → "/es/book/" (http 주소는 그대로)
        return h if h.startswith("http") else "/" + h
    return f"/soon.html?p={mid}&lang={l}"


def page(D, links, names):
    l = D["lang"]; font, sans, fonts = FONT
    T = fr_typo if l == "fr" else (lambda s: s)
    css = CSS.replace("{font}", font).replace("{sans}", sans)
    heads = [T(b[1]) for b in D["body"] if b[0] == "h"]
    o = [f'<!DOCTYPE html>\n<html lang="{l}">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1">\n'
         f'<title>{esc(D["title"])}</title>\n<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         f'<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">\n<style>{css}</style>\n'
         f'<script src="/home-button.js" defer></script>\n</head>\n<body>\n'
         f'<header class="top"><div class="eb">{esc(D["eb"])}</div><h1>{esc(D["title"])}</h1><p>{esc(T(D["sub"]))}</p></header>\n<div class="wrap">',
         f'<nav class="toc"><b>{esc(D["toc"])}</b><ol>' + "".join(f'<li><a href="#s{i+1}">{esc(h)}</a></li>' for i, h in enumerate(heads)) + "</ol></nav>"]
    hi = nq = 0
    for kind, v in D["body"]:
        if kind == "h":
            hi += 1; o.append(f'<h2 id="s{hi}">{esc(T(v))}</h2>')
        elif kind == "p":
            o.append(f"<p>{T(v)}</p>")  # 문단 안의 <b>·<i> 는 의도한 꾸밈
        elif kind == "q":
            ref, t = quote(l, v)       # 인용은 공식 번역 그대로(문장부호도 손대지 않음)
            o.append(f'<div class="q">{esc(t)}<a href="{amq.link(l, ref)}">{ref}</a></div>'); nq += 1
        elif kind == "t":
            o.append('<div class="tw"><table><thead><tr>' + "".join(f"<th>{esc(T(c))}</th>" for c in v[0]) + "</tr></thead><tbody>" +
                     "".join("<tr>" + "".join(f"<td>{esc(T(c))}</td>" for c in r) + "</tr>" for r in v[1:]) + "</tbody></table></div>")
        elif kind == "links":
            o.append('<div class="links">' + "".join(
                f'<a href="{esc(menu_href(l, mid, links))}"><b>{esc(names[mid][l])}</b> — {esc(T(desc))}</a>' for mid, desc in v) + "</div>")
    o.append(f'<p class="note">{esc(D["note"])}</p><a class="back" href="/{l}/">{esc(D["back"])}</a>\n</div>\n</body>\n</html>\n')
    return "\n".join(o), nq


def shape(body):
    # 구조 비교용: 종류·인용키·표 크기·링크 메뉴 id
    out = []
    for k, v in body:
        if k == "q": out.append(("q", v))
        elif k == "t": out.append(("t", len(v), len(v[0])))
        elif k == "links": out.append(("links", tuple(m for m, _ in v)))
        else: out.append((k,))
    return out


names, links = site_menu()
for D in (ES, FR, PT):
    l = D["lang"]
    assert shape(D["body"]) == shape(EN["body"]), f"[{l}] structure differs from English"
    html_, nq = page(D, links, names)
    bad = re.findall(r"[가-힣]", html_)
    assert not bad, f"[{l}] Korean characters left: {''.join(bad[:20])}"
    out = os.path.join(SITE, l, "intro"); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(html_)
    print(f"[{l}] sections: {sum(1 for b in D['body'] if b[0] == 'h')}, quotations: {nq} (all checked word for word) → {l}/intro/index.html")
