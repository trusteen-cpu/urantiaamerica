# -*- coding: utf-8 -*-
import json, os, sys, glob, importlib.util
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer"
sys.path.insert(0, os.path.dirname(H))
import pt_old_spelling as P
src = json.load(open(os.path.join(H, "work", "src_c02.json"), encoding="utf-8"))
T = {}
for f in sorted(glob.glob(os.path.join(H, "scratch", "pt_c02", "tr_*.py"))):
    spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    T.update(m.T)

def fx(s):
    s = s.replace("**O que diz *O Livro de Urântia***", "**O que diz O Livro de Urântia**")
    return P.fix(s)

out = {}
for k in src:
    if k in T:
        v = T[k]
        out[k] = [fx(x) for x in v] if isinstance(v, list) else ({a: fx(b) for a, b in v.items()} if isinstance(v, dict) else fx(v))
extra = [k for k in T if k not in src]
print("units", len(out), "/", len(src), "extra", extra)
json.dump(out, open(os.path.join(H, "pt", "c02.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
