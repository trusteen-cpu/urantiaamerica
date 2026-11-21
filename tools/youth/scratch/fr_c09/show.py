import json,sys
d=json.load(open('work/src_c09.json',encoding='utf-8'))
h=json.load(open('work/headings_fr_c09.json',encoding='utf-8'))
for p in sys.argv[1:]:
    for k,v in d.items():
        if k.split('.')[0]=='p'+p and k not in h: print(k,v)
