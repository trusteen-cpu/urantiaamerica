import json,sys
sys.stdout.reconfigure(encoding='utf-8')
T=json.load(open('data/pt.json',encoding='utf-8'))
for k in sys.argv[1].split(','): print(k,T[k][:700]);print()
