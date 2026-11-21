import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c07.json')
OUT = os.path.join(BASE, 'fr', 'c07.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        if isinstance(src[k], list):
            assert len(src[k]) == len(T[k]), (k, len(src[k]), len(T[k]))
            for a, b in zip(src[k], T[k]):
                assert len(a) == len(b), (k, a, b)
        else:
            assert isinstance(T[k], str), k
        cur[k] = T[k]
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src))
