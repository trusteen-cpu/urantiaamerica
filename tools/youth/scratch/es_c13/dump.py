import json
s=json.load(open('work/src_c13.json',encoding='utf-8'))
q=json.load(open('work/quotes_es_c13.json',encoding='utf-8'))
h=json.load(open('work/headings_es_c13.json',encoding='utf-8'))
out=open('scratch/es_c13/dump.txt','w',encoding='utf-8')
for k,v in s.items():
    out.write(f'## {k}\n{v}\n')
    if k in h: out.write(f'   HEAD: {h[k]["official"]}\n')
    for x in q.get(k,[]):
        out.write(f'   Q#{x["n"]} {x["cit"]} how={x["how"]}\n     EN: {x["en"]}\n     AUTO: {x["auto"]}\n     VERSE: {x["verse"]}\n')
    out.write('\n')
