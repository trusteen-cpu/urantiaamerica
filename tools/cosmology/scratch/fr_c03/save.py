import json, os, sys, importlib
SRC = json.load(open('work/src_c03.json', encoding='utf-8'))
OUT = 'fr/c03.json'

def save(part):
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, v in part.items():
        assert k in SRC, k
        if isinstance(SRC[k], list):
            assert isinstance(v, list) and len(v) == len(SRC[k]), k
        else:
            assert isinstance(v, str), k
        D[k] = v
    D = {k: D[k] for k in SRC if k in D}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(part), 'total', len(D), '/', len(SRC))
    missing = [k for k in SRC if k not in D]
    print('next missing:', missing[:3])

if __name__ == '__main__':
    for name in sys.argv[1:]:
        m = importlib.import_module(name)
        save(m.T)
