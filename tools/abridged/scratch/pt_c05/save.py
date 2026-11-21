import json, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..')
SRC = os.path.join(BASE, 'work', 'src_c05.json')
OUT = os.path.join(BASE, 'pt', 'c05.json')

def save(d):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(d)
    for k in d:
        if k not in src:
            raise SystemExit('unknown key ' + k)
        if type(d[k]) != type(src[k]):
            raise SystemExit('type ' + k)
        if isinstance(src[k], list):
            if len(src[k]) != len(d[k]) or any(len(a) != len(b) for a, b in zip(src[k], d[k])):
                raise SystemExit('table shape ' + k)
    res = {k: cur[k] for k in src if k in cur}
    json.dump(res, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k.split('.')[0] in {k2.split('.')[0] for k2 in d} and k not in res]
    print('saved', len(res), 'of', len(src), 'missing in these papers:', missing)
