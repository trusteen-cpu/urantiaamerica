import json, os, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__))
Y = os.path.dirname(os.path.dirname(H))
for p in ("part1.py", "part2.py", "part3.py"):
    subprocess.run([sys.executable, os.path.join(H, p)], check=True)
src = json.load(open(os.path.join(Y, "work", "src_c05.json"), encoding="utf-8"))
T = {}
for p in ("part1.json", "part2.json", "part3.json"):
    T.update(json.load(open(os.path.join(H, p), encoding="utf-8")))
missing = [k for k in src if k not in T]
extra = [k for k in T if k not in src]
print("missing", missing, "extra", extra)
D = {k: T[k] for k in src if k in T}
os.makedirs(os.path.join(Y, "fr"), exist_ok=True)
json.dump(D, open(os.path.join(Y, "fr", "c05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", len(D))
