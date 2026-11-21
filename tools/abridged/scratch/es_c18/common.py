import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c18.json')
OUT = os.path.join(BASE, 'es', 'c18.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    D = {}
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding='utf-8'))
    for k, v in T.items():
        assert k in src, k
        assert type(v) == type(src[k]), k
        if isinstance(v, list):
            assert len(v) == len(src[k]), k
            for a, b in zip(v, src[k]):
                assert len(a) == len(b), (k, a)
        D[k] = v
    out = {k: D[k] for k in src if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), 'of', len(src))


def hints(T):
    import re
    th = json.load(open(os.path.join(BASE, 'work', 'title_hints_es.json'), encoding='utf-8'))
    for k in list(T):
        if (k.endswith('.h') or k.endswith('.title')) and k in th:
            T[k] = th[k]
    for k, v in T.items():
        if isinstance(v, list) and v and v[0] and v[0][0] == 'Sección':
            p = k.split('.')[0]
            num = {}
            for hk, hv in th.items():
                if hk.startswith(p + '.b') and hk.endswith('.h'):
                    m = re.match(r'(\d+)\. ', hv)
                    if m: num[m.group(1)] = hv
            for row in v[1:]:
                m = re.match(r'(\d+)\. ', row[0])
                if m and m.group(1) in num: row[0] = num[m.group(1)]
    return T
