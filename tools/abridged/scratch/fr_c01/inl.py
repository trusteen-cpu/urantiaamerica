import json,sys
sys.stdout.reconfigure(encoding='utf-8')
inl=json.load(open('work/inline_fr_c01.json',encoding='utf-8'))
for k,v in inl.items():
    if k.split('.')[0]!=sys.argv[1]: continue
    for x in v:
        print('##',k,x['cit'],'|',x['en'],'| AUTO:',x['auto'])
        for c,t in x['verses'].items(): print('   ',c,':',t)
