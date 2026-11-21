import json, glob, os, importlib.util
base = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(base, '..', '..'))
src = json.load(open(os.path.join(root, 'work', 'src_c13.json'), encoding='utf-8'))
T = {}
for f in sorted(glob.glob(os.path.join(base, 'part*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k in m.T:
        if k not in src: print('UNKNOWN KEY', k)
    T.update(m.T)
out = {k: T[k] for k in src if k in T}
missing = [k for k in src if k not in T]
json.dump(out, open(os.path.join(root, 'es', 'c13.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(out), 'missing', len(missing), missing[:5])
