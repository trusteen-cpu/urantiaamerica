import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
data = json.load(open(os.path.join(BASE, '..', 'data', 'es.json'), encoding='utf-8'))
def cut(v, start, end):
    t = data[v]; i = t.index(start); j = t.index(end, i) + len(end); return t[i:j]
Q = {
 "159.b5.q": cut("159:1.2", "En vuestra religi", "pensado seriamente en arrepentirse."),
 "160.b5.q": cut("160:3.1", "La meditaci", "receptividad espiritual."),
 "160.b26.q": data["160:4.16"].split("; ")[-1],
 "161.b14.q": cut("161:1.8", "Que la personalidad de Jes", "presencia de Dios en el hombre."),
 "162.b5.q": cut("162:7.2", "Conocer", "os hará libres"),
 "162.b23.q": cut("162:5.2", "Yo soy la luz del mundo.", "la luz de la vida."),
 "162.b34.q": cut("162:8.3", "los asuntos menores", "reino celestial"),
 "163.b5.q": cut("163:6.7", "Acudid a m", "yo os daré descanso."),
 "163.b11.q": cut("163:1.4", "Habéis recibido generosamente", "dad pues generosamente."),
 "163.b34.q": cut("163:6.2", "no os sintáis entusiastas", "listas del cielo"),
 "164.b5.q": cut("164:4.9", "una cosa sí sé", "ahora veo"),
 "164.b12.q": cut("164:1.3", "Ve pues y haz tú lo mismo", "mismo"),
 "164.b29.q": cut("164:5.3", "así como el Padre está en mí, así", "creen este evangelio"),
 "165.b5.q": cut("165:5.3", "Buscad las cosas más grandes", "serán halladas"),
 "165.b14.q": cut("165:2.8", "yo he venido para", "más abundantemente."),
 "165.b18.q": cut("165:3.8", "el Padre jamás obliga", "en el reino."),
 "165.b29.q": cut("165:5.3", "pedid cosas celestiales", "sigue a la sustancia."),
 "166.b5.q": cut("166:4.10", "la salud no es la sonrisa", "la ira de Dios."),
 "166.b20.q": cut("166:3.3", "Aunque la puerta", "yo soy esa puerta."),
 "167.b5.q": cut("167:1.5", "el que se exalta", "será exaltado."),
 "167.b26.q": cut("167:5.2", "La ley del universo es", "encontrarás."),
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c21.json'), encoding='utf-8'))
assert set(Q) == set(todo)
for k,v in Q.items(): print(k, v)
json.dump(Q, open(os.path.join(BASE, 'es', 'quotes_c21.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
