import json
p='fr/c02.json'
D=json.load(open(p,encoding='utf-8'))
s=json.dumps(D,ensure_ascii=False).replace('naît','nait')
D=json.loads(s)
json.dump(D,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
