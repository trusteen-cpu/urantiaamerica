import json,sys
B=r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged\\"
s=json.load(open(B+r"work\src_c23.json",encoding="utf-8"))
h=json.load(open(B+r"work\title_hints_fr.json",encoding="utf-8"))
p=sys.argv[1]
for k,v in s.items():
    if k.split('.')[0]==p:
        print(k, json.dumps(v,ensure_ascii=False))
        if k in h: print('  HINT', h[k])
