import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c08.json')
OUT = os.path.join(BASE, 'fr', 'c08.json')

def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    cur.update(units)
    for k, u in units.items():
        assert u['_ref'] == src[k]['_ref'], k
        assert len(u['msg']) == len(src[k]['msg']), k
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), 'units')
