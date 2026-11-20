import json, os
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.abspath(os.path.join(H, '..', '..'))
pt = json.load(open(os.path.join(T, '..', 'data', 'pt.json'), encoding='utf-8'))

def cut(ref, start, end):
    v = pt[ref]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]

E = ' … '
Q = {}
Q['ch08.s3.u1.q1#0'] = cut('15:0.1', 'NO QUE', 'Pai das personalidades.') + E + cut('15:0.1', 'Os Sete Esp', 'grande universo.')
Q['ch08.s3.u3.q1#0'] = cut('15:2.1', 'Apenas o Pai', 'pelo número.')
Q['ch09.s5.u2.q2#0'] = cut('32:5.8', 'A corrida', 'toda a carne.')
Q['ch12.s2.u2.q1#0'] = cut('20:2.9', 'Em todo o seu', 'dos mortais.')
Q['ch12.s3.u3.q1#0'] = cut('20:6.2', 'Numa miss', 'ser humano.') + E + cut('20:6.2', 'Fazem pedidos', 'em que servem.')
todo = json.load(open(os.path.join(T, 'work', 'todo_pt_c02.json'), encoding='utf-8'))
assert set(todo) == set(Q), (set(todo) ^ set(Q))
json.dump(Q, open(os.path.join(T, 'pt', 'quotes_c02.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
