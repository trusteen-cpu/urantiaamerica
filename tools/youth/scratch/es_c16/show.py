import json,sys
sys.stdout.reconfigure(encoding='utf-8')
B='work/'
src=json.load(open(B+'src_c16.json',encoding='utf-8'))
q=json.load(open(B+'quotes_es_c16.json',encoding='utf-8'))
h=json.load(open(B+'headings_es_c16.json',encoding='utf-8'))
paper=sys.argv[1]
for k,v in src.items():
    if k.split('.')[0]!='p'+paper: continue
    print('==',k,v)
    if k in h: print('   HEAD:',json.dumps(h[k],ensure_ascii=False))
    for x in q.get(k,[]):
        print('   Q#%d %s how=%s why=%s'%(x['n'],x['cit'],x['how'],x.get('why')))
        print('     EN:',x['en'])
        print('     AUTO:',x['auto'])
        if not x['auto'] or x['how']=='positional': print('     VERSE:',x['verse'])
