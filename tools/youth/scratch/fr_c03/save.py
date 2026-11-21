import json, os, importlib.util, sys
HERE = os.path.dirname(os.path.abspath(__file__))
YOUTH = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(YOUTH, "fr", "c03.json")
SRC = json.load(open(os.path.join(YOUTH, "work", "src_c03.json"), encoding="utf-8"))


def merge(T):
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(T)
    D = {k: cur[k] for k in SRC if k in cur}
    extra = [k for k in T if k not in SRC]
    if extra:
        print("UNKNOWN KEYS", extra)
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(SRC))


if __name__ == "__main__":
    for p in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location("m", os.path.join(HERE, p))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        merge(m.T)
