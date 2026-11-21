import json,sys
g=json.load(open('../glossary/glossary_es.json',encoding='utf-8'))
for q in sys.argv[1:]:
    for e in g:
        if q.lower() in e[0].lower(): print(e[0],'=>',e[1])
