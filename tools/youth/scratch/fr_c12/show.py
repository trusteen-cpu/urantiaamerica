import json,sys
s=json.load(open('work/src_c12.json',encoding='utf-8'))
q=json.load(open('work/quotes_fr_c12.json',encoding='utf-8'))
lo,hi=sys.argv[1],sys.argv[2]
for k,v in s.items():
    p=int(k[1:].split('.')[0])
    if int(lo)<=p<=int(hi):
        print(k,v)
        for x in q.get(k,[]):
            print('   Q#%d %s en=%r auto=%r how=%s'%(x['n'],x['cit'],x['en'],x['auto'],x['how']))
            print('      VERSE:',x['verse'])
