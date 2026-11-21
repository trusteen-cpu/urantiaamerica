import json, os, glob, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(here, '..', '..'))
src = json.load(open('work/src_c03.json', encoding='utf-8'))
out = 'fr/c03.json'
D = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else {}
for f in sorted(glob.glob(os.path.join(here, 'p*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in src, ('unknown key', k)
        assert type(v) == type(src[k]), ('type', k)
        if isinstance(v, list):
            assert len(v) == len(src[k]) and all(len(a) == len(b) for a, b in zip(v, src[k])), ('table shape', k)
        D[k] = v
R = {k: D[k] for k in src if k in D}
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(R), 'of', len(src), 'missing:', [k for k in src if k not in R][:5])
