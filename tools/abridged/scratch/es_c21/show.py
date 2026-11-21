import json, os, sys
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
s = json.load(open(os.path.join(BASE,'work','src_c21.json'), encoding='utf-8'))
inl = json.load(open(os.path.join(BASE,'work','inline_es_c21.json'), encoding='utf-8'))
th = json.load(open(os.path.join(BASE,'work','title_hints_es.json'), encoding='utf-8'))
p = sys.argv[1]
out = []
for k, v in s.items():
    if k.split('.')[0] != p: continue
    out.append('## ' + k + ('   HINT: ' + th[k] if k in th else ''))
    out.append(json.dumps(v, ensure_ascii=False))
    for x in inl.get(k, []):
        out.append('   INL %s | %s | AUTO: %s' % (x['cit'], x['en'], x['auto']))
        if not x['auto']:
            for vv, t in x['verses'].items(): out.append('      V %s: %s' % (vv, t))
open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src_%s.txt' % p), 'w', encoding='utf-8').write('\n'.join(out))
