import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c02.json')
OUT = os.path.join(BASE, 'fr', 'c02.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in T:
        if k not in src:
            raise SystemExit('unknown key ' + k)
    cur.update(T)
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in out]
    print('saved', len(out), 'of', len(src), '; missing', len(missing))
