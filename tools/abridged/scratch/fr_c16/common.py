import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c16.json')
OUT = os.path.join(BASE, 'fr', 'c16.json')

def save(new):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k in new:
        if k not in src:
            raise SystemExit('unknown key ' + k)
        a, b = src[k], new[k]
        if type(a) != type(b):
            raise SystemExit('type mismatch ' + k)
        if isinstance(a, list):
            if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)):
                raise SystemExit('table shape ' + k)
    cur.update(new)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src))
