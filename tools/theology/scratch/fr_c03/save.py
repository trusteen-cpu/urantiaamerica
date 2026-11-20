import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
TH = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(TH, 'work', 'src_c03.json')
OUT = os.path.join(TH, 'fr', 'c03.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    bad = [k for k in T if k not in src]
    if bad:
        raise SystemExit('unknown keys: %s' % bad)
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
