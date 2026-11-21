# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
C = lambda v, a, b: amq.cut("es", v, a, b)
Q = {
 "w12.009": C("12:3.8", "Estos investigadores llegan", "gravedad absoluta del Paraíso."),
 "w12.010": C("31:10.19", "donde ya podemos", "superuniversos actuales."),
 "w12.049": C("54:5.13", "El valor relativo", "de haberlo cometido."),
 "w12.111": C("27:7.10", "ahora el finalista", "Dios el Último."),
 "w12.132": C("9:4.4", "La mente infinita", "condicionada por el tiempo."),
 "w12.140": C("3:3.5", "La omnipotencia no implica", "que no puede conocerse."),
 "w12.150": C("109:7.4", "son omnipersonales", "después de la personalidad."),
 "w12.194": C("106:6.5", "aunque la existencial", "tan fácil de clasificar."),
 "w12.206": C("106:6.4", "Y parecería también", "relaciones cuantitativas."),
 "w12.210": C("106:7.3", "el destino se consume", "en la Trinidad Absoluta."),
 "w13.027": C("55:0.3", "por lo que sabemos", "todo el tiempo futuro."),
 "w13.054": C("7" if False else "0:2.18", "En este nivel supercreativo", "encuentra el cumplimiento de la divinidad"),
 "w13.077": C("12:1.16", "postulan una creación", "en constante expansión."),
 "w13.126": C("0:7.10", "Toda realidad finita", "de la realidad finita"),
 "w13.147": C("56:6.2", "La evolución del poder", "por medio de la Mente Suprema"),
 "w13.157": C("117:3.7", "Dios el Supremo es él mismo", "como deidad."),
 "w13.205": C("0:12.9", "Los filósofos de los universos", "no pueden visualizar su personalización"),
 "w13.226": C("10:8.8", "porque percibimos", "continúen expandiéndose."),
 "w13.231": C("105:1.5", "Éste es un momento hipotético", "infinidad del YO SOY."),
}
todo = json.load(open(os.path.join(H, "work", "todo_es_c07.json"), encoding="utf-8"))
assert list(Q) == list(todo), set(todo) ^ set(Q)
for k, v in Q.items():
    assert v and amq.check("es", todo[k]["cit"], v), k
json.dump(Q, open(os.path.join(H, "es", "quotes_c07.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(Q))
