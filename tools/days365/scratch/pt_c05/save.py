import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'pt', 'c05.json')
SRC = os.path.join(BASE, 'work', 'src_c05.json')


def add(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(units)
    for k, u in units.items():
        s = src[k]
        assert u['_ref'] == s['_ref'], k
        assert len(u['msg']) == len(s['msg']), (k, len(u['msg']), len(s['msg']))
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'units')
