import json, os, sys, importlib.util
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work", "src_c05.json")
OUT = os.path.join(BASE, "es", "c05.json")
QOUT = os.path.join(BASE, "es", "quotes_c05.json")

def load(p):
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))
    return {}

def main(mod):
    spec = importlib.util.spec_from_file_location(mod, os.path.join(os.path.dirname(__file__), mod + ".py"))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    src = json.load(open(SRC, encoding="utf-8"))
    cur = load(OUT)
    cur.update(getattr(m, "T", {}))
    bad = [k for k in cur if k not in src]
    if bad:
        print("UNKNOWN KEYS", bad); sys.exit(1)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    Q = load(QOUT); Q.update(getattr(m, "Q", {}))
    json.dump(Q, open(QOUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    pre = mod + "."
    miss = [k for k in src if k.startswith(pre) and k not in D]
    print("saved", len(D), "/", len(src), "quotes", len(Q), "missing in", mod, miss)

if __name__ == "__main__":
    main(sys.argv[1])
