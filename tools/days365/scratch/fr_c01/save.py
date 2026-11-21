import json, os, re, importlib.util, sys
H = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
P = os.path.join(H, 'fr', 'c01.json')
S = json.load(open(os.path.join(H, 'work', 'src_c01.json'), encoding='utf-8'))
QRE = re.compile(r'⟦Q ([^⟧]+)⟧')

def save(units):
    D = json.load(open(P, encoding='utf-8')) if os.path.exists(P) else {}
    for k, u in units.items():
        if isinstance(S[k], str):
            D[k] = u
            continue
        assert len(u['msg']) == len(S[k]['msg']), k
        a = QRE.findall(' '.join(S[k]['msg']) + ' ' + S[k]['pr'])
        b = QRE.findall(' '.join(u['msg']) + ' ' + u['pr'])
        assert a == b, (k, a, b)
        D[k] = {'_ref': S[k]['_ref'], 't': u['t'], 'msg': u['msg'], 'pr': u['pr']}
    D = {k: D[k] for k in S if k in D}
    os.makedirs(os.path.dirname(P), exist_ok=True)
    json.dump(D, open(P, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), 'of', len(S))

if __name__ == '__main__':
    for f in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location('p', os.path.join(os.path.dirname(os.path.abspath(__file__)), f))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        save(m.U)
