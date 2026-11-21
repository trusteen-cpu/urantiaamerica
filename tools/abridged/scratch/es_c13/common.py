import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c13.json')
OUT = os.path.join(BASE, 'es', 'c13.json')


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


def heads():
    src = json.load(open(SRC, encoding='utf-8'))
    H = json.load(open(os.path.join(BASE, 'work', 'title_hints_es.json'), encoding='utf-8'))
    fixed = {'Overview': 'Panorama general', 'The Paper': 'El documento', 'Conclusion': 'Conclusi\u00f3n'}
    T = {}
    for k, v in src.items():
        if k.endswith('.title') or k.endswith('.h'):
            if v in fixed:
                T[k] = fixed[v]
            elif v.startswith('Key Points of Paper '):
                T[k] = 'Puntos clave del documento ' + v.split()[-1]
            else:
                T[k] = H[k]
    save(T)
