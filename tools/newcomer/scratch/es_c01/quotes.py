import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
todo = json.load(open(os.path.join(ROOT, "work", "todo_es_c01.json"), encoding="utf-8"))

# key -> list of (start, end) substrings; each piece = verse[start .. end inclusive]
CUTS = {
"w01:174": [("5. Los documentos de Urantia.", "hacer estas declaraciones francas")],
"w01:239": [("para cada uno de vosotros y para todos nosotros", "el camino está abierto")],
"w02:33": [("No permitáis que la magnitud", "la cumbre de la personalidad divina")],
"w02:57": [("primero, en las personalidades de los Hijos", "uno con vosotros"),
           ("Y segundo, existen", "enviados sin anuncio ni explicación.")],
"w02:78": [("La capacidad del Padre Universal", "al mismo tiempo.")],
"w02:90": [("Y debería ser consuelo", "se lo pidáis».")],
"w02:100": [("La omnipotencia no implica", "lo que no puede conocerse.")],
"w02:160": [("Al ponderar sobre la naturaleza", "para con su padre terrenal")],
"w02:200": [("Dios ama al pecador porque", "(potencialmente eterna)"),
            ("El amor de Dios salva al pecador", "destruye el pecado.")],
"w02:223": [("es verdad que «las cosas invisibles", "las cosas hechas»")],
"w02:245": [("En la ciencia, Dios es la Primera Causa", "el único ser que existe por sí mismo"),
            ("Pero hace falta la revelación", "sus hijos en la tierra.")],
"w02:323": [("Dios concede elección soberana", "del Dios de libre albedrío.")],
"w02:335": [("aunque yo no pueda hacer esto", "aun vuestra fe».")],
"w03:52": [("Y así como el fragmento espiritual", "tu avance espiritual.")],
"w03:74": [("Los Hijos divinos son ciertamente", "a través del Espíritu Infinito")],
"w03:78": [("en la administración de los universos están", "no siempre es posible distinguirlos."),
           ("recordad simplemente que Dios", "el verbo expresivo.")],
"w03:82": [("La Trinidad del Paraíso es real.", "el Hijo y el Espíritu"),
           ("El Padre, el Hijo, y el Espíritu pueden colaborar", "ésa no es la Trinidad.")],
"w03:135": [("La Deidad puede causar", "el Paraíso no es Deidad")],
"w03:148": [("Esta es la única colección", "los Hijos Creadores de Dios")],
"w03:160": [("aunque su velocidad es enorme", "una vigilia en la noche».")],
"w03:199": [("Havona es el objetivo preparadisiaco", "los mortales ascendentes."),
            ("Havona se alza ante todas", "el campo deportivo de los finalistas")],
"w03:266": [("La personalidad también responde a la gravedad: al circuito exclusivo del Padre", "al circuito exclusivo del Padre"),
            ("el Padre Universal es infinito y actúa", "la Isla del Paraíso.")],
"w03:286": [("El circuito de gravedad espiritual es el canal", "las personalidades divinas competentes")],
"w03:304": [("Aquí, Dios está personal", "para todos los universos.")],
"w04:104": [("como Padre de un universo local", "personalidad de maestro del Espíritu Infinito.")],
"w04:152": [("Los ángeles son los asociados", "altamente individualizadas."),
            ("poseen naturalezas muy sociables", "la de los seres humanos.")],
"w04:170": [("son los supernafines, seconafines y serafines quienes", "a través del Hijo Eterno.")],
"w04:209": [("La narrativa siguiente presenta", "morado por un Ajustador."),
            ("hemos elegido contar esta historia", "todas las razas humanas de Urantia.")],
}
Q = {}
for k, v in todo.items():
    verse = v["verse"]
    pieces = []
    pos = 0
    for s, e in CUTS[k]:
        i = verse.find(s, pos)
        assert i >= 0, (k, s)
        j = verse.find(e, i)
        assert j >= 0, (k, e)
        pieces.append(verse[i:j + len(e)])
        pos = j + len(e)
    Q[k] = " … ".join(pieces)
missing = [k for k in todo if k not in Q]
assert not missing, missing
json.dump(Q, open(os.path.join(ROOT, "es", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes", len(Q))
