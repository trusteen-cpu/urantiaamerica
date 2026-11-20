import json, os
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(ROOT, 'es', 'c03.json')
SRC = os.path.join(ROOT, 'work', 'src_c03.json')


import re
REFLIST = re.compile(r"^\d+:\d+\.\d+(?:~\d+)?(?:, \d+:\d+\.\d+(?:~\d+)?){2,}$")


def fixrefs(t):
    if isinstance(t, dict) and 'rows' in t:
        t['rows'] = [[(c.rsplit(', ', 1)[0] + ' y ' + c.rsplit(', ', 1)[1]) if REFLIST.match(c) else c for c in r] for r in t['rows']]
    return t


def save(units):
    units = {k: fixrefs(v) for k, v in units.items()}
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in units:
        if k not in src:
            raise KeyError(k)
        e, t = src[k], units[k]
        if isinstance(e, dict):
            if 'rows' in e:
                assert len(e['rows']) == len(t['rows']), k
                for a, b in zip(e['rows'], t['rows']):
                    assert len(a) == len(b), (k, a)
            else:
                assert len(e['items']) == len(t['items']), k
    cur.update(units)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print('saved', len(D), 'missing', len(missing), missing[:10])
