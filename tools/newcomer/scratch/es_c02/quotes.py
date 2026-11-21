import json, os
B = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
T = json.load(open(B + r"\work\todo_es_c02.json", encoding="utf-8"))
# key -> list of (start, end) substrings; piece = verse[start .. end inclusive]
P = {
 "w05:91": [("Durante la larga lucha para alcanzar al Padre", "ha visto al Padre.")],
 "w05:109": [("Así se emitió y publicó", "mundos del espacio.")],
 "w05:173": [("En todo mortal existe", "difícilmente pueden reconciliarse plenamente")],
 "w06:58": [("el reensamblaje real y consciente", "mañanas de resurrección.")],
 "w06:120": [("el mundo de estancia número uno es una esfera", "siete mundos progresivos.")],
 "w06:128": [("Un verdadero nacimiento", "horizontes en expansión."), ("El estudio se está volviendo", "está evolucionando.")],
 "w06:180": [("Aquellas cosas que podrías", "antes de proceder a la siguiente")],
 "w06:220": [("A través de esta magnífica ascensión", "separar al hombre y al Ajustador")],
 "w07:73": [("En ese momento el Avonal autootorgador", "al mundo de autootorgamiento."), ("concomitantemente con esto", "de elección espiritual.")],
 "w07:89": [("El Hijo autootorgador es el Príncipe de la Paz.", "el Príncipe de la Paz."), ("Pero estas influencias saludables", "de la procesión planetaria.")],
 "w07:124": [("Es muy difícil señalar", "si no del universo entero."), ("Durante mucho tiempo se le ofreció", "la misericordia ofrecida.")],
 "w07:158": [("Los mortales ascendentes eran vulnerables", "los espíritus más bajos."), ("está registrado para gloria", "la rebelión de Lucifer.")],
 "w07:233": [("El valor relativo del período", "simultáneo al acto.")],
 "w07:245": [("Pero debemos aclarar una cosa:", "Pero debemos aclarar una cosa:"), ("puedes estar seguro de la certidumbre", "al logro de Dios.")],
 "w08:142": [("Imaginaos nuestro regocijo", "con la del gemelo."), ("cuando, al año, resolvieron", "reconocidas como humanas.")],
 "w08:249": [("No comprendí por aquel entonces", "orgullo de la personalidad.")],
 "w08:253": [("La presentación de esta sorprendente exigencia", "el Soberano del Sistema de Satania")],
 "w09:25": [("El sitio elegido", "el clima entonces era ideal."), ("En este lugar de reunión", "único punto risueño en Urantia")],
 "w09:33": [("ARRIBARON Adán y Eva", "hace 37.848 años."), ("Siempre los Hijos e Hijas Materiales", "rara vez funcionan solos.")],
 "w09:74": [("los Melquisedek, antes de partir", "sus empresas mutuas.")],
 "w09:110": [("No ha habido ninguna", "su previa condición biológica.")],
 "w09:173": [("El matrimonio que culmina", "pero es esencialmente humana")],
 "w09:222": [("pero durante todo este tiempo existía", "sus primeras manifestaciones.")],
 "w09:262": [("Dios responde a la oración", "de la experiencia humana")],
 "w09:284": [("1.973 años antes", "presenciada por ojos humanos."), ("«Soy Melquisedek", "el único Dios».")],
 "w09:300": [("Aunque no se permitían sacrificios", "sacrificio de carne y sangre.")],
}
out = {}
for k, v in T.items():
    verse = v["verse"]
    parts = []
    pos = 0
    for s, e in P[k]:
        i = verse.index(s, pos)
        j = verse.index(e, i) + len(e)
        parts.append(verse[i:j])
        pos = j
    out[k] = " \u2026 ".join(parts)
    print(k, "|", out[k][:90], "...", out[k][-60:])
assert set(out) == set(T)
json.dump(out, open(B + r"\es\quotes_c02.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
