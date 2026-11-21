import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c19.json')
OUT = os.path.join(BASE, 'es', 'c19.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(T)
    bad = [k for k in T if k not in src]
    if bad:
        raise SystemExit('unknown keys: %r' % bad)
    for k, v in T.items():
        s = src[k]
        if type(s) != type(v):
            raise SystemExit('type mismatch ' + k)
        if isinstance(s, list):
            if len(s) != len(v) or any(len(a) != len(b) for a, b in zip(s, v)):
                raise SystemExit('table shape ' + k)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src), 'missing:', [k for k in src if k not in D][:5])
