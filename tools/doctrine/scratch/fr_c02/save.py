import json, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
SRC = os.path.join(root, 'work', 'src_c02.json')
OUT = os.path.join(root, 'fr', 'c02.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        assert k in src, k
        s, t = src[k], T[k]
        if isinstance(s, dict):
            assert isinstance(t, dict), k
            if 'rows' in s:
                assert len(s['rows']) == len(t['rows']), k
                for a, b in zip(s['rows'], t['rows']):
                    assert len(a) == len(b), (k, a)
            else:
                assert len(s['items']) == len(t['items']), k
        else:
            assert isinstance(t, str), k
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
