import json,sys
sys.stdout.reconfigure(encoding='utf-8')
q=json.load(open('work/quotes_es_c09.json',encoding='utf-8'))
for u,L in q.items():
  for x in L:
    print('==',u,x['n'],x['cit'],x.get('how'),'|EN:',x['en'])
    print('  AUTO:',x['auto'])
    if not x['auto']: print('  VERSE:',x['verse'])
