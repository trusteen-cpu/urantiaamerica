import json,sys,re
B='E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/youth/'
s=json.load(open(B+'work/src_c17.json',encoding='utf-8'))
q=json.load(open(B+'work/quotes_fr_c17.json',encoding='utf-8'))
h=json.load(open(B+'work/headings_fr_c17.json',encoding='utf-8'))
out=open(B+'scratch/fr_c17/dump.txt','w',encoding='utf-8')
for k,v in s.items():
    out.write('### %s\n%s\n'%(k,v))
    if k in h: out.write('  HEAD: %s\n'%h[k]['official'])
    for i,x in enumerate(q.get(k,[])):
        out.write('  Q#%d %s [%s] EN: %s\n  VERSE: %s\n'%(i,x['cit'],x['how'],x['en'],x['verse']))
        if x['auto']: out.write('  AUTO: %s\n'%x['auto'])
    out.write('\n')
