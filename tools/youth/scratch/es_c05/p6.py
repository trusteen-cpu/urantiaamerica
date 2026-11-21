import json, os
from save import save, OUT
D = json.load(open(OUT, encoding='utf-8'))
R = [
("p48.014", "«⟦Q 48:4.15⟧⟦/Q⟧».", "«⟦Q 48:4.15⟧El humorismo es el antídoto divino contra la exaltación del ego⟦/Q⟧»."),
("p48.024", "«⟦Q 48:7.26⟧⟦/Q⟧»", "«⟦Q 48:7.26⟧Las acciones de hoy son el destino de mañana⟦/Q⟧»"),
("p49.005", "«⟦Q 49:1.6⟧⟦/Q⟧».", "«⟦Q 49:1.6⟧El hombre mortal no es un accidente evolucionario⟦/Q⟧»."),
("p53.023", "«⟦Q 53:7.12⟧⟦/Q⟧».", "«⟦Q 53:7.12⟧No se ha perdido un solo ciudadano de Jerusem⟦/Q⟧»."),
("p54.004", "«⟦Q 54:1.5⟧⟦/Q⟧»", "«⟦Q 54:1.5⟧El libertinaje que se enmascara en el manto de la libertad es el precursor de la esclavitud abyecta⟦/Q⟧»."),
("p56.002", "es: «⟦Q 56:0.1⟧⟦/Q⟧».", "es: «⟦Q 56:0.1⟧DIOS es unidad⟦/Q⟧»."),
("p56.002", "Padre: «⟦Q 56:0.1⟧⟦/Q⟧».", "Padre: «⟦Q 56:0.1⟧Sed perfectos, así como yo soy perfecto⟦/Q⟧»."),
("p56.031", "dice: «⟦Q 56:10.14⟧⟦/Q⟧»,", "dice: «⟦Q 56:10.14⟧Ningún hombre vive para sí⟦/Q⟧»,"),
("p56.031", "«⟦Q 56:10.21⟧⟦/Q⟧» Hacer", "«⟦Q 56:10.21⟧El amor es el deseo de hacer el bien a los demás⟦/Q⟧». Hacer"),
]
T = {}
for k, a, b in R:
    s = T.get(k, D[k])
    assert a in s, (k, a)
    T[k] = s.replace(a, b)
save(T)
