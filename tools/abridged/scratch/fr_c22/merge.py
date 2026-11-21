import json, os, sys, importlib
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, H)
os.chdir(os.path.join(H, "..", ".."))
src = json.load(open("work/src_c22.json", encoding="utf-8"))
out = "fr/c22.json"
D = json.load(open(out, encoding="utf-8")) if os.path.exists(out) else {}
for m in ["p168_170", "p171_173", "p174_176"]:
    if os.path.exists(os.path.join(H, m + ".py")):
        D.update(importlib.import_module(m).T)
extra = [k for k in D if k not in src]
if extra: print("EXTRA", extra)
R = {k: D[k] for k in src if k in D}
for k in R:
    if type(R[k]) != type(src[k]): print("TYPE", k)
    if isinstance(src[k], list) and (len(R[k]) != len(src[k]) or any(len(a) != len(b) for a, b in zip(R[k], src[k]))): print("SHAPE", k)
json.dump(R, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(R), "/", len(src), "missing:", [k for k in src if k not in R][:5])
