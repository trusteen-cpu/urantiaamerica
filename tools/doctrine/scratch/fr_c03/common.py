import json, os
BASE = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c03.json')
OUT = os.path.join(BASE, 'fr', 'c03.json')


def add(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in T.items():
        assert k in src, k
        e = src[k]
        if isinstance(e, dict) and 'rows' in e:
            assert len(v['rows']) == len(e['rows']), k
            for a, b in zip(v['rows'], e['rows']):
                assert len(a) == len(b), (k, a)
        if isinstance(e, dict) and 'items' in e:
            assert len(v['items']) == len(e['items']), k
        assert type(v) == type(e), k
        cur[k] = v
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in cur]
    print('written', len(D), 'missing', len(missing), missing[:8])
