import json, os, re, importlib.util, sys
os.chdir(os.path.join(os.path.dirname(__file__), "..", ".."))
src = json.load(open("work/src_c06.json", encoding="utf-8"))
out_p = "pt/c06.json"
D = json.load(open(out_p, encoding="utf-8")) if os.path.exists(out_p) else {}
here = os.path.dirname(os.path.abspath(__file__))
SP = [("cinquenta", "cinqüenta"), ("Cinquenta", "Cinqüenta"), ("sequência", "seqüência"),
      ("consequência", "conseqüência"), ("Consequência", "Conseqüência"), ("frequente", "freqüente"),
      ("ideia", "idéia"), ("Ideia", "Idéia"), ("subsequente", "subseqüente"), ("tranquil", "tranqüil")]
def fix(v):
    if isinstance(v, list):
        return [fix(x) for x in v]
    for a, b in SP:
        v = v.replace(a, b)
    return v
for fn in sorted(os.listdir(here)):
    if re.fullmatch(r"p\d+\.py", fn):
        spec = importlib.util.spec_from_file_location(fn[:-3], os.path.join(here, fn))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for k, v in m.P.items():
            assert k in src, k
            if isinstance(src[k], list):
                assert isinstance(v, list) and len(v) == len(src[k]), k
            D[k] = fix(v)
R = {k: D[k] for k in src if k in D}
json.dump(R, open(out_p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("done", len(R), "/", len(src), "missing:", [k for k in src if k not in R][:5])
