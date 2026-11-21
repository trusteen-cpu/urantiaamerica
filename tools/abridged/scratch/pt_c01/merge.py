import json, os, importlib.util, glob
H = os.path.dirname(os.path.abspath(__file__))
S = json.load(open('work/src_c01.json', encoding='utf-8'))
T = {}
for f in sorted(glob.glob(os.path.join(H, 'part_*.py'))):
    sp = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m)
    for k in m.T:
        if k not in S: print('EXTRA KEY', k)
    T.update(m.T)
os.makedirs('pt', exist_ok=True)
D = {k: T[k] for k in S if k in T}
for k in S:
    if k in T and type(T[k]) != type(S[k]): print('TYPE', k)
    if k in T and isinstance(S[k], list):
        if len(S[k]) != len(T[k]) or any(len(a) != len(b) for a, b in zip(S[k], T[k])): print('SHAPE', k)
print('units', len(D), '/', len(S), 'missing', [k for k in S if k not in T][:5])
json.dump(D, open('pt/c01.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
