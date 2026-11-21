# -*- coding: utf-8 -*-
import json
R = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools"

def a(y):  # A.D.
    return f"{y} d. de J.C."

def b(y):  # B.C.
    return f"{y} a. de J.C."

M = {
 "ui": {
  "site_title": "Mapas de El libro de Urantia",
  "og_desc": "38 mapas que siguen la vida de Jesús, desde su nacimiento hasta las apariciones morontiales",
  "sub": "Desde el nacimiento de Jesús hasta las apariciones morontiales — 38 mapas que siguen sus pasos",
  "search_ph": "Buscar títulos, lugares, años",
  "choose": "Elegir un mapa",
  "prev": "Mapa anterior",
  "next": "Mapa siguiente",
  "full": "Tamaño completo",
  "print": "Imprimir",
  "map": "Mapa",
  "sketch": "croquis de ubicación",
  "note": "Los nombres de lugares, las fechas y las rutas se tomaron del texto de El libro de Urantia, con su propia ortografía. Las rutas que el texto no describe aparecen punteadas, y las zonas pequeñas, como el interior de Jerusalén, se muestran como croquis de ubicación. La ubicación de las poblaciones es aproximada; el relieve de base procede de Natural Earth (costas y lagos actuales, de dominio público).",
  "note_labels": "Los rótulos de los mapas están en inglés, con la ortografía del texto inglés de El libro de Urantia (The Urantia Book)."
 },
 "maps": [
  ["El nacimiento de Jesús y la huida a Egipto", f"Agosto del año {b(7)} – octubre del año {b(4)}"],
  ["Nazaret y sus alrededores durante la infancia", f"{b(3)} – {a(8)}"],
  ["Poblaciones de Galilea visitadas con su padre", f"{b(1)} – {a(5)}"],
  ["El primer viaje a Jerusalén", f"4–7 de abril del año {a(7)}"],
  ["Jerusalén y el templo", f"Abril del año {a(7)}, su primera Pascua"],
  ["La antigua Nazaret y el hogar de Jesús", f"{b(4)} – hacia el año {a(28)}"],
  ["La Pascua con Santiago", f"Primavera del año {a(12)}"],
  ["La tercera visita a Jerusalén para la Pascua", f"Primavera del año {a(14)}"],
  ["La cuarta visita a Jerusalén para la Pascua — con su hermano José", f"Primavera del año {a(15)}"],
  ["La quinta visita a Jerusalén para la Pascua — con su hermano Simón", f"Primavera del año {a(17)}"],
  ["La sexta visita a Jerusalén para la Pascua — con su hermano Judá", f"Primavera del año {a(19)}"],
  ["El taller de barcas de Zebedeo y Jerusalén", f"Enero del año {a(21)} – abril del año {a(22)}"],
  ["El viaje a Roma, Grecia y Mesopotamia", f"Abril del año {a(22)} – diciembre del año {a(23)}"],
  ["El Lago Urmia y el viaje con la caravana al Mar Caspio", f"Abril del año {a(24)} – abril del año {a(25)}"],
  ["Siria y la costa del Mediterráneo", f"Abril – verano del año {a(25)}"],
  ["A través de Palestina hasta el Monte Hermón", f"Verano del año {a(25)}"],
  ["Del Monte Hermón a Jerusalén, y de regreso a Galilea", f"Finales del verano del año {a(25)} – enero del año {a(26)}"],
  ["El bautismo cerca de Pella y los cuarenta días en las colinas de Perea", f"13 de enero – 23 de febrero del año {a(26)}"],
  ["De Pella, pasando por Nazaret, a Caná y Betsaida", f"24 de febrero – 2 de marzo del año {a(26)}"],
  ["La elección y la ordenación de los apóstoles — Betsaida y el mar de Galilea", f"Febrero del año {a(26)} – enero del año {a(27)}"],
  ["Por el valle del Jordán hasta Judea", f"Enero – abril del año {a(27)}"],
  ["La primera labor con los apóstoles — Judea, Samaria y la Decápolis", f"Abril del año {a(27)} – enero del año {a(28)}"],
  ["La primera gira de predicación pública por Galilea", f"Enero – marzo del año {a(28)}"],
  ["El viaje de la Pascua a Jerusalén", f"Marzo – mayo del año {a(28)}"],
  ["El campamento de Zebedeo y la segunda gira de predicación por Galilea", f"Mayo – diciembre del año {a(28)}"],
  ["La tercera gira de predicación y la visita a Nazaret", f"Enero – marzo del año {a(29)}"],
  ["La subida a Jerusalén, y luego hacia el norte", f"Marzo – junio del año {a(29)}"],
  ["De Sidón a lo largo de la costa, y al parque de Magadán", f"Junio – agosto del año {a(29)}"],
  ["La transfiguración en el Monte Hermón y la gira por la Decápolis", f"Agosto – septiembre del año {a(29)}"],
  ["El cuartel general se traslada a Pella, y las visitas a Jerusalén", f"Septiembre – diciembre del año {a(29)}"],
  ["La gira por Perea, y a Betania para resucitar a Lázaro", f"Enero – marzo del año {a(30)}"],
  ["Del campamento de Pella a Jerusalén", f"Marzo – 2 de abril del año {a(30)}"],
  ["De Betania al templo y al campamento de Getsemaní", f"3–5 de abril del año {a(30)}"],
  ["El campamento de Getsemaní y el aposento superior", f"Jueves 6 de abril del año {a(30)}"],
  ["Del arresto en Getsemaní al juicio ante Pilato", f"Noche del 6 de abril – mañana del 7 de abril del año {a(30)}"],
  ["Del pretorio al Gólgota", f"Viernes 7 de abril del año {a(30)}"],
  ["El domingo de la resurrección: apariciones en Jerusalén y Betania", f"Domingo 9 de abril del año {a(30)}"],
  ["Las apariciones morontiales, de la décima a la decimonovena", f"11 de abril – 18 de mayo del año {a(30)}"],
 ]
}
assert len(M["maps"]) == 38
json.dump(M, open(R + r"\maps\strings_es.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

BOOK = "El libro de Urantia"
RD = {
 "index": {
  "title": f"Lectura de {BOOK} en un año",
  "sub": "Desde el Prólogo hasta el Documento 196, en orden — marque lo que ha leído y se registrará la fecha",
  "start": "Fecha de inicio",
  "goal": "Meta",
  "g260": "1 año · 5 días por semana (260 días)",
  "g365": "1 año · todos los días (365 días)",
  "g182": "6 meses (182 días)",
  "next": "Ir a la siguiente lectura ▶",
  "c1": "Completado",
  "c2": "Secciones leídas",
  "c4": "Días restantes",
  "ahead": "Adelantado al plan",
  "behind": "Atrasado respecto al plan",
  "onpace": "Al día con el plan",
  "notyet": "Sin comenzar",
  "fore": "Prólogo",
  "parts": ["Prólogo", "Parte I", "Parte II", "Parte III", "Parte IV"],
  "intro": "Introducción",
  "quotes": "Pasajes memorables",
  "qph": "Escriba el pasaje",
  "add": "Añadir",
  "memo": "Notas",
  "mph": "Escriba sus reflexiones sobre este documento",
  "saved": "Guardado",
  "dbtn": f"📔 Diario de {BOOK}",
  "graph": "Progreso",
  "l1": "Mi progreso",
  "l2": "Meta (plan)",
  "export": "Exportar (guardar en un archivo)",
  "import": "Importar",
  "reset": "Borrar todo",
  "store": "Su registro se guarda en este navegador, en este dispositivo. Expórtelo a un archivo de vez en cuando para trasladarlo o conservarlo a salvo.",
  "resetQ": "¿Borrar todas las marcas, pasajes y notas? Esta acción no se puede deshacer.",
  "editDate": "Fecha de lectura (p. ej., 2026-10-30). Déjela vacía para desmarcar.",
  "st_ahead1": "Va {d} día adelantado respecto al plan.",
  "st_ahead": "Va {d} días adelantado respecto al plan.",
  "st_behind1": "Va {d} día atrasado. Si lee hoy hasta el {p}%, se pondrá al día.",
  "st_behind": "Va {d} días atrasado. Si lee hoy hasta el {p}%, se pondrá al día.",
  "st_on": "Va al día con el plan.",
  "day1": "{n} día",
  "days": "{n} días",
  "today_graph": "hoy"
 },
 "diary": {
  "title": f"📔 Diario de {BOOK}",
  "prev": "◀ Día anterior",
  "next": "Día siguiente ▶",
  "today": "Hoy",
  "verse": "✦ Pasaje del día",
  "other": "Otro pasaje ↻",
  "think": "✎ Acontecimientos y reflexiones de hoy",
  "ph": "Escriba sobre lo que sucedió en su día",
  "saved": "Guardado",
  "past": "Entradas anteriores",
  "hint": f"Su diario se guarda en este navegador. Se incluye en el archivo de exportación de la página de Lectura de {BOOK} en un año."
 }
}
json.dump(RD, open(R + r"\reading\strings_es.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
