import json, os, sys, importlib
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
src = json.load(open('work/src_c15.json', encoding='utf-8'))
path = 'es/c15.json'
cur = json.load(open(path, encoding='utf-8')) if os.path.exists(path) else {}
sys.path.insert(0, 'scratch/es_c15')
for mod in sys.argv[1:]:
    m = importlib.import_module(mod)
    for k, v in m.T.items():
        assert k in src, k
        cur[k] = v
out = {k: cur[k] for k in src if k in cur}
json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out), 'of', len(src))
