import json, os, sys, re, importlib.util
B = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(B, '..', '..')
src = json.load(open(os.path.join(R, 'work/src_c11.json'), encoding='utf-8'))
hints = json.load(open(os.path.join(R, 'work/title_hints_pt.json'), encoding='utf-8'))
out_p = os.path.join(R, 'pt/c11.json')
cur = json.load(open(out_p, encoding='utf-8')) if os.path.exists(out_p) else {}
FIX = {'Overview': 'Visão geral', 'The Paper': 'O documento', 'Conclusion': 'Conclusão'}
new = {}
for f in sorted(os.listdir(B)):
    if re.match(r'p\d+\.py$', f):
        spec = importlib.util.spec_from_file_location(f[:-3], os.path.join(B, f))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        new.update(m.T)
for k, v in src.items():
    if k in new:
        cur[k] = new[k]
    elif k.endswith('.title') or k.endswith('.h'):
        if k in hints:
            cur[k] = hints[k]
        elif v in FIX:
            cur[k] = FIX[v]
        elif v.startswith('Key Points of Paper '):
            cur[k] = 'Pontos-chave do documento ' + v.split()[-1]
D = {k: cur[k] for k in src if k in cur}
for k in D:
    a, b = src[k], D[k]
    if type(a) != type(b): print('TYPE', k)
    if isinstance(a, list):
        if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)): print('SHAPE', k)
json.dump(D, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('units', len(D), '/', len(src), 'missing', [k for k in src if k not in D][:5])
