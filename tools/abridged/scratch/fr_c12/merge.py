import json, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
src = json.load(open(os.path.join(ROOT, 'work', 'src_c12.json'), encoding='utf-8'))
out_path = os.path.join(ROOT, 'fr', 'c12.json')
cur = json.load(open(out_path, encoding='utf-8')) if os.path.exists(out_path) else {}
for name in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.D.items():
        if k not in src:
            print('UNKNOWN KEY', k); continue
        s = src[k]
        if type(s) != type(v):
            print('TYPE', k); continue
        if isinstance(s, list):
            if len(s) != len(v) or any(len(a) != len(b) for a, b in zip(s, v)):
                print('SHAPE', k); continue
        cur[k] = v
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in cur]
print('have', len(D), 'of', len(src), 'missing', len(missing), missing[:8])
