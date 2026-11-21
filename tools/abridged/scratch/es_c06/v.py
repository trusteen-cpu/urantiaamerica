import json,sys,os,re
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
D=json.load(open('data/es.json',encoding='utf-8'))
for a in sys.argv[1:]:
    if a.startswith('?'):
        pat=a[1:]
        n=0
        for k,v in D.items():
            for m in re.finditer(pat,v):
                print(k, '...'+v[max(0,m.start()-60):m.end()+60]+'...'); n+=1
                break
            if n>=12: break
    else:
        print(a, D[a]); print()
