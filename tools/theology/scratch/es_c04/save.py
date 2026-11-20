import json, os, sys, importlib
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, '..', '..'))
SRC = os.path.join(ROOT, 'work', 'src_c04.json')
OUT = os.path.join(ROOT, 'es', 'c04.json')

def save(new):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(new)
    for k in new:
        if k not in src:
            print('UNKNOWN KEY', k)
    out = {k: cur[k] for k in src if k in cur}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), '/', len(src))

if __name__ == '__main__':
    for name in sys.argv[1:]:
        sys.path.insert(0, BASE)
        m = importlib.import_module(name)
        save(m.D)
