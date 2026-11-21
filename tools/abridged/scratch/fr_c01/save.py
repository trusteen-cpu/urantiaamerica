import json, os, sys
BASE = r'E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged'
OUT = os.path.join(BASE, 'fr', 'c01.json')

def add(D):
    src = json.load(open(os.path.join(BASE, 'work', 'src_c01.json'), encoding='utf-8'))
    cur = {}
    if os.path.exists(OUT):
        cur = json.load(open(OUT, encoding='utf-8'))
    for k, v in D.items():
        if k not in src:
            print('UNKNOWN KEY', k); continue
        s = src[k]
        if isinstance(s, list):
            if not isinstance(v, list) or len(v) != len(s) or any(len(a) != len(b) for a, b in zip(v, s)):
                print('SHAPE MISMATCH', k); continue
        cur[k] = v
    out = {k: cur[k] for k in src if k in cur}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    missing = [k for k in src if k not in out]
    print('saved', len(out), '/', len(src), 'missing', len(missing))
