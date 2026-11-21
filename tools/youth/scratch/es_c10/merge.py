import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
YOUTH = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(YOUTH, 'work', 'src_c10.json')
OUT = os.path.join(YOUTH, 'es', 'c10.json')
HEAD = os.path.join(YOUTH, 'work', 'headings_es_c10.json')


def merge(units):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(units)
    # official headings
    h = json.load(open(HEAD, encoding='utf-8'))
    for k, v in h.items():
        if v['official'] and k not in cur:
            num = v['en'].split('. ', 1)[0]
            cur[k] = num + '. ' + v['official'][0].split(': ', 1)[1]
        elif not v['official'] and v['en'] == 'Introduction':
            cur.setdefault(k, 'Introducción')
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('units', len(out), 'of', len(src))
