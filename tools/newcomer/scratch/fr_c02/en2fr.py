import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
FR = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\fr.json", encoding="utf-8"))
for q in sys.argv[1:]:
    print("==", q)
    n = 0
    for k, v in EN.items():
        if q.lower() in v.lower():
            print(k, "|", FR.get(k, "")[:700]); n += 1
            if n >= 3: break
