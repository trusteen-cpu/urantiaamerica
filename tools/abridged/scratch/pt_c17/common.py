import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(BASE, 'pt', 'c17.json')
SRC = os.path.join(BASE, 'work', 'src_c17.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        if isinstance(src[k], list):
            assert isinstance(T[k], list) and len(T[k]) == len(src[k]), k
            for a, b in zip(T[k], src[k]):
                assert len(a) == len(b), (k, a)
        else:
            assert isinstance(T[k], str), k
    D.update(T)
    O = {k: D[k] for k in src if k in D}
    json.dump(O, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(O), 'of', len(src), 'missing:', [k for k in src if k not in O][:5])
