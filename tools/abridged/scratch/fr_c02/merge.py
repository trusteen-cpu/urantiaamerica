import json, os, importlib.util, glob
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, '..', '..')
src = json.load(open(os.path.join(root, 'work/src_c02.json'), encoding='utf-8'))
outp = os.path.join(root, 'fr/c02.json')
T = {}
if os.path.exists(outp):
    T = json.load(open(outp, encoding='utf-8'))
for f in sorted(glob.glob(os.path.join(here, 'p*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.D.items():
        assert k in src, ('unknown key', k)
        s = src[k]
        assert type(s) == type(v), ('type', k)
        if isinstance(s, list):
            assert len(s) == len(v) and all(len(a) == len(b) for a, b in zip(s, v)), ('shape', k)
        T[k] = v
out = {k: T[k] for k in src if k in T}
json.dump(out, open(outp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in out]
print('done', len(out), '/', len(src), 'missing', len(missing), missing[:5])
