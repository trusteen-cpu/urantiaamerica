import json, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
g = json.load(open('../glossary/glossary_fr.json', encoding='utf-8'))
for term in sys.argv[1:]:
    t = term.lower()
    hits = [x for x in g if t in x[0].lower()]
    for x in hits[:6]:
        print(term, '->', x[0], '=', x[1])
    if not hits:
        print(term, '-> (none)')
