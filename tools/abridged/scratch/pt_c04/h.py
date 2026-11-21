import json,sys,io,re
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
D=json.load(open('../data/pt.json',encoding='utf-8'))
# print first 90 chars of verses in given paper:section
for a in sys.argv[1:]:
    p,s=a.split(':')
    i=0
    for k,v in D.items():
        if k.startswith(f"{p}:{s}."): print(k, v[:int(90)])
