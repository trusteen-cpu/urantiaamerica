import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('work/src_c01.json',encoding='utf-8'))
h=json.load(open('work/title_hints_fr.json',encoding='utf-8'))
inl=json.load(open('work/inline_fr_c01.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in s.items():
    if k.split('.')[0]!=p: continue
    print('##',k, ('HINT: '+h[k]) if k in h else '')
    print(json.dumps(v,ensure_ascii=False) if not isinstance(v,str) else v)
    if k in inl:
        for x in inl[k]: print('  INL', x['cit'], '|', x['en'], '| AUTO:', x['auto'])
