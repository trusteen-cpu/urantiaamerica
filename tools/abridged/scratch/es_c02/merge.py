import json, os, sys, importlib.util, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
H = os.path.dirname(os.path.abspath(__file__))
AB = os.path.normpath(os.path.join(H, '..', '..'))
src = json.load(open(os.path.join(AB, 'work', 'src_c02.json'), encoding='utf-8'))
out_p = os.path.join(AB, 'es', 'c02.json')
D = json.load(open(out_p, encoding='utf-8')) if os.path.exists(out_p) else {}
Q = {}
for name in sorted(os.listdir(H)):
    if name.startswith('p') and name.endswith('.py'):
        spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(H, name))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.T.items():
            if k not in src: print('UNKNOWN KEY', k); continue
            if type(v) != type(src[k]): print('TYPE', k)
            if isinstance(v, list):
                if len(v) != len(src[k]) or any(len(a) != len(b) for a, b in zip(v, src[k])): print('SHAPE', k)
            D[k] = v
        Q.update(getattr(m, 'Q', {}))
O = {k: D[k] for k in src if k in D}
json.dump(O, open(out_p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
qp = os.path.join(AB, 'es', 'quotes_c02.json')
todo = json.load(open(os.path.join(AB, 'work', 'todo_es_c02.json'), encoding='utf-8'))
QQ = json.load(open(qp, encoding='utf-8')) if os.path.exists(qp) else {}
QQ.update(Q)
QQ = {k: QQ[k] for k in todo if k in QQ}
json.dump(QQ, open(qp, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('units', len(O), '/', len(src), 'quotes', len(QQ), '/', len(todo))
print('missing', [k for k in src if k not in O][:10])
