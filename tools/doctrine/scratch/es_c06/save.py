import json, os
SRC = 'work/src_c06.json'
OUT = 'es/c06.json'

def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in units.items():
        assert k in src, k
        s = src[k]
        if isinstance(s, dict):
            assert isinstance(v, dict) and set(v) == set(s), k
            if 'rows' in s:
                assert len(v['rows']) == len(s['rows']), k
                for a, b in zip(v['rows'], s['rows']):
                    assert len(a) == len(b), (k, a)
            if 'items' in s:
                assert len(v['items']) == len(s['items']), k
        else:
            assert isinstance(v, str), k
        cur[k] = v
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
