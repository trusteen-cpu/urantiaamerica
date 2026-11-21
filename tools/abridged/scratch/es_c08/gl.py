import json,sys
G=json.load(open('../glossary/glossary_es.json',encoding='utf-8'))
for w in sys.argv[1:]:
    hits=[g for g in G if w.lower() in g[0].lower()]
    for g in hits[:6]: print(w,'=>',g[0],'|',g[1])
