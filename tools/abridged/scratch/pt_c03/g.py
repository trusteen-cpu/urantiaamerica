import json,sys,re
G=json.load(open('glossary/glossary_pt.json',encoding='utf-8'))
for q in sys.argv[1:]:
    hits=[g for g in G if q.lower() in g[0].lower()]
    print('##',q,':',' ; '.join(f'{g[0]}={g[1]}' for g in hits[:8]))
