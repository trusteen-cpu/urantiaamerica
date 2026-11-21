import json, os
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
OUT = os.path.join(BASE, 'es', 'c07.json')
SRC = os.path.join(BASE, 'work', 'src_c07.json')

def save(D):
    S = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in D:
        if k not in S:
            raise SystemExit('unknown key ' + k)
        if type(D[k]) != type(S[k]):
            raise SystemExit('type mismatch ' + k)
        if isinstance(S[k], list):
            if len(D[k]) != len(S[k]) or any(len(a) != len(b) for a, b in zip(D[k], S[k])):
                raise SystemExit('table shape ' + k)
    cur.update(D)
    res = {k: cur[k] for k in S if k in cur}
    json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in S if k not in res]
    print('saved', len(res), 'missing', len(missing), missing[:5])
