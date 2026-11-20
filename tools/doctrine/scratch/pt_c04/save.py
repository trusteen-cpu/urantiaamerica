import json, os, sys, importlib
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
src = json.load(open(os.path.join(root, 'work', 'src_c04.json'), encoding='utf-8'))
out = os.path.join(root, 'pt', 'c04.json')
cur = json.load(open(out, encoding='utf-8')) if os.path.exists(out) else {}
sys.path.insert(0, here)
for name in sys.argv[1:]:
    m = importlib.import_module(name)
    for k, v in m.T.items():
        if k not in src:
            print('UNKNOWN KEY', k)
            continue
        e = src[k]
        if isinstance(e, dict) and 'rows' in e:
            assert len(e['rows']) == len(v['rows']), k
            for a, b in zip(e['rows'], v['rows']):
                assert len(a) == len(b), (k, a, b)
        if isinstance(e, dict) and 'items' in e:
            assert len(e['items']) == len(v['items']), k
        cur[k] = v
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in D]
print('saved', len(D), 'of', len(src), 'missing', len(missing), missing[:5])
