import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
base = os.path.join(here, "..", "..")
src = json.load(open(os.path.join(base, "work", "src_c01.json"), encoding="utf-8"))
es = json.load(open(os.path.join(base, "es", "c01.json"), encoding="utf-8"))
ch = sys.argv[1]
out = []
for k, v in src.items():
    if k.startswith(ch + ":"):
        out.append("### " + k)
        out.append("EN: " + json.dumps(v, ensure_ascii=False))
        out.append("ES: " + json.dumps(es.get(k), ensure_ascii=False))
open(os.path.join(here, "dump_" + ch + ".txt"), "w", encoding="utf-8").write("\n".join(out))
