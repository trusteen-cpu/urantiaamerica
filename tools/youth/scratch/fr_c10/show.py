import json,sys
sys.stdout.reconfigure(encoding='utf-8')
s=json.load(open('work/src_c10.json',encoding='utf-8'))
q=json.load(open('work/quotes_fr_c10.json',encoding='utf-8'))
h=json.load(open('work/headings_fr_c10.json',encoding='utf-8'))
ks=list(s); a,b=int(sys.argv[1]),int(sys.argv[2])
for k in ks[a:b]:
    print('##',k, ('H '+json.dumps(h[k]['official'],ensure_ascii=False)) if k in h else '')
    print(s[k])
    for e in q.get(k,[]):
        print('  Q',e['n'],e['cit'],e['how'],'AUTO:',e['auto'])
        if e['auto'] is None or e['how']=='positional': print('  VERSE:',e['verse'])
