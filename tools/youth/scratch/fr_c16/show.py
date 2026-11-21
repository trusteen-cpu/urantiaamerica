import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('work/src_c16.json',encoding='utf-8'))
q=json.load(open('work/quotes_fr_c16.json',encoding='utf-8'))
ks=list(s); a,b=int(sys.argv[1]),int(sys.argv[2])
for k in ks[a:b]:
    print(k,'|',s[k])
    for i,x in enumerate(q.get(k,[])):
        print('   #%d %s [%s] auto=%s'%(i,x['cit'],x['how'],x['auto']))
        if x['how']!='whole': print('      VERSE:',x['verse'])
    print()
