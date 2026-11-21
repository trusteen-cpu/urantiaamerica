import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, 'work', 'src_c07.json')
OUT = os.path.join(BASE, 'es', 'c07.json')
HEAD = os.path.join(BASE, 'work', 'headings_es_c07.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    heads = json.load(open(HEAD, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    # headings from official titles
    for k, h in heads.items():
        if k not in cur:
            if h['official']:
                t = h['official'][0]
                num, rest = t.split(': ', 1)
                cur[k] = num + '. ' + rest
            else:
                cur[k] = 'Introducción'
    for k, v in T.items():
        assert k in src, k
        cur[k] = v
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))
