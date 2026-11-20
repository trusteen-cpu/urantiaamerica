import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from save import save

D = json.load(open("es/c01.json", encoding="utf-8"))
t = D["ch00:7"]
for row in t["rows"][1:]:
    c = row[3]
    parts = [p.strip() for p in c.split(",")]
    if len(parts) >= 3:
        row[3] = ", ".join(parts[:-1]) + " y " + parts[-1]
save({"ch00:7": t})
print([r[3] for r in t["rows"]])
