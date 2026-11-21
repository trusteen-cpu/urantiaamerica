import json, os, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
src = json.load(open(os.path.join(ROOT, 'work', 'src_c06.json'), encoding='utf-8'))
out = os.path.join(ROOT, 'es', 'c06.json')
cur = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else {}
for f in sorted(glob.glob(os.path.join(HERE, 'part*.py'))):
    spec = importlib.util.spec_from_file_location('m', f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.D.items():
        assert k in src, k
        cur[k] = v
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in D]
print('saved', len(D), 'of', len(src), 'missing', len(missing), missing[:5])
