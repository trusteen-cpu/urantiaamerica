import json, os, importlib.util, glob
src = json.load(open('work/src_c22.json', encoding='utf-8'))
out = 'pt/c22.json'
D = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else {}
for f in sorted(glob.glob('scratch/pt_c22/p[0-9]*.py')):
    spec = importlib.util.spec_from_file_location('m', f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in src, ('unknown key', k)
        s = src[k]
        assert type(v) == type(s), ('type', k)
        if isinstance(s, list):
            assert len(v) == len(s) and all(len(a) == len(b) for a, b in zip(v, s)), ('shape', k)
        D[k] = v
R = {k: D[k] for k in src if k in D}
json.dump(R, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('have', len(R), 'of', len(src), 'missing:', [k for k in src if k not in R][:8])
