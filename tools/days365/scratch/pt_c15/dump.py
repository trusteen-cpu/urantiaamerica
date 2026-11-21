import json,sys
sys.stdout.reconfigure(encoding='utf-8')
S=json.load(open('work/src_c15.json',encoding='utf-8'))
I=json.load(open('work/inline_pt_c15.json',encoding='utf-8'))
R=json.load(open('work/ref_pt_c15.json',encoding='utf-8'))
for d in sys.argv[1:]:
    u=S[d]
    print('=====',d,u['_ref'],'|',u['t'])
    for i,p in enumerate(u['msg']): print(f'[{i}]',p)
    print('PR:',u['pr'])
    print('--REF PT:',' / '.join(R[d]['pt']))
    seen=set()
    for q in I.get(d,[]):
        print('  Q',q['at'],q['cit'],'EN:',q['en'])
        if q['auto']: print('    AUTO:',q['auto'])
        elif q['cit'] not in seen and not any(q['cit']==c for c in [R[d]['ref']]):
            print('    VERSE:',q['verse'])
        seen.add(q['cit'])
