import json,sys
sys.stdout.reconfigure(encoding='utf-8')
B='work/'
d=json.load(open(B+'src_c14.json',encoding='utf-8'))
q=json.load(open(B+'quotes_es_c14.json',encoding='utf-8'))
h=json.load(open(B+'headings_es_c14.json',encoding='utf-8'))
pfx=sys.argv[1]
for k,v in d.items():
    if not k.startswith(pfx+'.'): continue
    print('##',k,v)
    if k in h: print('   HEAD:',h[k])
    for i,x in enumerate(q.get(k,[])):
        if x['auto'] is None:
            print('   TODO#%d %s EN=%s\n      VERSE=%s'%(i,x['cit'],x['en'],x['verse']))
        else:
            print('   AUTO#%d %s [%s] %s'%(i,x['cit'],x['how'],x['auto']))
            if x['how']=='positional': print('      EN=%s\n      VERSE=%s'%(x['en'],x['verse']))
