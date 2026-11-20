import json, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
QNA = os.path.dirname(os.path.dirname(HERE))
OUT = os.path.join(QNA, "es", "c03.json")
SRC = os.path.join(QNA, "work_es", "src_c03.json")

def save(units):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    ordered = {k: cur[k] for k in src if k in cur}
    json.dump(ordered, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for k, v in units.items():
        a = src[k]["answer"]; b = v["answer"]
        print(k, "paras", a.count("\n\n"), b.count("\n\n"), "lines", a.count("\n"), b.count("\n"), "bold", a.count("**"), b.count("**"))

if __name__ == "__main__":
    for f in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location("b", os.path.join(HERE, f))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        save(m.U)
