import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c08.json')
OUT = os.path.join(BASE, 'fr', 'c08.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k in T:
        if k not in src:
            raise SystemExit('unknown key ' + k)
        if type(T[k]) != type(src[k]):
            raise SystemExit('type mismatch ' + k)
        if isinstance(src[k], list):
            if len(T[k]) != len(src[k]) or any(len(a) != len(b) for a, b in zip(T[k], src[k])):
                raise SystemExit('table shape ' + k)
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src))
