import json
P='fr/c10.json'
D=json.load(open(P,encoding='utf-8'))
s=json.load(open('work/src_c10.json',encoding='utf-8'))
D['p111.022']=D['p111.022'].replace('\u00ab \u27e6Q 111:6.10','Car \u00ab \u27e6Q 111:6.10')
D['p111.025']=D['p111.025'].replace('dont elle avait','dont il avait')
assert set(D)==set(s), set(s)^set(D)
D={k:D[k] for k in s}
json.dump(D,open(P,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print(len(D))
