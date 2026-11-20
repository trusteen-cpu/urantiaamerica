import json, os, sys, importlib
H = os.path.dirname(os.path.abspath(__file__))
T = H + "/../.."
SRC = json.load(open(T + "/work/src_c04.json", encoding="utf-8"))
OUT = T + "/pt/c04.json"

def save(units):
    cur = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    cur.update(units)
    for k in units:
        if k not in SRC:
            print("UNKNOWN KEY", k)
    D = {k: cur[k] for k in SRC if k in cur}
    json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("saved", len(D), "/", len(SRC))

if __name__ == "__main__":
    sys.path.insert(0, H)
    for name in sys.argv[1:]:
        m = importlib.import_module(name)
        ch = name
        exp = [k for k in SRC if k.split(".")[0] == ch]
        miss = [k for k in exp if k not in m.U]
        if miss:
            print("MISSING", miss)
        save(m.U)
