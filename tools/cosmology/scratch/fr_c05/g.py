import json,sys
G=json.load(open('../glossary/glossary_fr.json',encoding='utf-8'))
for t in sys.argv[1:]:
    hits=[g for g in G if t.lower() in g[0].lower()]
    print(t,'->',' ; '.join(f"{h[0]}={h[1]}" for h in hits[:6]))
