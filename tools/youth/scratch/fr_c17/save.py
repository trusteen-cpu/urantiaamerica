import json, os
B = 'E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/youth/'
OUT = B + 'fr/c17.json'

def save(new):
    src = json.load(open(B + 'work/src_c17.json', encoding='utf-8'))
    cur = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k in new:
        assert k in src, k
    cur.update(new)
    D = {k: cur[k] for k in src if k in cur}
    json.dump(D, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(D), '/', len(src))
