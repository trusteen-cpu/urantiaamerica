# -*- coding: utf-8 -*-
# usage: python v.py 38:2.3 39:2.1 ...   or  python v.py ?word
import sys, os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
import amq
for a in sys.argv[1:]:
    if a.startswith("?"):
        print(a, amq.find("es", a[1:], n=8))
        for c in amq.find("es", a[1:], n=3):
            t = amq.text("es", c); i = t.find(a[1:])
            print("  ", c, t[max(0, i - 80): i + 120])
    else:
        print(f"[{a}] {amq.text('es', a)}\n")
