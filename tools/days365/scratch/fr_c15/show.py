import json,sys
sys.stdout.reconfigure(encoding='utf-8')
S=json.load(open('work/src_c15.json',encoding='utf-8'))
I=json.load(open('work/inline_fr_c15.json',encoding='utf-8'))
R=json.load(open('work/ref_fr_c15.json',encoding='utf-8'))
for day in sys.argv[1:]:
    u=S[day]
    print('=====',day,u['_ref'],'|',u['t'])
    print('REF fr:',' / '.join(R[day]['fr']))
    for i,p in enumerate(u['msg']): print(f'[{i}]',p)
    print('PR:',u['pr'])
    seen={}
    for q in I.get(day,[]):
        a=' AUTO: '+q['auto'] if q['auto'] else ''
        print('  --',q['at'],q['cit'],a)
        if not q['auto'] and q['cit']!=u['_ref']: seen[q['cit']]=q['verse']
    for c,v in seen.items(): print('  VERSE',c,':',v)
