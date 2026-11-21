import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
T=json.load(open(r'E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\es.json',encoding='utf-8'))
E=json.load(open(r'E:\OneDrive\유란시아 작업\theology-book\en.json',encoding='utf-8'))
args=open(sys.argv[1],encoding='utf-8').read().split('\n')
for a in args:
    a=a.strip()
    if not a: continue
    if a.startswith('EN:'):
        w=a[3:]; hits=[k for k,v in E.items() if w in v][:3]
        print('EN',w,hits)
        for k in hits[:2]:
            print('   ',k,T.get(k,'')[:300])
        continue
    hits=[k for k,v in T.items() if a.lower() in v.lower()]
    print(len(hits),a,hits[:3])
