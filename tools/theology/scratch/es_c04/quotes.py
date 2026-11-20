import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, '..', '..'))
data = json.load(open(os.path.join(ROOT, '..', 'data', 'es.json'), encoding='utf-8'))
v1 = data['111:3.7']
v2 = data['148:4.9']
v3 = data['75:8.2']
def upto(v, end):
    i = v.index(end) + len(end)
    return v[:i]
q = {}
a = upto(v1, 'indestructible.')
b = v1[v1.index('Pero es por siempre verdad'):]
q['ch19.s4.u2.q2#0'] = a + ' … ' + b
c = upto(v2, 'en forma segura y certera.')
q['ch24.s3.u2.q1#0'] = c[1:] if c.startswith('«') else c
q['ch25.s3.u1.q2#0'] = upto(v3, 'previa condición biológica.')
for k, s in q.items():
    print(k, s)
json.dump(q, open(os.path.join(ROOT, 'es', 'quotes_c04.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
