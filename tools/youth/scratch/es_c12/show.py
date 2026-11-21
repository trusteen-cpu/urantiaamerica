import json,sys
s=json.load(open('work/src_c12.json',encoding='utf-8'))
q=json.load(open('work/quotes_es_c12.json',encoding='utf-8'))
h=json.load(open('work/headings_es_c12.json',encoding='utf-8'))
ks=list(s); a,b=int(sys.argv[1]),int(sys.argv[2])
for k in ks[a:b]:
    print('##',k,s[k])
    if k in h: print('   HEAD:',h[k]['official'])
    for x in q.get(k,[]):
        print('   Q',x['n'],x['cit'],'|EN:',x['en'],'|HOW:',x['how'],'|AUTO:',x['auto'])
        print('     VERSE:',x['verse'])
