import json, glob, os, sys
sys.stdout.reconfigure(encoding='utf-8')
B = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src = json.load(open(os.path.join(B, 'work/src_c16.json'), encoding='utf-8'))
T = {}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'p*.py'))):
    ns = {}
    exec(open(f, encoding='utf-8').read(), ns)
    T.update(ns['T'])
out = {}
for k in src:
    if k in T:
        out[k] = T[k]
extra = [k for k in T if k not in src]
print('units', len(out), '/', len(src), 'extra', extra)
for k in out:
    if type(out[k]) != type(src[k]):
        print('TYPE', k)
    if isinstance(src[k], list):
        if len(src[k]) != len(out[k]) or any(len(a) != len(b) for a, b in zip(src[k], out[k])):
            print('SHAPE', k)
json.dump(out, open(os.path.join(B, 'es/c16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
ns = {}
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'quotes.py'), encoding='utf-8').read(), ns)
json.dump(ns['Q'], open(os.path.join(B, 'es/quotes_c16.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes', len(ns['Q']))
