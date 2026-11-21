import json,re,sys,collections
sys.stdout.reconfigure(encoding='utf-8')
T=json.load(open('../../data/pt.json',encoding='utf-8'))
for pat in sys.argv[1:]:
    c=collections.Counter()
    for v in T.values():
        for m in re.findall(pat,v): c[m]+=1
    print(pat,'->',c.most_common(6))
