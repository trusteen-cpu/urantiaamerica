import json, sys, re
sys.stdout.reconfigure(encoding="utf-8")
en = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
fr = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\fr.json", encoding="utf-8"))
for phrase in sys.argv[1:]:
    print("=====", phrase)
    n = 0
    for k, v in en.items():
        if phrase.lower() in v.lower():
            print(k, "|", fr.get(k, "")[:400])
            n += 1
            if n >= 2:
                break
