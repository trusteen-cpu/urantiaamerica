import json, os
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "es", "c05.json")
D = json.load(open(OUT, encoding="utf-8"))
s = json.dumps(D, ensure_ascii=False)
n = s.count("reino de los cielos")
s = s.replace("reino de los cielos", "reino del cielo")
json.dump(json.loads(s), open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("replaced", n)
