import json, os
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.normpath(os.path.join(base, '..', '..'))
pt = json.load(open(os.path.join(root, '..', 'data', 'pt.json'), encoding='utf-8'))

def cut(ref, start, end):
    v = pt[ref]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]

Q = {}
Q["ch13.s2.u3.q1#0"] = cut("21:4.5", "Segundo consta", "estava literalmente terminado.")
Q["ch13.s3.u1.q1#0"] = cut("120:2.8", "Essa tua grande", "criaturas da carne.")
Q["ch13.s4.u3.q2#0"] = cut("21:6.4", "Quando estava em", "eterna da deidade.")
Q["ch14.s1.u2.q1#0"] = cut("34:1.4", "Essa presen", "pelo Filho Criador.")
for k, v in Q.items():
    print(k, v)
json.dump(Q, open(os.path.join(root, 'pt', 'quotes_c03.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
