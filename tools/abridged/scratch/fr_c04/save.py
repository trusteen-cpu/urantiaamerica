import json, os, sys, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(here, '..', '..'))
src = json.load(open('work/src_c04.json', encoding='utf-8'))
out_p = 'fr/c04.json'
cur = json.load(open(out_p, encoding='utf-8')) if os.path.exists(out_p) else {}
for name in sys.argv[1:]:
    spec = importlib.util.spec_from_file_location(name, os.path.join(here, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.D.items():
        assert k in src, k
        s = src[k]
        assert type(v) == type(s), k
        if isinstance(s, list):
            assert len(v) == len(s) and all(len(a) == len(b) for a, b in zip(v, s)), ('shape', k)
        cur[k] = v
out = {k: cur[k] for k in src if k in cur}
json.dump(out, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(out), 'of', len(src), 'missing:', [k for k in src if k not in out][:5])
