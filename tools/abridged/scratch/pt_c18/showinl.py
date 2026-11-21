import json,sys,re
i=json.load(open('work/inline_pt_c18.json',encoding='utf-8'))
for k,v in i.items():
  if k.split('.')[0] not in sys.argv[1:]: continue
  for x in v:
    print('==',k,x['cit'],'|',x['en'],'| AUTO:',x['auto'])
    if not x['auto']:
      # print only first verse fully, others truncated
      for c,t in x['verses'].items(): print('   ',c,t[:1500])
