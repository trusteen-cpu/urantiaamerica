import json, os, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
src = json.load(open(os.path.join(ROOT, "work", "src_c03.json"), encoding="utf-8"))
out_path = os.path.join(ROOT, "pt", "c03.json")
D = {}
if os.path.exists(out_path):
    D = json.load(open(out_path, encoding="utf-8"))
for name in sorted(os.listdir(BASE)):
    if name.startswith("p") and name.endswith(".py"):
        spec = importlib.util.spec_from_file_location(name[:-3], os.path.join(BASE, name))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.T.items():
            if k not in src:
                print("UNKNOWN KEY", k); continue
            if isinstance(src[k], list) and (not isinstance(v, list) or len(v) != len(src[k])):
                print("CELL MISMATCH", k)
            D[k] = v
O = {k: D[k] for k in src if k in D}
json.dump(O, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("saved", len(O), "/", len(src))
missing = [k for k in src if k not in O]
print("missing", missing[:10], len(missing))
