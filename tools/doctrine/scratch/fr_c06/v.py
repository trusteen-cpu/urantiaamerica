# -*- coding: utf-8 -*-
# python v.py 5:3.2 T27 T27.7 ?word chNN  -> prints FR verses / titles / search / src chapter
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, os.path.join(H, ".."))
import amq
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
for a in sys.argv[1:]:
    if a.startswith("T"):
        p = a[1:].split(".")
        print(a, amq.title("fr", int(p[0]), int(p[1]) if len(p) > 1 else None))
    elif a.startswith("?"):
        print(a, amq.find("fr", a[1:], 8))
    elif a.startswith("ch"):
        d = json.load(open(os.path.join(H, "work", "src_c06.json"), encoding="utf-8"))
        for k, v in d.items():
            if k.split(":")[0] == a: print(k, json.dumps(v, ensure_ascii=False))
    else:
        print("==", a, "\nEN:", EN.get(a), "\nFR:", amq.text("fr", a))
