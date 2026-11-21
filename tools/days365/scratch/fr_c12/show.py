import json,sys
B='E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/days365/'
s=json.load(open(B+'work/src_c12.json',encoding='utf-8'))
inl=json.load(open(B+'work/inline_fr_c12.json',encoding='utf-8'))
ref=json.load(open(B+'work/ref_fr_c12.json',encoding='utf-8'))
for d in sys.argv[1:]:
    print('=====',d)
    print('REF FR:',' '.join(ref[d]['fr']))
    print(json.dumps(s[d],ensure_ascii=False,indent=0))
    for q in inl.get(d,[]):
        print('Q',q['at'],q['cit'],'| EN:',q['en'])
        if q['auto']: print('  AUTO:',q['auto'])
        else: print('  V:',q['verse'])
