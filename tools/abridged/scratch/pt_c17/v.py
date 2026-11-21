import json,sys
pt=json.load(open('../data/pt.json',encoding='utf-8'))
for k in sys.argv[1:]: print(k, pt.get(k)); print()
