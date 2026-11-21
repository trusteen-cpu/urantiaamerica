import json,sys
B='../../'
src=json.load(open(B+'work/src_c14.json',encoding='utf-8'))
inl=json.load(open(B+'work/inline_fr_c14.json',encoding='utf-8'))
ref=json.load(open(B+'work/ref_fr_c14.json',encoding='utf-8'))
days=sys.argv[1:]
out=open('view.txt','w',encoding='utf-8')
for d in days:
    u=src[d]
    out.write('=== %s\n'%d)
    out.write(json.dumps(u,ensure_ascii=False,indent=1)+'\n')
    out.write('REF '+ref[d]['ref']+' FR: '+' | '.join(ref[d]['fr'])+'\n')
    seen=set()
    for q in inl.get(d,[]):
        out.write('Q %s %s EN=%s\n  AUTO=%s\n'%(q['at'],q['cit'],q['en'],q['auto']))
        if q['auto'] is None and q['cit'] not in seen:
            seen.add(q['cit']); out.write('  VERSE=%s\n'%q['verse'])
