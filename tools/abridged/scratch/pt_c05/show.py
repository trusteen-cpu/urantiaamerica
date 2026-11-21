import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('work/src_c05.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in s.items():
  if k.split('.')[0]==p: print(k,'::',json.dumps(v,ensure_ascii=False))
