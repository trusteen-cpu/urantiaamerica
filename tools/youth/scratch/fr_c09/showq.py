import json
q=json.load(open('work/quotes_fr_c09.json',encoding='utf-8'))
for u,L in q.items():
    for x in L:
        print('==',u,x['n'],x['cit'],x['how'],'|EN:',x['en'])
        print('  AUTO:',x['auto'])
        if not x['auto']: print('  V:',x['verse'])
