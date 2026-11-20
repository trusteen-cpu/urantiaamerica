import json, os, sys, importlib
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(BASE, 'work', 'src_c06.json')
OUT = os.path.join(BASE, 'es', 'c06.json')

def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k in T:
        if k not in src:
            raise SystemExit('unknown key ' + k)
    cur.update(T)
    out = {k: cur[k] for k in src if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in out]
    print('saved', len(out), 'missing', len(missing), missing[:5])

if __name__ == '__main__':
    for m in sys.argv[1:]:
        sys.path.insert(0, os.path.dirname(__file__))
        save(importlib.import_module(m).T)
