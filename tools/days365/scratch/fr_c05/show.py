import json,sys
d=json.load(open('work/src_c05.json',encoding='utf-8'))
r=json.load(open('work/ref_fr_c05.json',encoding='utf-8'))
for k in sys.argv[1:]:
    print('=====',k,d[k]['_ref'],'|',d[k]['t'])
    print('REF:',r[k]['fr'])
    for i,p in enumerate(d[k]['msg']): print(i,p)
    print('PR:',d[k]['pr'])
