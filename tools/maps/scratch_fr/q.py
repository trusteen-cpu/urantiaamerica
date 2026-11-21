import json,re,sys,io
sys.stdout=io.open(sys.stdout.fileno(),'w',encoding='utf-8',closefd=False)
fr=json.load(open('data/fr.json',encoding='utf-8'))
tt=json.load(open('data/fr_titles.json',encoding='utf-8'))
all=' '.join(fr.values())
pats=sys.argv[1:]
for p in pats:
    c={}
    for m in re.finditer(p,all): c[m.group(0)]=c.get(m.group(0),0)+1
    print(p,'=>',sorted(c.items(),key=lambda x:-x[1])[:8])