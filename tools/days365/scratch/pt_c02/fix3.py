# -*- coding: utf-8 -*-
import io
p = "part3.py"
s = io.open(p, encoding="utf-8").read()
R = [
 ("Como Criador, Ele já", "Como Criador, ele já"),
 ("solidarizar-Se", "solidarizar-se"), ("humilhou-Se", "humilhou-se"), ("tornou-Se um soberano", "tornou-se um soberano"),
 ("Diante Dele, portanto", "Diante dele, portanto"),
 ("A Sua vida como Jesus", "A sua vida como Jesus"),
 ("Lhe retribuamos o amor. Só a lealdade dada livremente O alegra", "lhe retribuamos o amor. Só a lealdade dada livremente o alegra"),
 ("sentido, Ele suportou por longo tempo e esperou que os Seus filhos", "sentido, ele suportou por longo tempo e esperou que os seus filhos"),
 ("que Se comprometeu a nunca nos abandonar. Mesmo quando caímos, Ele nos", "que se comprometeu a nunca nos abandonar. Mesmo quando caímos, ele nos"),
]
for a, b in R:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
io.open(p, "w", encoding="utf-8").write(s)
