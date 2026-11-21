import json,sys
d=json.load(open('work/src_c16.json',encoding='utf-8'))
h=json.load(open('work/title_hints_pt.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in d.items():
    if k.split('.')[0]!=p: continue
    print('##',k, ('  [HINT: '+h[k]+']') if k in h else '')
    print(json.dumps(v,ensure_ascii=False) if not isinstance(v,str) else v)
