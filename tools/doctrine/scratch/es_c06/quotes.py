import json
V = json.load(open('../data/es.json', encoding='utf-8'))
todo = json.load(open('work/todo_es_c06.json', encoding='utf-8'))

# key: (verse, start, end-inclusive-marker)
S = {
 "ch28:12": ("5:3.3", "La adoración es por su propio", "en el culto verdadero"),
 "ch28:32": ("5:3.8", "La experiencia de la adoración", "del alma humana"),
 "ch29:1": ("144:2.3", "La oración es el aliento", "la voluntad del Padre."),
 "ch29:8": ("91:8.11", "Dios responde a la oración", "de la experiencia humana"),
 "ch29:18": ("91:3.7", "para que el hombre pueda hablar", "el Padre Universal."),
 "ch29:27": ("144:2.5", "Vuestra perseverancia no es", "para recibir el espíritu."),
 "ch29:51": ("168:4.13", "Todas las solicitudes", "del tiempo y del espacio"),
 "ch29:56": ("91:6.7", "No existe ninguna otra técnica", "comunicarse con su Hacedor"),
 "ch30:15": ("148:5.3", "Pero puedes estar seguro", "de la iniquidad son inexorables."),
 "ch30:29": ("152:0.3", "Era su fe y no su toque", "la carrera terrenal de Jesús"),
 "ch30:35": ("148:2.2", "se nos informó que", "destruye la ansiedad."),
 "ch30:37": ("147:3.5", "su sensación de inutilidad", "salir caminando."),
 "ch30:41": ("164:3.15", "deseaba enseñar a sus seguidores", "eran los milagros."),
 "ch30:48": ("147:3.3", "Si pudierais todos vosotros", "todas las dolencias morales."),
 "ch31:8": ("194:4.6", "Cometieron el gran error", "haya conocido jamás."),
 "ch31:10": ("196:2.1", "En el entusiasmo de Pentecostés", "del camino a Damasco."),
 "ch31:39": ("195:10.12", "Pero el cristianismo, aun en el siglo veinte", "en pos del bien en la tierra"),
 "ch32:7": ("92:4.8", "Cristo Micael presentó", "era amor y servicio"),
 "ch32:26": ("196:2.4", "El cristianismo de Pablo", "hasta hacerse uno con la divinidad"),
 "ch32:32": ("104:1.13", "Pero aunque el concepto cristiano", "las interrelaciones espirituales."),
 "ch32:38": ("170:5.19", "Tarde o temprano surgirá", "en el corazón del creyente"),
 "ch32:42": ("170:5.21", "pero debéis comprender que esta iglesia", "oportunidad más plena para su desarrollo."),
 "ch33:2": ("1:0.3", "Las criaturas volitivas", "reconocer al Padre Universal."),
}
out = {}
for k in todo:
    v, a, b = S[k]
    t = V[v]
    i = t.index(a)
    j = t.index(b, i) + len(b)
    out[k] = t[i:j]
assert set(out) == set(todo) and len(out) == len(todo)
json.dump(out, open('es/quotes_c06.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out))
