import json, glob, os, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine"
S = json.load(open(os.path.join(H, "work", "src_c06.json"), encoding="utf-8"))
p = os.path.join(H, "es", "c06.json")
O = json.load(open(p, encoding="utf-8"))
for f in sorted(glob.glob(os.path.join(H, "scratch", "es_c06", "t_*.py"))):
    spec = importlib.util.spec_from_file_location("m", f); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.T.items():
        assert k in S, k
        O[k] = v
D = {k: O[k] for k in S if k in O}
json.dump(D, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(D), "of", len(S), "missing:", [k for k in S if k not in D][:10])
