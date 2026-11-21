import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c01.json')
OUT = os.path.join(BASE, 'es', 'c01.json')
def save(new):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(new)
    D = {k: cur[k] for k in src if k in cur}
    for k, v in D.items():
        if isinstance(v, dict):
            assert v['_ref'] == src[k]['_ref'], k
            assert len(v['msg']) == len(src[k]['msg']), (k, len(v['msg']), len(src[k]['msg']))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
