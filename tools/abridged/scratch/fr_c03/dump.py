import json,sys
src=json.load(open('work/src_c03.json',encoding='utf-8'))
inl=json.load(open('work/inline_fr_c03.json',encoding='utf-8'))
hints=json.load(open('work/title_hints_fr.json',encoding='utf-8'))
p=sys.argv[1]
for k,v in src.items():
    if k.split('.')[0]!=p: continue
    print('##',k, ('HINT='+hints[k]) if k in hints else '')
    print(json.dumps(v,ensure_ascii=False))
    for q in inl.get(k,[]):
        print('   IQ',q['cit'],'|EN:',q['en'],'|AUTO:',q['auto'] if q['auto'] else ('NONE '+json.dumps(q['verses'],ensure_ascii=False)))
