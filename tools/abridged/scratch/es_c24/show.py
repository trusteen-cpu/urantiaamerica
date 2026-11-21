import json, os, sys
sys.stdout.reconfigure(encoding='utf-8')
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
src = json.load(open(os.path.join(BASE, 'work', 'src_c24.json'), encoding='utf-8'))
inl = json.load(open(os.path.join(BASE, 'work', 'inline_es_c24.json'), encoding='utf-8'))
hints = json.load(open(os.path.join(BASE, 'work', 'title_hints_es.json'), encoding='utf-8'))
p = sys.argv[1]
seen=set()
for k, v in src.items():
    if k.split('.')[0] != p:
        continue
    h = hints.get(k)
    print('##', k, ('  HINT: ' + h) if h else '')
    print(json.dumps(v, ensure_ascii=False) if isinstance(v, list) else v)
    if k in inl:
        for x in inl[k]:
            print('   INLINE', x['cit'], '|', x['en'], '| AUTO:', x['auto'])
            if not x['auto']:
                for vk, vt in x['verses'].items():
                    print('     ', vk, vt if vk not in seen else '(seen)')
                    seen.add(vk)
