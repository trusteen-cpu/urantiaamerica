import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c04.json')
OUT = os.path.join(BASE, 'es', 'c04.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    extra = [k for k in T if k not in src]
    assert not extra, extra
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
