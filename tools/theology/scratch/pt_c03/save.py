import json, os
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.normpath(os.path.join(base, '..', '..'))
SRC = os.path.join(root, 'work', 'src_c03.json')
OUT = os.path.join(root, 'pt', 'c03.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(T)
    bad = [k for k in T if k not in src]
    if bad:
        raise SystemExit('unknown keys: %s' % bad)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print('saved', len(D), 'of', len(src), 'missing', len(missing))
