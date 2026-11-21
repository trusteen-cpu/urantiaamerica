# -*- coding: utf-8 -*-
import json, os, glob, importlib.util, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
A = os.path.normpath(os.path.join(H, "..", ".."))
src = json.load(open(os.path.join(A, "work", "src_c05.json"), encoding="utf-8"))
D = {}
for f in sorted(glob.glob(os.path.join(H, "p*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    D.update(m.D)
extra = [k for k in D if k not in src]
if extra: print("EXTRA KEYS", extra)
out = {k: D[k] for k in src if k in D}
missing = [k for k in src if k not in D]
for k in out:
    a, b = src[k], out[k]
    if type(a) != type(b): print("TYPE", k)
    elif isinstance(a, list):
        if len(a) != len(b) or any(len(x) != len(y) for x, y in zip(a, b)): print("SHAPE", k)
json.dump(out, open(os.path.join(A, "fr", "c05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
Q = {}
qf = os.path.join(H, "quotes.py")
if os.path.exists(qf):
    spec = importlib.util.spec_from_file_location("quotes", qf)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); Q = m.Q
    json.dump(Q, open(os.path.join(A, "fr", "quotes_c05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("units", len(out), "/", len(src), "missing", len(missing), "quotes", len(Q))
