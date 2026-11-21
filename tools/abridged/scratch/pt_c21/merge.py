import json, os, glob, importlib.util
here = os.path.dirname(os.path.abspath(__file__))
os.chdir(os.path.join(here, '..', '..'))
s = json.load(open('work/src_c21.json', encoding='utf-8'))
T = {}
for f in sorted(glob.glob(os.path.join(here, 'p1*.py'))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); T.update(m.T)
extra = set(T) - set(s)
assert not extra, extra
for k in T:
    if type(T[k]) != type(s[k]): raise SystemExit('type ' + k)
    if isinstance(s[k], list):
        assert len(T[k]) == len(s[k]) and all(len(a) == len(b) for a, b in zip(T[k], s[k])), 'shape ' + k
D = {k: T[k] for k in s if k in T}
json.dump(D, open('pt/c21.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('units', len(D), 'of', len(s), 'missing', [k for k in s if k not in T][:5])
