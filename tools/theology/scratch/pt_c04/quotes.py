import json, os
T = os.path.dirname(os.path.abspath(__file__)) + "/../.."
V = json.load(open(T + "/../data/pt.json", encoding="utf-8"))

def cut(ref, start, end):
    v = V[ref]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]

Q = {}
Q["ch19.s4.u2.q2#0"] = cut("111:3.7", "Na mesma medida", "indestrutível.") + " … " + cut("111:3.7", "Todavia, para sempre", "se valer a pena terminar.")
Q["ch20.s1.u3.q2#0"] = cut("107:0.6", "O Ajustador é a realidade", "na direção de Deus.")
Q["ch22.s1.u2.q1#0"] = cut("83:8.1", "O matrimônio que culmina", "considerado um sacramento.")
Q["ch24.s3.u2.q1#0"] = cut("148:4.9", "Os gregos e outros", "e a perfeição divina.")
Q["ch25.s3.u1.q2#0"] = cut("75:8.2", "Não houve uma", "condição biológica anterior.")
Q["ch25.s3.u3.q1#0"] = cut("75:8.6", "Somos parte de", "não a nossa origem.")
json.dump(Q, open(T + "/pt/quotes_c04.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for k, v in Q.items():
    print(k, v)
