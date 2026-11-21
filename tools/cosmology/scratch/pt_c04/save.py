import json, os, sys, importlib.util
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(BASE, 'pt', 'c04.json')
SRC = os.path.join(BASE, 'work', 'src_c04.json')

def save(new):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    cur.update(new)
    for k in new:
        assert k in src, k
        if isinstance(src[k], list):
            assert isinstance(new[k], list) and len(new[k]) == len(src[k]), k
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(src))

if __name__ == '__main__':
    for f in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location('b', f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        save(m.T)
