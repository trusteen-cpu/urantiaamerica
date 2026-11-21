import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(ROOT, 'fr', 'c06.json')
SRC = os.path.join(ROOT, 'work', 'src_c06.json')

def merge(D):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    cur.update(D)
    res = {}
    for k in src:
        if k in cur:
            u = cur[k]
            assert u['_ref'] == src[k]['_ref'], k
            assert len(u['msg']) == len(src[k]['msg']), (k, len(u['msg']), len(src[k]['msg']))
            res[k] = {'_ref': u['_ref'], 't': u['t'], 'msg': u['msg'], 'pr': u['pr']}
    json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(res), 'units')
