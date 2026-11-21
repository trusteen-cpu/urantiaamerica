import json, os, sys, importlib.util
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', '..', 'pt', 'c10.json')
SRC = os.path.join(HERE, '..', '..', 'work', 'src_c10.json')

def save(units):
    src = json.load(open(SRC, encoding='utf-8'))
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(units)
    out = {}
    for k in src:
        if k in D:
            u = D[k]
            out[k] = {"_ref": src[k]["_ref"], "t": u["t"], "msg": u["msg"], "pr": u["pr"]}
            assert len(u["msg"]) == len(src[k]["msg"]), k
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), 'units')

if __name__ == '__main__':
    for p in sys.argv[1:]:
        spec = importlib.util.spec_from_file_location('m', os.path.join(HERE, p))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        save(m.U)
