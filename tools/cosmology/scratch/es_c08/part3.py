import json, os
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(H, "es", "c08.json")
D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
U = {
"w14.117": "El crecimiento del Cosmos Infinito",
"w14.118": "Apéndice XXVII, El crecimiento del Cosmos Infinito (pp. 508–519)",
"w14.119": "En su último apéndice Sadler pone a prueba hasta dónde pueden llevarnos los conceptos en el Cosmos Infinito. La trinidización de Dios el Absoluto, sugiere, hará surgir de repente una «cabeza de playa en las costas de la infinidad»: la zona interior del Cosmos Infinito. Divide el Cosmos Infinito en zonas interior, intermedia y exterior, y las empareja con tres edades posuniversales y tres Deidades Duales. También reconstruye los siete niveles de función de la Deidad Total como niveles existencial-experienciales.",
"w14.120": "1. Ecos de la trinidización Supremo-Última (orig., pp. 508–509)",
"w14.121": "El Supremo y el Último expresan todo el potencial finito y absonito del universo maestro, y como Supremo-Último lo resumen. Sadler ve su trinidización de Dios el Absoluto como la proyección de esa suma más allá del universo maestro, y la llama una «cabeza de playa en las costas de la infinidad». Puede que no sea una mera figura retórica, dice, sino un acontecimiento literal, del mismo modo que Havona fue eternizado junto con la aparición del Espíritu Infinito.",
"w14.123": "Sadler sospecha que el Cosmos Infinito, en su zona interior, se cristalizará igualmente de una sola vez, sin pasar por etapas. Una porción de la infinidad que poseen los tres Absolutos de potencialidad sería materializada, mentalizada y espiritualizada: se haría experiencial.",
"w14.124": "Dos eternidades",
"w14.125": "De esta comparación Sadler extrae la idea de dos eternidades. Con la trinidización existencial se estableció un ciclo de eternidad [8:1.3]: la primera edad, sin comienzo, la edad de Havona. La trinidización Supremo-Última puede abrir otro ciclo, una eternidad existencial-experiencial: la edad final, sin fin, la edad del Cosmos Infinito. Los dos albores se parecen notablemente. En el primer albor estaban el Padre y el Hijo, dos Deidades existenciales, junto con una base nuclear existencial, la Isla del Paraíso. En el segundo albor están el Supremo y el Último, dos Deidades experienciales, junto con una base nuclear experiencial, el universo maestro completado.",
"w14.126": "2. Un marco para pensar el Cosmos Infinito (orig., pp. 510–511)",
"w14.127": "Al pensar en la infinidad, uno se pierde fácilmente en una serie sin fin. Por eso Sadler elige el esquema más sencillo que puede: un marco conceptual de tres zonas.",
"w14.128": "**La zona interior.** Aparece de una sola vez con la trinidización de Dios el Absoluto. Es lo bastante grande como para empequeñecer al universo maestro, quizá en la misma proporción en que el universo maestro está con respecto al gran universo. Sadler insiste en que esta es la última estimación razonable de tamaño que alguien puede hacer. Se empareja con la actividad del Supremo-Último.",
"w14.129": "**La zona o zonas intermedias.** Son las etapas sucesivas del desarrollo del Cosmos Infinito. Como se suceden una tras otra, sus límites no pueden fijarse, y puede que no tengan fin. Se emparejan con la actividad del Último-Absoluto.",
"w14.130": "**La zona o zonas exteriores.** Son zonas conceptuales que el Cosmos Infinito en expansión quizá nunca alcance realmente. Se emparejan con la función de la última Deidad Dual, el Absoluto y Padre-Infinito.",
"w14.131": "Sadler reconoce que la única zona relativamente segura es la interior, que puede aparecer de una vez y completa. Las zonas exteriores, que se amplían en secuencia, pueden continuar sin fin en la eternidad.",
"w14.132": "Las seis asociaciones de Deidad Dual (106:8.12) y las tres zonas del Cosmos Infinito; el emparejamiento de zonas y edades es el marco conceptual de Sadler",
"w14.133": "3. Reelaboración de los niveles de función de la Deidad Total (orig., pp. 511–516)",
"w14.134": "El Prólogo de *El libro de Urantia* enumera siete niveles en los que funciona la Deidad Total, desde los niveles estático y potencial, pasando por el asociativo, el creador y el evolutivo, hasta el supremo y el último [0:1.3–1.10]. El nivel absoluto falta en esa lista. Poco después, sin embargo, el texto habla por separado del nivel absoluto.",
"w14.136": "Sobre esta base Sadler sostiene que existen niveles postúltimos más allá de los siete. En un momento consideró un esquema de diez niveles, añadiendo tres imágenes especulares de los tres primeros niveles, pero lo dejó de lado. Recordó cómo, en el Apéndice VI, aplicar medidas experienciales a Havona no había producido más que paradojas, y concluyó que en las edades postúltimas actuaría un nuevo mecanismo existencial-experiencial. Una vez completo el universo maestro, cesa el nivel creador, el nivel evolutivo llega a su fin una vez que han emergido las dos Deidades experienciales, y los niveles de supremacía y ultimidad quedan en reposo. Nuevos niveles ocupan su lugar.",
"w14.137": "Siete niveles para la edad postúltima propuestos por Sadler",
"w14.138": ["Nivel", "Carácter", "Explicación de Sadler"],
"w14.139": ["1 Nivel estático", "Existencial (sin cambio)", "Deidad autocontenida y autoexistente"],
"w14.140": ["2 Nivel potencial", "Existencial (sin cambio)", "Depósito de lo que la Deidad ha querido pero aún no ha actualizado"],
"w14.141": ["3 Nivel asociativo", "Existencial (sin cambio)", "Primera agrupación de personas y Deidades: la Trinidad del Paraíso"],
"w14.142": ["4 Nivel coabsoluto", "Nivel nuevo", "Nivel postúltimo en el que funcionan los coabsolutos"],
"w14.143": ["5 Nivel reasociativo", "Espejo del 3", "Toda la Deidad existencial y experiencial reunida de nuevo en la Trinidad de Trinidades"],
"w14.144": ["6 Nivel de potencial actualizador", "Espejo del 2", "Los potenciales absolutos se vuelven actuales directamente, sin etapas de maduración"],
"w14.145": ["7 Nivel estático-dinámico", "Espejo del 1", "La dinámica del crecimiento experiencial penetra lo estático"],
"w14.146": "En el quinto nivel Sadler contrasta la asociación con la reasociación. En el nivel asociativo la Deidad existencial se hizo una en la Trinidad del Paraíso. En el nivel reasociativo la Deidad existencial y la experiencial se unen de nuevo dentro de la Trinidad de Trinidades. La entrada en el sexto nivel requiere dos condiciones: el potencial de crecimiento de lo finito y lo absonito debe agotarse por completo, y la Deidad y la trinidad experienciales deben abrirse paso hasta el nivel absoluto y tocar directamente a los Absolutos potenciales.",
"w14.147": "El nombre del séptimo nivel, estático-dinámico, suena extraño, pero Sadler señala que la revelación emplea este mismo término al describir al Absoluto Universal [0:11.14]. Este nivel puede penetrarse, pero nunca agotarse. Si el crecimiento llegara a consumir todo potencial, el nivel volvería a ser estático, pero la revelación dice que eso nunca sucederá.",
"w14.149": "No tener fin, añade Sadler, no significa no tener comienzo ni continuación. Las secciones sobre los niveles sexto y séptimo llevan en el original una nota del autor que indica que sus conceptos quedaron incompletos.",
"w14.150": "4. Las últimas asociaciones de Deidad Dual (orig., pp. 516–518)",
"w14.151": "En todo el universo maestro Sadler se ha apoyado en un principio: la Deidad Dual abre el camino y la trinidad consolida. Si ese principio vale también en el Cosmos Infinito, las asociaciones de Deidad Dual se pondrán a trabajar antes que la Trinidad de Trinidades. La revelación expone todo el linaje de estas asociaciones en una sola frase.",
"w14.153": "Sadler divide estas seis asociaciones en dos grupos. Las tres primeras (Padre-Hijo, Hijo-Espíritu, Espíritu-Supremo) inician, desarrollan y completan el universo maestro, incluida Havona. Las tres últimas (Supremo-Último, Último-Absoluto, y Absoluto y Padre-Infinito) trabajan más allá del universo maestro. Luego invierte el método del Apéndice VI, donde retrocedió tres veces por detrás de la primera edad, empezando por la Edad Cero, y divide el tiempo posterior al universo maestro en tres edades.",
"w14.154": "Tres edades posuniversales (concepto de Sadler)",
"w14.155": ["Edad", "Deidad Dual", "Zona del Cosmos Infinito", "Fundamento y analogía"],
"w14.156": ["Primera edad posuniversal", "Supremo-Último", "Zona interior", "El Padre y el Hijo reconocen su unidad y entran en una asociación eterna [8:0.2]"],
"w14.157": ["Segunda edad posuniversal", "Último-Absoluto", "Zona o zonas intermedias", "La relación del Espíritu con el Hijo en la creación posterior [8:3.3]"],
"w14.158": ["Tercera edad posuniversal", "Absoluto y Padre-Infinito", "Zona o zonas exteriores", "«⟦Q 106:8.12⟧completándose así el ciclo de la realidad⟦/Q⟧» [106:8.12]"],
"w14.159": "Para la segunda edad Sadler añade una esperanza. Si los Ajustadores Personalizados están destinados a ministrar incluso en los niveles del Último-Absoluto [109:7.5], los finalistas también estarán allí, puesto que el potencial eterno de la dotación personal de un finalista se parece a la actualidad que un Ajustador Personalizado ya posee. En cuanto a la relación que Dios el Absoluto tendrá con el Padre Infinito en la tercera edad, Sadler dice que solo puede conjeturarse.",
"w14.160": "Los cuatro apéndices no escritos",
"w14.161": "La tabla de apéndices del original enumera otros cuatro apéndices que tienen título pero no texto: XXVIII, La naturaleza del Absoluto de Deidad; XXIX, La naturaleza del Absoluto No Cualificado; XXX, La naturaleza del Absoluto Universal; y XXXI, El concepto del Infinito. Sadler nunca llegó a escribirlos, y por eso este comentario también termina aquí. Sin embargo, los apéndices anteriores ya apuntan en su dirección. Dios el Absoluto crece sin fin, el Absoluto Universal y el Absoluto No Cualificado nunca pueden agotarse, y todo tiende finalmente a experimentar al YO SOY como el Padre-Infinito. Los apéndices no escritos muestran que Sadler dejó su estudio como una pregunta abierta e inconclusa.",
"w14.162": "Sadler espera que la trinidización de Dios el Absoluto haga surgir de repente una «cabeza de playa en las costas de la infinidad», la zona interior del Cosmos Infinito.",
"w14.163": "El Cosmos Infinito puede representarse como zonas interior, intermedia y exterior; solo la zona interior es relativamente segura.",
"w14.164": "Los siete niveles de *El libro de Urantia* omiten el nivel absoluto. Para la edad postúltima Sadler propone un nuevo conjunto de siete que incluye los niveles coabsoluto, reasociativo, de potencial actualizador y estático-dinámico.",
"w14.165": "Como la estática en el crecimiento nunca aparece en el cosmos total, el nivel estático-dinámico se penetra sin fin, pero nunca se agota.",
"w14.166": "De las seis asociaciones de 106:8.12, las tres primeras trabajan dentro del universo maestro y las tres últimas trabajan en el Cosmos Infinito durante tres edades posuniversales.",
"w14.167": "El original contiene secciones inconclusas y cuatro apéndices no escritos. El estudio de Sadler termina como una pregunta abierta.",
}
D.update(U)
# reorder per source, normalize quotes
S = json.load(open(os.path.join(H, "work", "src_c08.json"), encoding="utf-8"))
def fix(s): return s.replace("“", "«").replace("”", "»")
O = {}
for k in S:
    if k in D:
        v = D[k]
        O[k] = [fix(x) for x in v] if isinstance(v, list) else fix(v)
missing = [k for k in S if k not in O]
json.dump(O, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(O), "missing", missing)

Q = {
"w14.025": "el Padre no es discerniblemente absoluto como Deidad total, salvo en la Trinidad del Paraíso.",
"w14.052": "La primera y la segunda Trinidad experiencial, las Trinidades post-Havona, no pueden ser infinitas porque comprenden Deidades derivadas,",
"w14.067": "no estamos seguros en cuanto al envolvimiento de todos los valores absolutos, puesto que no se nos ha informado en ningún momento de que el Absoluto Cualificado sea equivalente al Infinito.",
"w14.069": "Dios el Absoluto es la meta del logro-realización de todos los seres superabsonitos,",
"w14.090": "Como la personalidad absoluta y no cualificada, el Padre puede funcionar solamente como el Hijo y con el Hijo, pero como Padre personal continúa otorgando personalidad a las diversas huestes de los diferentes niveles de criaturas volitivas inteligentes,",
"w14.094": "algunos de nosotros postulan que la creación de estos mensajeros por parte del Espíritu Infinito está en cierto modo relacionada con la dotación por parte del Actor Conjunto de la Mente Suprema-Última.",
"w14.099": "Pero cuando un finalista y un habitante del Paraíso-Havona juntos trinidizan una nueva criatura, este esfuerzo conjunto repercute en ciertas faces de la Mente Suprema-Última. Los hijos trinidizados por criaturas resultantes son supercreacionales;",
"w14.109": "y de este modo están ambos destinados a la futura superpersonalidad eterna del ministerio trascendental de los dominios absonitos del Último, el Supremo-Último, y aun en los niveles del Último-Absoluto.",
"w14.135": "Existencialmente las Deidades del Paraíso logran este nivel mediante la Trinidad, pero este tercer nivel de la expresión de la Deidad unificadora no está plenamente unificado experiencialmente.",
}
Q = {k: (("… " if k in ("w14.025", "w14.067", "w14.094", "w14.109") else "") + (v[:-1] + " …" if v[-1] in ",;" else v)) for k, v in Q.items()}
json.dump(Q, open(os.path.join(H, "es", "quotes_c08.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
