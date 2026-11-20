import json, os
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.abspath(os.path.join(H, '..', '..'))
SRC = os.path.join(T, 'work', 'src_c02.json')
OUT = os.path.join(T, 'pt', 'c02.json')


def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k in units:
        assert k in src, k
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
