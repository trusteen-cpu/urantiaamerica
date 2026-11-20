import json
from save import merge, OUT

cur = json.load(open(OUT, encoding="utf-8"))
t = cur["ch00:7"]
fixed = []
for row in t["rows"]:
    c = row[-1]
    parts = c.split(", ")
    if len(parts) >= 3:
        c = ", ".join(parts[:-1]) + " e " + parts[-1]
    fixed.append(row[:-1] + [c])
t["rows"] = fixed
merge({"ch00:7": t})
