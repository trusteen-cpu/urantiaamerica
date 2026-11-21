import json, os, sys, importlib
B = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
S = json.load(open(B + r"\work\src_c02.json", encoding="utf-8"))
out_p = B + r"\es\c02.json"
old = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {}
U = dict(old)
for n in range(1, 10):
    try:
        m = importlib.import_module(f"p{n}")
    except ModuleNotFoundError:
        continue
    U.update(m.U)
bad = [k for k in U if k not in S]
D = {k: U[k] for k in S if k in U}
miss = [k for k in S if k not in U]
for k in D:
    a, b = S[k], D[k]
    if type(a) != type(b) or (isinstance(a, list) and len(a) != len(b)):
        print("SHAPE", k)
    if isinstance(b, str) and "\n" in b:
        print("NEWLINE", k)
    if isinstance(b, list) and any("|" in x for x in b):
        print("PIPE", k)
json.dump(D, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("written", len(D), "of", len(S), "| extra keys", bad, "| missing", len(miss), miss[:5])
