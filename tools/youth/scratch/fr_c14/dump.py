import json,sys
src=json.load(open('work/src_c14.json',encoding='utf-8'))
q=json.load(open('work/quotes_fr_c14.json',encoding='utf-8'))
h=json.load(open('work/headings_fr_c14.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in src.items():
    if k.split('.')[0]!=p: continue
    print('##',k,v)
    if k in h: print('   HEAD:',h[k])
    for i,x in enumerate(q.get(k,[])):
        print('   Q#%d %s how=%s\n     EN: %s\n     AUTO: %s\n     VERSE: %s'%(i,x['cit'],x['how'],x['en'],x['auto'],x['verse']))
