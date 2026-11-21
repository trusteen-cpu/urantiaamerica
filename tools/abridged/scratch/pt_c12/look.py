import json, sys, os
sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
pt = json.load(open(os.path.join(T, "data", "pt.json"), encoding="utf-8"))
en = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
mode = sys.argv[1]
if mode == "v":  # show verses en+pt
    for c in sys.argv[2:]:
        print(c, "EN:", en.get(c)); print(c, "PT:", pt.get(c)); print()
elif mode == "g":  # glossary search
    g = json.load(open(os.path.join(T, "glossary", "glossary_pt.json"), encoding="utf-8"))
    for w in sys.argv[2:]:
        for row in g:
            if w.lower() in row[0].lower():
                print(w, "=>", row[0], "|", row[1])
elif mode == "f":  # find pt word, print snippets
    w = sys.argv[2]; n = int(sys.argv[3]) if len(sys.argv) > 3 else 5
    k = 0
    for c, t in pt.items():
        i = t.find(w)
        if i >= 0:
            print(c, t[max(0, i-80):i+120]); k += 1
            if k >= n: break
