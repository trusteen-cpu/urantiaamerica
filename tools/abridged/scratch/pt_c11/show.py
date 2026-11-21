import json,sys
s=json.load(open('work/src_c11.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in s.items():
  if k.split('.')[0]==p and not (k.endswith('.h') or k.endswith('.title')):
    print('##',k); print(json.dumps(v,ensure_ascii=False) if isinstance(v,list) else v)
