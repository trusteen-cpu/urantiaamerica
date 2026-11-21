# -*- coding: utf-8 -*-
import json, os
from save import save, OUT, H
cur = json.load(open(OUT, encoding="utf-8"))
fix = {}
for k, v in cur.items():
    if isinstance(v, str):
        n = v.replace("Epílogo final", "Posfacio").replace("epílogo final", "posfacio")
        n = n.replace("En su Prólogo, Sadler", "En su prefacio, Sadler")
        if n != v:
            fix[k] = n
print(sorted(fix))
save(fix)

Q = {
"w06.081": "Y parecería también que el no condicionado también sería sin límites, por lo menos desde un punto de vista cualitativo, aunque no estamos igualmente seguros en cuanto a las relaciones cuantitativas.",
"w06.108": "Probablemente sería tan sólo una distorsión mínima de la verdad si se concibiese al tercer miembro de la Trinidad de Trinidades como el Absoluto Universal …",
"w06.135": "… y de este modo están ambos destinados a la futura superpersonalidad eterna del ministerio trascendental de los dominios absonitos del Último, el Supremo-Último, y aun en los niveles del Último-Absoluto.",
"w06.142": "Existencialmente las Deidades del Paraíso logran este nivel mediante la Trinidad, pero este tercer nivel de la expresión de la Deidad unificadora no está plenamente unificado experiencialmente.",
"w06.150": "La improbabilidad del alcance del destino infinito no previene en lo más mínimo el surgimiento de ideas sobre dicho destino …",
"w06.154": "La infinidad está colmada por el Infinito; el Infinito envuelve la infinidad. Éste es un momento hipotético estático de la eternidad …",
"w07.050": "Éste es un momento hipotético estático de la eternidad; los actuales aún están contenidos dentro de sus potenciales, y los potenciales aún no han aparecido dentro de la infinidad del YO SOY. Pero aun en esta situación conjetural debemos suponer la existencia de la posibilidad de la autovoluntad.",
}
todo = json.load(open(os.path.join(H, "work", "todo_es_c04.json"), encoding="utf-8"))
assert set(Q) == set(todo)
json.dump({k: Q[k] for k in todo}, open(os.path.join(H, "es", "quotes_c04.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes", len(Q))
