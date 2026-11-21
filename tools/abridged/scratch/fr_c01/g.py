import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
G=json.load(open(r'E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/glossary/glossary_fr.json',encoding='utf-8'))
for w in sys.argv[1:]:
    for e in G:
        if w.lower() in e[0].lower(): print(e[0],'=>',e[1])
