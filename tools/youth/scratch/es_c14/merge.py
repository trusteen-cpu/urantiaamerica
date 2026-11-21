import json, sys, os, importlib.util
sys.stdout.reconfigure(encoding='utf-8')
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, '..', '..'))
OUT = os.path.join(ROOT, 'es', 'c14.json')
src = json.load(open(os.path.join(ROOT, 'work', 'src_c14.json'), encoding='utf-8'))
cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
for name in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location(name, os.path.join(BASE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in src, k
        cur[k] = v.strip()
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in D]
print('units', len(D), 'of', len(src), 'missing', len(missing), missing[:5])
