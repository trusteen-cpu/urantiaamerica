import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'pt', 'c06.json')
SRC = os.path.join(BASE, 'work', 'src_c06.json')


def save(P):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    cur.update(P)
    D = {}
    for k in src:
        if k in cur:
            v = cur[k]
            assert v['_ref'] == src[k]['_ref'], k
            assert len(v['msg']) == len(src[k]['msg']), (k, len(v['msg']), len(src[k]['msg']))
            D[k] = {'_ref': v['_ref'], 't': v['t'], 'msg': v['msg'], 'pr': v['pr']}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'units')
