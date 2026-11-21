import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(BASE, 'fr', 'c20.json')
SRC = os.path.join(BASE, 'work', 'src_c20.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        assert type(T[k]) == type(src[k]), k
        if isinstance(src[k], list):
            assert len(T[k]) == len(src[k]), (k, 'rows')
            for a, b in zip(T[k], src[k]):
                assert len(a) == len(b), (k, a)
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src))
