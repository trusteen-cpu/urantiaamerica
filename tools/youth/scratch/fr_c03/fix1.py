import json
p='part2.py'
s=open(p,encoding='utf-8').read()
s=s.replace('les directeurs de rétrospection','les directeurs de la rétrospection')
s=s.replace('Les étudiants des étoiles, les astronomes du ciel','Les étudiants d’étoiles, les astronomes célestes')
s=s.replace('devenir étudiant des étoiles','devenir étudiant d’étoiles')
open(p,'w',encoding='utf-8').write(s)
