import json,sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
D=json.load(open('../data/es.json',encoding='utf-8'))
for r in sys.argv[1:]:
    print(r,':',D.get(r,'??'))
