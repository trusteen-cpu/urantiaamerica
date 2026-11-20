import json, os, re
H = os.path.dirname(os.path.abspath(__file__))
OUT = H + "/../../pt/c04.json"
D = json.load(open(OUT, encoding="utf-8"))
R = [("ideia", "idéia"), ("Ideia", "Idéia"), ("frequente", "freqüente"), ("Frequente", "Freqüente"),
     ("consequ", "conseqü"), ("autorrealiza", "auto-realiza"), ("tranquil", "tranqüil")]
n = 0
for k, v in D.items():
    w = v
    for a, b in R:
        w = w.replace(a, b)
    if w != v:
        n += 1
        D[k] = w
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("changed", n)
