import json, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
Q = {
 "w04.046": "…donde ya podemos identificar la acumulación de por lo menos setenta mil agregaciones de materia, cada una de las cuales es más grande que cualquiera de los superuniversos actuales.",
 "w04.107": "En otras palabras: en este momento, alrededor del noventa y cinco por ciento de la acción de la gravedad cósmica activa de la Isla del Paraíso, computada sobre la base de esta teoría de totalidad, está dedicada a controlar sistemas materiales mas allá de las fronteras de los actuales universos organizados.",
 "w04.134": "…consideramos que el universo maestro tiene limitaciones, siendo definitivamente delimitado y contenido en sus fronteras exteriores por el espacio abierto.",
 "w05.040": "…el destino se consume probablemente por la acción del Consumador del Destino Universal, y este acto tiene probablemente que ver con el Supremo y el Último en la Trinidad Absoluta.",
 "w05.042": "La Trinidad Última, presentemente en evolución, finalmente consistirá en el Ser Supremo, las Personalidades Supremas Creadoras y los Arquitectos absonitos del Universo Maestro…",
 "w05.045": "Sin embargo, de lo siguiente estamos seguros: aunque la existencial Trinidad del Paraíso es infinita, y aunque la experiencial Trinidad Última es subinfinita, la Trinidad Absoluta no es tan fácil de clasificar.",
 "w05.086": "De todos aquellos que ascienden a la Isla eterna, sólo los que llegan de este modo son hijos de la eternidad…",
 "w05.099": "…pero según el hombre asciende, según progresa hacia adentro, la visión en aumento de esta procesión de acontecimientos es tal que cada vez más se la discierne en su totalidad.",
 "w05.115": "Y parecería también que el no condicionado también sería sin límites, por lo menos desde un punto de vista cualitativo, aunque no estamos igualmente seguros en cuanto a las relaciones cuantitativas.",
 "w05.120": "Si suponemos un cosmos infinito —un cosmos ilimitable más allá del universo maestro— y si concebimos que los desarrollos finales de la Trinidad Absoluta tomarán lugar allí afuera en tal escenario superúltimo de acción, …",
 "w05.164": "Estas tres Deidades experienciales eran potenciales en la Trinidad existencial, la Trinidad del Paraíso, pero su aparición en el universo como personalidades de poder depende en parte de su propio funcionamiento experiencial en los universos de poder y personalidad…",
 "w05.166": "…tal como se ilustra por la síntesis de poder-personalidad que en estos momentos se está produciendo en relación con la evolución del Ser Supremo.",
 "w05.175": "En este nivel supercreativo, la Deidad experimenta el agotamiento del potencial personalizable, encuentra el cumplimiento de la divinidad…",
 "w05.179": "La Trinidad Última se está unificando experiencialmente en cumplimiento, pero verdaderamente dudamos de la posibilidad de dicha unificación plena de la Trinidad Absoluta. Nuestro concepto, sin embargo, de la Trinidad eterna del Paraíso es un recuerdo constantemente presente de que la trinidización de Deidad puede lograr lo que es de otra manera inalcanzable…",
}
todo = json.load(open(os.path.join(H, "work", "todo_es_c03.json"), encoding="utf-8"))
assert set(todo) == set(Q), set(todo) ^ set(Q)
json.dump({k: Q[k] for k in todo}, open(os.path.join(H, "es", "quotes_c03.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(Q))
