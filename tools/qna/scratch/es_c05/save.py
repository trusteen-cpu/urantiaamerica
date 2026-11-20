import json, os, sys
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'es', 'c05.json')
SRC = os.path.join(BASE, 'work_es', 'src_c05.json')


def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(units)
    out = {k: D[k] for k in src if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for k, v in units.items():
        for f in ('question', 'answer'):
            a = src[k][f].count('\n\n'); b = v[f].count('\n\n')
            c = src[k][f].count('\n'); d = v[f].count('\n')
            if a != b or c != d:
                print('STRUCT MISMATCH', k, f, a, b, c, d)
    print('saved', len(out), 'units')
