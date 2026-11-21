import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c05.json')
OUT = os.path.join(BASE, 'es', 'c05.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    D = {}
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding='utf-8'))
    for k, v in T.items():
        assert k in src, k
        assert type(v) == type(src[k]), k
        if isinstance(v, list):
            assert len(v) == len(src[k]), k
            for a, b in zip(v, src[k]):
                assert len(a) == len(b), (k, a)
        D[k] = v
    out = {k: D[k] for k in src if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), 'of', len(src))
