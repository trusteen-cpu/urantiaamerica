import json, os, sys, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
COS = os.path.normpath(os.path.join(H, '..', '..'))
SRC = json.load(open(os.path.join(COS, 'work', 'src_c05.json'), encoding='utf-8'))
OUT = os.path.join(COS, 'fr', 'c05.json')
D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
for name in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location(name, os.path.join(H, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in SRC, k
        if isinstance(SRC[k], list):
            assert isinstance(v, list) and len(v) == len(SRC[k]), k
        else:
            assert isinstance(v, str), k
        assert '|' not in json.dumps(v, ensure_ascii=False), k
        D[k] = v
R = {k: D[k] for k in SRC if k in D}
json.dump(R, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(R), '/', len(SRC), 'missing:', [k for k in SRC if k not in R][:8])
