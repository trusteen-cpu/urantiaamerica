import json,glob
p='fr/c08.json'
for f in [p]+glob.glob('scratch/fr_c08/p*.py'):
    s=open(f,encoding='utf-8').read()
    s=s.replace('brûler','bruler').replace('goûté','gouté')
    open(f,'w',encoding='utf-8').write(s)
d=json.load(open(p,encoding='utf-8'))
json.dump(d,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
