import json, os, sys
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'fr', 'c11.json')
SRC = os.path.join(BASE, 'work', 'src_c11.json')

def save(part):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in part:
        if k not in src:
            raise SystemExit('unknown key ' + k)
    cur.update(part)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
