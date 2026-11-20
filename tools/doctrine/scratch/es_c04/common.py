import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c04.json')
OUT = os.path.join(BASE, 'es', 'c04.json')
QOUT = os.path.join(BASE, 'es', 'quotes_c04.json')


def _load(p):
    if os.path.exists(p):
        return json.load(open(p, encoding='utf-8'))
    return {}


def save(units, quotes=None):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = _load(OUT)
    cur.update(units)
    for k in units:
        if k not in src:
            raise SystemExit('unknown key ' + k)
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('units', len(out), '/', len(src))
    if quotes:
        todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c04.json'), encoding='utf-8'))
        q = _load(QOUT)
        q.update(quotes)
        order = list(todo.keys()) if isinstance(todo, dict) else [t if isinstance(t, str) else t.get('key') for t in todo]
        qo = {k: q[k] for k in order if k in q}
        for k in q:
            if k not in qo:
                raise SystemExit('quote key not in todo ' + k)
        json.dump(qo, open(QOUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('quotes', len(qo), '/', len(order))
