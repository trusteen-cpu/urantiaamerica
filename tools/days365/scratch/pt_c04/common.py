import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c04.json')
OUT = os.path.join(BASE, 'pt', 'c04.json')

def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(units)
    for k, v in units.items():
        assert v['_ref'] == src[k]['_ref'], k
        assert len(v['msg']) == len(src[k]['msg']), (k, len(v['msg']), len(src[k]['msg']))
    out = {k: D[k] for k in src if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), 'units')
