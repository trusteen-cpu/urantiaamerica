import json,sys
s=json.load(open('work/src_c03.json',encoding='utf-8'))
h=json.load(open('work/title_hints_pt.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in s.items():
    if k.split('.')[0]!=p: continue
    print('##',k, ('HINT: '+h[k]) if k in h else '')
    if isinstance(v,list):
        for r in v: print('  |'+' | '.join(r))
    else: print(v)
