import json, os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
OUT = os.path.join(BASE, 'fr', 'c14.json')
SRC = os.path.join(BASE, 'work', 'src_c14.json')
HINTS = os.path.join(BASE, 'work', 'title_hints_fr.json')


def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    hints = json.load(open(HINTS, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in units.items():
        assert k in src, k
        if v == 'HINT':
            v = hints[k]
        if isinstance(src[k], list):
            assert len(v) == len(src[k]), (k, len(v), len(src[k]))
            for a, b in zip(v, src[k]):
                assert len(a) == len(b), (k, a)
        cur[k] = v
    ordered = {k: cur[k] for k in src if k in cur}
    json.dump(ordered, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(ordered), 'of', len(src))


def sec(paper):
    """official section titles for tables: list index n -> 'n. Title'"""
    hints = json.load(open(HINTS, encoding='utf-8'))
    return {int(v.split('.')[0]): v for k, v in hints.items()
            if k.startswith(f'{paper}.b') and k.endswith('.h') and v[0].isdigit()}
