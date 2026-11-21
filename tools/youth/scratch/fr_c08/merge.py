import json, os, sys, importlib.util
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = os.path.join(BASE, "work", "src_c08.json")
OUT = os.path.join(BASE, "fr", "c08.json")

def merge(T):
    src = json.load(open(SRC, encoding="utf-8"))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding="utf-8"))
    for k in T:
        if k not in src:
            raise SystemExit("unknown key " + k)
    cur.update(T)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(src))

if __name__ == "__main__":
    for p in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location("m", p)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        merge(m.T)
