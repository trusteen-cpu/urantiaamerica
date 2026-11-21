import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c16.json')
OUT = os.path.join(BASE, 'pt', 'c16.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in T.items():
        assert k in src, k
        if isinstance(src[k], list):
            assert isinstance(v, list) and len(v) == len(src[k]), k
            for a, b in zip(v, src[k]):
                assert len(a) == len(b), (k, a)
        else:
            assert isinstance(v, str), k
        cur[k] = v
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), '/', len(src))
