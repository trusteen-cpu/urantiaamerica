import json, re, os
os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))
d = json.load(open("pt/c06.json", encoding="utf-8"))
pats = ['"', r"\b(the|and|of|which|with)\b", r"orig\. p", r"Nebadon\b", r"Orvonton", r"Urantia\b", r"Satania\b", r"Salvington"]
for k, v in d.items():
    s = " | ".join(v) if isinstance(v, list) else v
    for p in pats:
        if re.search(p, s):
            print(k, p, s[:90])
