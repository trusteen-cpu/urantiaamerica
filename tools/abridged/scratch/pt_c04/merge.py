import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
OUT = os.path.join(BASE, 'pt', 'c04.json')
SRC = os.path.join(BASE, 'work', 'src_c04.json')

def merge(T):
    src = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        if isinstance(src[k], list):
            assert len(src[k]) == len(T[k]), (k, 'rows')
            for a, b in zip(src[k], T[k]):
                assert len(a) == len(b), (k, a)
        else:
            assert isinstance(T[k], str), k
    D.update(T)
    D = {k: D[k] for k in src if k in D}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
