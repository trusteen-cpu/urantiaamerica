import json, os, glob, runpy
here = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(here, '..', '..')
src = json.load(open(os.path.join(base, 'work/src_c03.json'), encoding='utf-8'))
allp = {}
for f in sorted(glob.glob(os.path.join(here, 'p*.py'))):
    allp.update(runpy.run_path(f)['P'])
out = {}
for k, u in src.items():
    if k not in allp:
        continue
    v = allp[k]
    assert len(v['msg']) == len(u['msg']), (k, len(v['msg']), len(u['msg']))
    assert v['msg'] and all(x.strip() for x in v['msg'])
    out[k] = {"_ref": u['_ref'], "t": v['t'], "msg": v['msg'], "pr": v['pr']}
    # marker count check
    for a, b in zip(u['msg'], v['msg']):
        assert a.count('⟦Q ') == b.count('⟦Q '), (k, a[:40])
json.dump(out, open(os.path.join(base, 'fr/c03.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('units', len(out), 'of', len(src))
