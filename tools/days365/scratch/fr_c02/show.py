import json,sys
S=json.load(open('work/src_c02.json',encoding='utf-8'))
R=json.load(open('work/ref_fr_c02.json',encoding='utf-8'))
I=json.load(open('work/inline_fr_c02.json',encoding='utf-8'))
for k in sys.argv[1:]:
    u=S[k]
    print('=====',k,u['_ref'],'|',u['t'])
    print('REF FR:', ' / '.join(R[k]['fr']))
    for i,p in enumerate(u['msg']): print(f'[{i}]',p)
    print('PR:',u['pr'])
    for q in I.get(k,[]):
        print('  Q',q['at'],q['cit'],'| EN:',q['en'])
        print('    AUTO:',q['auto'])
        if not q['auto']: print('    VERSE:',q['verse'])
