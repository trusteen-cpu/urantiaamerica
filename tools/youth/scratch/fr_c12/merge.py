import json, os, sys, importlib.util
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = json.load(open(os.path.join(BASE, 'work', 'src_c12.json'), encoding='utf-8'))
out = os.path.join(BASE, 'fr', 'c12.json')
cur = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else {}
for f in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location('m', os.path.join(os.path.dirname(__file__), f))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in src, k
        cur[k] = v.strip()
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('units', len(D), '/', len(src), 'missing:', [k for k in src if k not in D][:5])
