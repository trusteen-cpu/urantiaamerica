import json, sys, re
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
FR = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\fr.json", encoding="utf-8"))
sys.stdout.reconfigure(encoding="utf-8")
# usage: look.py "phrase" [maxhits]   or  look.py =25:2.3
for a in sys.argv[1:]:
    if a.startswith("="):
        c = a[1:]
        print("##", c, "\nEN:", EN.get(c), "\nFR:", FR.get(c)); continue
    hits = [c for c, v in EN.items() if a.lower() in v.lower()][:2]
    print("########", a, len(hits))
    for c in hits:
        print("  ", c, "EN:", EN[c][:300])
        print("  ", c, "FR:", FR.get(c, "")[:700])
