import json
V=json.load(open('../data/es.json',encoding='utf-8'))
def cut(v,a,b=None):
    s=V[v]; i=s.index(a)
    if b is None: return a
    j=s.index(b,i)+len(b); return s[i:j]
Q={
"142.b14.q":cut("142:2.2","un padre verdadero","de la familia"),
"142.b26.q":cut("142:5.3","el que haya nacido","aun vuestra fe."),
"143.b27.q":cut("143:5.6","Dios es espíritu, y","en verdad."),
"144.b14.q":cut("144:2.3","La oración es el aliento","del Padre."),
"144.b37.q":cut("144:8.4","entre los nacidos de mujer","es más grande"),
"145.b18.q":cut("145:3.11","Lo que un Hijo Creador","SE HACE REALIDAD."),
"145.b32.q":cut("145:5.4","el reino del Padre no","curaciones físicas"),
"146.b17.q":cut("146:3.2","la intolerancia es la máscara","creencias de uno."),
"147.b28.q":cut("147:6.4","el sábado fue hecho","para el sábado."),
"148.b5.q":"Dios reside dentro de ti … se ha hecho como eres tú para que pueda hacerte como es él",
"149.b35.q":cut("149:6.5","He venido al mundo","en el lugar del terror"),
"149.b44.q":cut("149:6.3","Es este cambio","en la tierra."),
}
for k,v in Q.items(): print(k,v)
json.dump(Q,open('es/quotes_c19.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
