import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c15.json')
OUT = os.path.join(BASE, 'fr', 'c15.json')


def merge(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k in T:
        assert k in src, ('unknown key', k)
        sv, tv = src[k], T[k]
        assert type(sv) == type(tv), ('type', k)
        if isinstance(sv, list):
            assert len(sv) == len(tv), ('rows', k)
            for a, b in zip(sv, tv):
                assert len(a) == len(b), ('cells', k)
        assert sv.count('⟦') == tv.count('⟦') if isinstance(sv, str) else True, ('markers', k)
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print('saved', len(D), '/', len(src), 'missing', len(missing))
