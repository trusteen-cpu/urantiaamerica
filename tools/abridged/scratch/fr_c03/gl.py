import json,sys
g=json.load(open('glossary/glossary_fr.json',encoding='utf-8'))
for t in sys.argv[1:]:
    hits=[x for x in g if t.lower() in x[0].lower()]
    for x in hits[:6]: print(t,'=>',x[0],'|',x[1])
    if not hits: print(t,'=> ???')
