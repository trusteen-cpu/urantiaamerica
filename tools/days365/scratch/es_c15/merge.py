import json, os, sys, importlib.util
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, 'work', 'src_c15.json')
OUT = os.path.join(BASE, 'es', 'c15.json')

def merge(U):
    S = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(U)
    for k, v in U.items():
        assert v['_ref'] == S[k]['_ref'], k
        assert len(v['msg']) == len(S[k]['msg']), (k, len(v['msg']), len(S[k]['msg']))
    out = {k: D[k] for k in S if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), 'units')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location('p', p)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        merge(m.U)
