import json, os, sys, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
base = os.path.abspath(os.path.join(here, '..', '..'))
src = json.load(open(os.path.join(base, 'work', 'src_c01.json'), encoding='utf-8'))
T = {}
for name in sorted(f for f in os.listdir(here) if f.startswith('part') and f.endswith('.py')):
    spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(here, name))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    T.update(m.T)
extra = [k for k in T if k not in src]
assert not extra, extra
D = {k: T[k] for k in src if k in T}
os.makedirs(os.path.join(base, 'fr'), exist_ok=True)
json.dump(D, open(os.path.join(base, 'fr', 'c01.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in T]
print('done', len(D), 'missing', len(missing), missing[:5])
