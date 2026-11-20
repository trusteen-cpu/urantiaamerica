import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
OUT = os.path.join(BASE, 'pt', 'c03.json')
SRC = os.path.join(BASE, 'work', 'src_c03.json')


def save(units):
    S = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in units:
        if k not in S:
            raise SystemExit('unknown key ' + k)
    D.update(units)
    # keep source order
    R = {k: D[k] for k in S if k in D}
    json.dump(R, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in S if k not in R]
    print('written', len(R), 'missing', len(missing))
