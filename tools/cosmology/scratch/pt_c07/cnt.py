import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('../data/pt.json',encoding='utf-8'))
for w in sys.argv[1:]:
    hits=[k for k,v in d.items() if w in v]
    print(w, len(hits), hits[:6])
