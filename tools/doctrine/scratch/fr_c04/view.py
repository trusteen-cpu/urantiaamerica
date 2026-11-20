# -*- coding: utf-8 -*-
# python view.py ch18  -> units + FR quotes (compact)
# python view.py v 93:10.5 94:6.2 -> print official FR verses
# python view.py f "Lao" -> search FR text (substring), first 8 hits
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine"
sys.path.insert(0, os.path.join(H, ".."))
import amq
if sys.argv[1] == "v":
    for r in sys.argv[2:]:
        print(r, amq.text("fr", r)); print()
    raise SystemExit
if sys.argv[1] == "f":
    FR = json.load(open(os.path.join(H, "..", "data", "fr.json"), encoding="utf-8"))
    w = sys.argv[2]; n = 0
    for k, t in FR.items():
        i = t.find(w)
        if i >= 0:
            print(k, "…" + t[max(0, i - 80): i + 120] + "…"); n += 1
            if n >= int(sys.argv[3]) if len(sys.argv) > 3 else n >= 8: break
    raise SystemExit
ch = sys.argv[1]
S = json.load(open(os.path.join(H, "src", "c04.json"), encoding="utf-8"))
AUTO = json.load(open(os.path.join(H, "auto_fr.json"), encoding="utf-8"))
MAN = json.load(open(os.path.join(H, "fr", "quotes_c04.json"), encoding="utf-8"))
for k, v in S.items():
    if not k.startswith(ch + ":"): continue
    if isinstance(v, dict) and "cit" in v:
        print(k, "[Q", v["cit"] + "]", MAN.get(k) or AUTO.get(k))
    else:
        print(k, "=>", json.dumps(v, ensure_ascii=False))
