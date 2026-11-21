import json, sys, os
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
todo = json.load(open(os.path.join(ROOT, "work", "todo_es_c03.json"), encoding="utf-8"))

# key: list of (verse, start, end)
P = {
 "w10:37": [("101:8.1", "La creencia llega", "es meramente creencia")],
 "w10:51": [("99:5.7", "Algún día los religionistas", "unificar a los religiosos.")],
 "w10:61": [("99:6.2", "Existe un propósito", "la belleza y la bondad;"),
            ("99:6.2", "enaltecer el servicio", "alentar a la adoración comunitaria.")],
 "w10:65": [("99:6.3", "Pero cuando la religión", "la cristalización de los sentimientos;"),
            ("99:6.3", "la desviación de la religión", "administradores en vez de ministros;"),
            ("99:6.3", "y la pérdida gradual", "de la salvación eterna.")],
 "w10:95": [("107:0.3", "Dios, habiendo mandado", "con este Ajustador divino")],
 "w10:99": [("107:1.2", "todos están de acuerdo", "del Dios infinito."),
            ("107:1.2", "son de Dios, y en cuanto", "son Dios.")],
 "w10:103": [("107:0.6", "El Ajustador es una esencia", "de una criatura finita"),
             ("107:0.6", "El Ajustador es la realidad", "el alma hacia Dios.")],
 "w10:107": [("108:5.3", "Los ángeles y otros", "todos los siete grupos.")],
 "w10:127": [("110:3.4", "La meta magna", "del Ajustador residente;"),
             ("110:3.4", "Pero un esfuerzo dedicado", "honorable en la tierra."),
             ("110:3.4", "la vida ideal es", "aprehensión temerosa.")],
 "w10:133": [("107:0.7", "desde la llegada del Ajustador", "Controladores del Pensamiento.")],
 "w10:174": [("111:2.4", "Existen tres", None), ("111:2.5", "1. La mente", None) if False else None],
 "w10:190": [("111:3.7", "Pero es por siempre verdad", "vale la pena terminarlo.")],
 "w10:196": [("112:0.1", "Urantia es tu punto", "unión temporal."),
             ("112:0.1", "Has recibido el don de una guía perfecta;", "Has recibido el don de una guía perfecta;"),
             ("112:0.1", "Y a través de todas", "en presencia del cambio.")],
 "w10:224": [("100:2.7", "Jesús ilustró", "absolutamente inatacable")],
 "w10:250": [("91:8.11", "Dios responde", "de la experiencia humana")],
 "w10:268": [("111:5.6", "Esta elección no consiste", "que se haga tu voluntad».")],
 "w10:311": [("117:6.23", "El hombre puede descubrir", "todos los demás hombres")],
 "w10:315": [("117:6.3", "su Deidad es la gran avenida", "quien es amor.")],
 "w11:63": [("120:4.2", "No fue Dios en asociación", "ese ser combinado.")],
 "w11:81": [("121:1.1", "Cuando Micael se encarnó", "desde entonces.")],
 "w11:155": [("132:4.2", "La tesis de su mensaje", "haciéndoles preguntas."),
             ("132:4.2", "Como regla,", "ansiosos y deprimidos")],
 "w11:175": [("129:4.7", "Jesús no vivió su vida en la tierra", "todos los demás seres humanos."),
             ("129:4.7", "No podéis aspirar", "él vivió la suya."),
             ("129:4.7", "Jesús es la senda nueva", "del tiempo a la eternidad.")],
 "w11:183": [("134:8.8", "Ante todas las componendas", "que está en el Paraíso».")],
 "w11:200": [("134:9.8", "Pero Jesús siguió trabajando", "para ser bautizado.")],
 "w11:206": [("136:2.6", "Su bautismo fue su consagración", "los asuntos de su Padre")],
 "w11:212": [("136:2.3", "muchos observadores superhumanos", "en quien tengo complacencia».")],
 "w11:232": [("141:5.1", "No hace falta que veáis", "naturaleza y destino.")],
 "w11:242": [("137:8.9", "el reino de mi Padre nada", "el reino del cielo.")],
 "w12:31": [("172:3.10", "Bajando los ojos", "al evangelio de la salvación.")],
 "w12:77": [("187:5.6", "Jesús murió majestuosamente", "todo ese día trágico."),
            ("187:5.6", "Después de semejante vida", "«Consumado es».")],
 "w12:89": [("188:4.1", "A pesar de que Jesús no murió", "obtuviera la salvación")],
 "w12:97": [("188:4.7", "Aunque no sea adecuado", "más claro y seguro el camino de la salvación (sobrevivencia)")],
 "w12:148": [("189:2.7", "La tumba de José", "una disolución especial y singular")],
 "w12:160": [("189:4.10", "Mientras ellas reflexionaban", "«¡Mi Señor, y mi Maestro!»")],
 "w12:202": [("193:5.2", "Amad a los hombres", "así como yo os he servido."),
             ("193:5.2", "Mi amor os sobrecogerá", "Adiós")],
 "w12:224": [("194:3.6", "este don del espíritu", "en todo el mundo."),
             ("194:3.6", "Por fin, la religión", "el alma de cada hombre.")],
 "w12:258": [("196:2.1", "Podéis predicar", "resucitado y glorificado.")],
 "w12:275": [("196:0.1", "JESÚS poseía", "la guía de Dios."),
             ("196:0.1", "Su fe no fue ni tradicional", "puramente espiritual.")],
}
# w10:174: range 111:2.4-7
P["w10:174"] = [("111:2.4", "Existen tres", None), ("111:2.5", "1. La mente", None),
                ("111:2.6", "2. El espíritu divino que mora en esta mente humana", "2. El espíritu divino que mora en esta mente humana"),
                ("111:2.7", "3. La relación", None)]

out = {}
for k, pieces in P.items():
    segs = []
    joiner = []
    for (v, s, e) in pieces:
        segs.append(amq.cut("es", v, s, e))
    out[k] = segs

def join(k, segs):
    # pieces from adjacent verses joined by space unless an omission follows
    if k == "w10:174":
        return segs[0] + " " + segs[1] + " " + segs[2] + " … " + segs[3]
    return " … ".join(segs)

res = {}
for k in todo:
    q = join(k, out[k])
    res[k] = q
    cit = todo[k]["cit"]
    print(k, q[:80], "...", q[-40:])
json.dump(res, open(os.path.join(ROOT, "es", "quotes_c03.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(res), "written")
