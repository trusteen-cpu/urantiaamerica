import json,sys,os
B=os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..'))
s=json.load(open(os.path.join(B,'work','src_c09.json'),encoding='utf-8'))
p=sys.argv[1]
for k,v in s.items():
    if k.split('.')[0]==p: print(k, json.dumps(v,ensure_ascii=False))
