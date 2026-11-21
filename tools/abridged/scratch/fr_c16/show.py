import json,sys
d=json.load(open('work/src_c16.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in d.items():
    if k.split('.')[0]==p:
        print(k, json.dumps(v,ensure_ascii=False))
