import json,sys
sys.stdout.reconfigure(encoding='utf-8')
S=json.load(open('work/src_c15.json',encoding='utf-8'))
I=json.load(open('work/inline_es_c15.json',encoding='utf-8'))
R=json.load(open('work/ref_es_c15.json',encoding='utf-8'))
for d in sys.argv[1:]:
    print('=====',d)
    print(json.dumps(S[d],ensure_ascii=False,indent=0))
    print('REF',R[d]['ref'],'es:',' / '.join(R[d]['es']))
    seen=set(' / '.join(R[d]['es']).split(' / '))
    for q in I.get(d,[]):
        print('--',q['at'],q['cit'],'| EN:',q['en'])
        if q['auto']: print('   AUTO:',q['auto'])
        elif q['verse'] in seen: print('   (verse = ref above)')
        else: print('   VERSE:',q['verse']); seen.add(q['verse'])
