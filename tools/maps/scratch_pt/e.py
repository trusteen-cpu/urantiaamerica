import json,re,sys
sys.stdout.reconfigure(encoding='utf-8')
E=json.load(open(r'E:\OneDrive\유란시아 작업\theology-book\en.json',encoding='utf-8'))
T=json.load(open('../../data/pt.json',encoding='utf-8'))
pat,ppat=sys.argv[1],sys.argv[2]
for k,v in E.items():
    if re.search(pat,v):
        m=re.findall(ppat,T.get(k,''))
        print(k,m); 
