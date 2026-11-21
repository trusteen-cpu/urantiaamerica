import json, os, sys, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
src = json.load(open('work/src_c13.json', encoding='utf-8'))
T = {}
for i in range(1, 10):
    p = os.path.join(here, f'part{i}.py')
    if os.path.exists(p):
        spec = importlib.util.spec_from_file_location(f'part{i}', p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        T.update(m.T)
out = {k: T[k] for k in src if k in T}
extra = [k for k in T if k not in src]
print('units', len(out), '/', len(src), 'extra', extra)
json.dump(out, open('fr/c13.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
