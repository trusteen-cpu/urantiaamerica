import json, os, sys, glob, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
src = json.load(open(os.path.join(ROOT, "work", "src_c06.json"), encoding="utf-8"))
out_path = os.path.join(ROOT, "fr", "c06.json")
cur = json.load(open(out_path, encoding="utf-8")) if os.path.exists(out_path) else {}
for f in sorted(glob.glob(os.path.join(HERE, "t*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for k, v in m.U.items():
        if k not in src:
            print("UNKNOWN KEY", k); continue
        cur[k] = v
D = {k: cur[k] for k in src if k in cur}
json.dump(D, open(out_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
missing = [k for k in src if k not in D]
print("units", len(D), "/", len(src), "missing", len(missing), missing[:5])
