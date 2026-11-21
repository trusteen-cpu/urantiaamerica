import json,sys
B=json.load(open('../data/pt.json',encoding='utf-8'))
for c in sys.argv[1:]: print(c, B[c]); print()
