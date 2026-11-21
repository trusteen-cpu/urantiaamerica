import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(BASE, 'fr', 'c03.json')
SRC = json.load(open(os.path.join(BASE, 'work', 'src_c03.json'), encoding='utf-8'))


def save(new):
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in new:
        assert k in SRC, k
    cur.update(new)
    D = {k: cur[k] for k in SRC if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(SRC))
