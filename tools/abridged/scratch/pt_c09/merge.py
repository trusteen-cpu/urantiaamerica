import json, sys, os, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.normpath(os.path.join(HERE, '..', '..'))
OUT = os.path.join(BASE, 'pt', 'c09.json')
src = json.load(open(os.path.join(BASE, 'work', 'src_c09.json'), encoding='utf-8'))
cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
for name in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in src, k
        if isinstance(src[k], list):
            assert isinstance(v, list) and len(v) == len(src[k]), k
            for a, b in zip(v, src[k]):
                assert len(a) == len(b), (k, a)
        else:
            assert isinstance(v, str), k
        cur[k] = v
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in D]
print('done', len(D), 'missing', len(missing), missing[:5])
