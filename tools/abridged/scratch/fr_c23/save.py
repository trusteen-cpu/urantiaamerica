import json, os
B = os.path.dirname(os.path.abspath(__file__)) + '/../../'
OUT = B + 'fr/c23.json'
SRC = json.load(open(B + 'work/src_c23.json', encoding='utf-8'))

def save(T):
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in SRC, k
        s, t = SRC[k], T[k]
        assert type(s) == type(t), k
        if isinstance(s, list):
            assert len(s) == len(t) and all(len(a) == len(b) for a, b in zip(s, t)), k
    D.update(T)
    D = {k: D[k] for k in SRC if k in D}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(SRC), 'missing next:', [k for k in SRC if k not in D][:3])
