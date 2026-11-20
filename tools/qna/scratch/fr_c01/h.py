import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FR = json.load(open(os.path.join(BASE, '..', 'data', 'fr.json'), encoding='utf-8'))
OUT = os.path.join(BASE, 'fr', 'c01.json')
SRC = json.load(open(os.path.join(BASE, 'work_fr', 'src_c01.json'), encoding='utf-8'))


def V(ref):
    return FR[ref]


def refs(*keys):
    """'0:3.9 <verse> 0:3.10 <verse> ...'"""
    return ' '.join(k + ' ' + FR[k] for k in keys)


def Q(ref, txt):
    assert ''.join(txt.split()) in ''.join(FR[ref].split()), (ref, txt)
    return '⟦Q %s⟧%s⟦/Q⟧' % (ref, txt)


def sub(ref, piece, repl):
    t = FR[ref]
    assert piece in t, (ref, piece)
    return t.replace(piece, repl, 1)


def save(units):
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(units)
    order = list(SRC.keys())
    D = {k: D[k] for k in order if k in D}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(order))
