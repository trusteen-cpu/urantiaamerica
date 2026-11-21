import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'es', 'c04.json')
SRC = os.path.join(BASE, 'work', 'src_c04.json')

def save(part):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in part:
        assert k in src, k
        if isinstance(src[k], list):
            assert len(src[k]) == len(part[k]), (k, 'rows')
            for a, b in zip(src[k], part[k]):
                assert len(a) == len(b), (k, a, b)
        else:
            assert isinstance(part[k], str), k
    cur.update(part)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src), 'missing:', [k for k in src if k not in D][:5])
