import json,sys
G=json.load(open('../glossary/glossary_pt.json',encoding='utf-8'))
for w in sys.argv[1:]:
  for e in G:
    if w.lower() in e[0].lower(): print(e[0],'=>',e[1])
