import sys, os
here = os.path.dirname(os.path.abspath(__file__))
R = [
 ("la dernière Cène", "le dernier souper"),
 ("la chambre haute où ils avaient partagé le dernier souper", "la salle du haut où ils avaient partagé le dernier souper"),
 ("la chambre haute de la maison de Marc", "la salle du haut de la maison de Marc"),
 ("Depuis le dernier souper, Jésus", "Depuis le dernier souper, Jésus"),
]
for p in sys.argv[1:]:
    f = os.path.join(here, "p%s.py" % p)
    s = open(f, encoding="utf-8").read()
    for a, b in R:
        s = s.replace(a, b)
    open(f, "w", encoding="utf-8").write(s)
