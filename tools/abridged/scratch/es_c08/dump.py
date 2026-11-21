import json,sys
D=json.load(open('work/src_c08.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in D.items():
    if k.split('.')[0]==p:
        print('##',k, json.dumps(v,ensure_ascii=False) if not isinstance(v,str) else v)
