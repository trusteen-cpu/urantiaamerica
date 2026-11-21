# -*- coding: utf-8 -*-
import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'pt', 'c06.json')
SRC = os.path.join(BASE, 'work', 'src_c06.json')

def save(D):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in D:
        assert k in src, k
        assert type(D[k]) == type(src[k]), k
        if isinstance(src[k], list):
            assert len(D[k]) == len(src[k]), k
            for a, b in zip(D[k], src[k]):
                assert len(a) == len(b), (k, a)
    cur.update(D)
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), '/', len(src))
