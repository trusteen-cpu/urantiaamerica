import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'pt', 'c14.json')
SRC = os.path.join(BASE, 'work', 'src_c14.json')

def upd(T):
    src = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in T.items():
        assert k in src, k
        s = src[k]
        assert type(s) == type(v), k
        if isinstance(s, list):
            assert len(s) == len(v) and all(len(a) == len(b) for a, b in zip(s, v)), ('table shape', k)
        D[k] = v
    out = {k: D[k] for k in src if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), '/', len(src))
