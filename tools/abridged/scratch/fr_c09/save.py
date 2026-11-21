import json, os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c09.json')
OUT = os.path.join(BASE, 'fr', 'c09.json')

def save(new):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in new.items():
        if k not in src:
            raise SystemExit('unknown key ' + k)
        sv = src[k]
        if type(sv) != type(v):
            raise SystemExit('type mismatch ' + k)
        if isinstance(sv, list):
            if len(sv) != len(v) or any(len(a) != len(b) for a, b in zip(sv, v)):
                raise SystemExit('table shape ' + k)
        cur[k] = v
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print('saved', len(D), 'of', len(src), 'missing', len(missing), missing[:5])
