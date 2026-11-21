import json,sys,re
sys.stdout.reconfigure(encoding='utf-8')
T=r"E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/"
fr=json.load(open(T+"data/fr.json",encoding='utf-8'))
en=json.load(open(r"E:/OneDrive/유란시아 작업/theology-book/en.json",encoding='utf-8'))
gl=json.load(open(T+"glossary/glossary_fr.json",encoding='utf-8'))
mode=sys.argv[1]
for w in sys.argv[2:]:
    print("###",w)
    if mode=="g":
        for e in gl:
            if w.lower() in e[0].lower(): print("  ",e[0],"=>",e[1])
    elif mode=="e":  # find English phrase, show fr window
        n=0
        for k,v in en.items():
            if w.lower() in v.lower():
                print("  ",k,"|",fr.get(k,"")[:300]); n+=1
                if n>=3: break
    elif mode=="f":
        n=0
        for k,v in fr.items():
            i=v.lower().find(w.lower())
            if i>=0:
                print("  ",k,"|",v[max(0,i-80):i+120]); n+=1
                if n>=4: break
