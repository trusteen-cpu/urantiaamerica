# usage: python q.py "english regex" [n]  -> prints matching verses EN snippet + PT text
#        python q.py @pt "pt regex" [n]   -> search in pt
import json, re, sys
sys.stdout.reconfigure(encoding="utf-8")
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
PT = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\pt.json", encoding="utf-8"))
a = sys.argv[1:]
src = EN
if a[0] == "@pt":
    src = PT; a = a[1:]
rx = re.compile(a[0])
n = int(a[1]) if len(a) > 1 else 4
c = 0
for k, v in src.items():
    m = rx.search(v)
    if m:
        s = max(0, m.start() - 80)
        print("==", k, "EN:", EN.get(k, "")[s:m.end() + 80] if src is EN else "")
        pv = PT.get(k, "")
        r=(m.start()/max(1,len(v))) if src is EN else 0
        c0=max(0,int(r*len(pv))-250)
        print("   PT:", pv[c0:c0+500])
        c += 1
        if c >= n:
            break
