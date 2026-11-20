import json, os
B = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..'))
SRC = os.path.join(B, 'work', 'src_c06.json')
OUT = os.path.join(B, 'pt', 'c06.json')


def save(T):
    src = json.load(open(SRC, encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k in T:
        assert k in src, k
    cur.update(T)
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in out]
    print('saved', len(out), 'of', len(src), 'missing', len(missing))


def tab(cap, rows):
    return {"cap": cap, "rows": rows}


def qs(items):
    return {"title": "Perguntas para reflexão", "items": items}
