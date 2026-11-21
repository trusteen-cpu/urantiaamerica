import json,sys
B='../../'
src=json.load(open(B+'work/src_c14.json',encoding='utf-8'))
inl=json.load(open(B+'work/inline_es_c14.json',encoding='utf-8'))
ks=list(src)
a,b=int(sys.argv[1]),int(sys.argv[2])
for k in ks[a:b]:
    print('=====',k,json.dumps(src[k],ensure_ascii=False,indent=0))
    for q in inl.get(k,[]):
        print('  Q',q['at'],q['cit'],'| EN:',q['en'],'| AUTO:',q['auto'])
        if not q['auto']: print('     VERSE:',q['verse'])
