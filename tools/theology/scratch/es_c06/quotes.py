import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
ES = json.load(open(os.path.join(BASE, '..', 'data', 'es.json'), encoding='utf-8'))
OUT = os.path.join(BASE, 'es', 'quotes_c06.json')
SEP = ' … '

def cut(ref, start, end):
    v = ES[ref]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]

Q = {
 "ch32.s1.u1.q2#0": cut("194:4.6", "Es verdad que, de estas", "Padre en el cielo.") + SEP + cut("194:4.6", "Cometieron el gran error", "haya conocido jamás."),
 "ch32.s1.u2.q2#0": cut("196:2.1", "En el entusiasmo de Pentecostés", "del apóstol Pablo."),
 "ch33.s3.u1.q1#0": cut("101:8.1", "La creencia llega", "es meramente creencia") + SEP + cut("101:8.1", "Una persona cree en la verdad", "infinitamente más."),
 "ch35.s4.u1.q1#0": cut("40:7.4", "Éstos son los mortales", "perfección última de vosotros."),
 "ch35.s4.u1.q2#0": cut("40:7.5", "La fusión con un fragmento", "cada uno de vosotros!"),
 "ch36.s2.u3.q1#0": cut("47:7.5", "Un verdadero nacimiento", "mundo de estancia número cinco") + SEP + cut("47:7.5", "El estudio se está volviendo", "está evolucionando."),
 "ch36.s2.u4.q1#0": cut("48:6.35", "De ellos aprenderás", "para probar de nuevo?"),
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c06.json'), encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
json.dump(Q, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in Q.items():
    print(k, '=>', v)
