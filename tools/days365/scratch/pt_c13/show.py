import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('work/src_c13.json',encoding='utf-8'))
inl=json.load(open('work/inline_pt_c13.json',encoding='utf-8'))
ref=json.load(open('work/ref_pt_c13.json',encoding='utf-8'))
for d in sys.argv[1:]:
    u=s[d]; print('=====',d,u['_ref']); print('T:',u['t'])
    for i,p in enumerate(u['msg']): print(f'[{i}]',p)
    print('PR:',u['pr'])
    print('REF-PT:',' | '.join(ref[d]['pt']))
    vs={}
    for q in inl.get(d,[]):
        print('  Q',q['at'],q['cit'],'EN:',q['en'],'\n    AUTO:',q['auto'])
        if not q['auto']: vs[q['cit']]=q['verse']
    for c,v in vs.items(): print('  VERSE',c,':',v)
