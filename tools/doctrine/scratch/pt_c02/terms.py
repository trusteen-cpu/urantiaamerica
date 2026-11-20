import json, sys, os, re
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
g = json.load(open("../glossary/glossary_pt.json", encoding="utf-8"))
pt = json.load(open("../data/pt.json", encoding="utf-8"))
terms = sys.argv[1:]
for t in terms:
    if t.startswith("@"):
        v = t[1:]
        print("==", v, ":", pt.get(v, "")[:600])
        continue
    if t.startswith("?"):
        w = t[1:]
        hits = [(k, v) for k, v in pt.items() if w in v]
        print("==", w, len(hits))
        for k, v in hits[:4]:
            i = v.find(w)
            print("  ", k, v[max(0, i-80):i+100])
        continue
    print("==", t)
    n = 0
    for row in (g if isinstance(g, list) else g.items()):
        s = json.dumps(row, ensure_ascii=False)
        if t.lower() in s.lower():
            print("  ", s[:200]); n += 1
            if n > 4: break
