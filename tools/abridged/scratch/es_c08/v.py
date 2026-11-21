import json,sys,re
D=json.load(open('E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/data/es.json',encoding='utf-8'))
for a in sys.argv[1:]:
    if a.startswith('?'):
        pat=a[1:]; pre=None
        if '@' in pat: pat,pre=pat.split('@')
        n=0
        for k,v in D.items():
            if pre and not k.startswith(pre+('.' if ':' in pre else ':')): continue
            for m in re.finditer(pat,v):
                print(k,'..',v[max(0,m.start()-60):m.end()+60]); n+=1
                break
            if n>=4: break
    else:
        print(a,D[a])
