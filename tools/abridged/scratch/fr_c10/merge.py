import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
OUT = os.path.join(BASE, 'fr', 'c10.json')
SRC = os.path.join(BASE, 'work', 'src_c10.json')

def merge(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        a, b = src[k], T[k]
        assert type(a) == type(b), k
        if isinstance(a, list):
            assert len(a) == len(b), (k, len(a), len(b))
            for i, (r1, r2) in enumerate(zip(a, b)):
                assert len(r1) == len(r2), (k, i)
        if isinstance(a, str):
            assert a.count('⟦Q') == b.count('⟦Q'), k
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src), 'missing in this paper:',
          [k for k in src if k.split('.')[0] == list(T)[0].split('.')[0] and k not in T])
