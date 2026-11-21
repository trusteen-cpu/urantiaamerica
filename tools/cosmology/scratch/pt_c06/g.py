import json,sys
g=json.load(open('../glossary/glossary_pt.json',encoding='utf-8'))
for t in sys.argv[1:]:
    hits=[x for x in g if t.lower() in x[0].lower()]
    print(t,'->',' ; '.join(f'{x[0]}={x[1]}' for x in hits[:6]))
