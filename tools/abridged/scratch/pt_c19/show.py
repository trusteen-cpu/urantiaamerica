import json,sys
s=json.load(open('work/src_c19.json',encoding='utf-8'))
h=json.load(open('work/title_hints_pt.json',encoding='utf-8'))
for k,v in s.items():
  if k.split('.')[0] in sys.argv[1:]:
    print(k, '=>', json.dumps(v,ensure_ascii=False))
    if k in h: print('   HINT', h[k])
