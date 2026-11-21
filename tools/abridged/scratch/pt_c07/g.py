import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
G=json.load(open('../glossary/glossary_pt.json',encoding='utf-8'))
for term in sys.argv[1:]:
    hits=[g for g in G if term.lower() in g[0].lower()]
    for g in hits[:6]: print(term,'=>',g[0],'|',g[1])
    if not hits: print(term,'=> NONE')
