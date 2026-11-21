import json,sys
sys.stdout.reconfigure(encoding='utf-8')
g=json.load(open('../glossary/glossary_es.json',encoding='utf-8'))
for w in sys.argv[1:]:
    for e in g:
        if w.lower() in e[0].lower(): print(w,'=>',e[0],'|',e[1])
