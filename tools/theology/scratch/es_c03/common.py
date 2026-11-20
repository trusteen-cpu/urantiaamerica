import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c03.json')
OUT = os.path.join(BASE, 'es', 'c03.json')
QOUT = os.path.join(BASE, 'es', 'quotes_c03.json')


def save(upd):
    src = json.load(open(SRC, encoding='utf-8'))
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in upd:
        if k not in src:
            raise SystemExit('unknown key ' + k)
    cur.update(upd)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in D]
    print('saved', len(D), 'missing', len(missing))


def saveq(upd):
    os.makedirs(os.path.dirname(QOUT), exist_ok=True)
    cur = json.load(open(QOUT, encoding='utf-8')) if os.path.exists(QOUT) else {}
    cur.update(upd)
    json.dump(cur, open(QOUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('quotes', len(cur))
