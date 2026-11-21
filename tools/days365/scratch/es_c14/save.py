import json, os
B = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(B, 'es', 'c14.json')
SRC = os.path.join(B, 'work', 'src_c14.json')


def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k, v in units.items():
        assert k in src, k
        assert v['_ref'] == src[k]['_ref'], k
        assert len(v['msg']) == len(src[k]['msg']), (k, len(v['msg']), len(src[k]['msg']))
        cur[k] = {'_ref': v['_ref'], 't': v['t'], 'msg': v['msg'], 'pr': v['pr']}
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'units:', ', '.join(units))
